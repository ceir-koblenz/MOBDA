#Skript zum Import der Daten aus der Homepage Datenbank
#Libraries
#Database Connector
from ibm_db import connect
import ibm_db_dbi
#Pandas ist für den Dataframe 
import pandas as pd
#BeautifulSoup bereinigt HTML Formatierung im CONTENT Feld
from bs4 import BeautifulSoup
#NeoInterface ist Schnittstelle zu Neo4j
import neointerface

#Datenbankverbindung zur UniConnect Datenbank homepage
cnxnhomepage = connect('DATABASE=homepage;'
                 'HOSTNAME=db2.uniconnect.de;'  # localhost would work 
                 'PORT=50000;'
                 'PROTOCOL=TCPIP;'
                 'UID=reader19;'
                 'PWD=b2BwaRHN;', '', '')

connhomepage = ibm_db_dbi.Connection(cnxnhomepage)

#SQL Queries

sqlMicroblogPost = """SELECT be.ENTRY_ID AS id, be.CREATION_DATE AS created, be.UPDATE_DATE  AS last_updated, be.CONTENT AS content, 
be.CONTAINER_ID, person.EXID 
FROM HOMEPAGE.BOARD_ENTRIES be 
JOIN HOMEPAGE.PERSON person ON PERSON.PERSON_ID = BE.actor_uuid
WHERE source <> 'PROFILES'
"""

sqlMicroblog = """SELECT MICROBLOG.BOARD_CONTAINER_ID AS id, PERSON.EXID 
FROM homepage.BOARD microblog
JOIN HOMEPAGE.PERSON  AS person ON MICROBLOG.BOARD_OWNER_ASSOC_ID = PERSON.PERSON_ID 
"""

sqlMicroblogPostComment = """SELECT microblogPostComments.comment_id AS id, microblogPostComments.content AS content, 
microblogPostComments.creation_date AS created, microblogPostComments.entry_id, microblogPostComments.update_date AS last_updated,
users.exid, MICROBLOGPOSTCOMMENTS.ITEM_ID 
FROM homepage.BOARD_COMMENTS AS microblogPostComments
JOIN homepage.BOARD_ENTRIES AS boardEntries ON (microblogPostComments.entry_id = boardEntries.entry_id)
JOIN homepage.PERSON AS users ON (users.person_id = microblogPostComments.actor_uuid)
WHERE category_type = 3  
"""

sqlMicroblogPostAttachment = """ SELECT boref.OBJECT_ID AS id, boref.CREATION_DATE AS created, boref.DISPLAY_NAME AS title, 
BOREF.item_id, person.EXID, REPLACE(BOREF.object_external_id, '-', '') AS match_object_id
FROM homepage.BOARD_OBJECT_REFERENCE boref
JOIN HOMEPAGE.PERSON person ON person.PERSON_ID = boref.AUTHOR_ID 
"""

sqlMicroblogPostLike = """SELECT likes.creation_date AS created, likes.recommendation_id AS id, microblogposts.entry_id, users.exid
FROM HOMEPAGE.BOARD_RECOMMENDATIONS AS likes
JOIN HOMEPAGE.BOARD_ENTRIES AS microblogposts ON likes.item_id = microblogposts.item_id
JOIN HOMEPAGE.PERSON AS users ON (users.person_id = likes.recommender_id) 
 """

sqlMicroblogPostCommentLike = """SELECT likes.recommendation_id AS id, likes.creation_date AS created,  comments.comment_id, users.exid
FROM HOMEPAGE.BOARD_RECOMMENDATIONS AS likes
JOIN HOMEPAGE.BOARD_COMMENTS AS comments ON likes.item_id = comments.item_id
JOIN HOMEPAGE.PERSON AS users ON (users.person_id = likes.recommender_id) 
"""

sqlSocialProfile = """SELECT USER.CREATION_DATE AS created, USER.displayname AS title, USER.person_id AS id, USER.last_update AS last_updated, USER.exid
FROM HOMEPAGE.PERSON AS USER 
WHERE USER.member_type = 0  
"""

sqlSocialProfileFollow= """SELECT socPFollow.follow_id AS id, USERS.EXID, USERS.PERSON_ID 
FROM HOMEPAGE.NR_FOLLOWS AS socPFollow
JOIN HOMEPAGE.PERSON AS users ON (users.person_id = socPFollow.person_id)
"""


sqlSocialProfileComment= """SELECT mainComs.content AS content, mainComs.creation_date AS created, mainComs.entry_id AS id, 
mainComs.update_date AS last_updated, USERS.exid
FROM homepage.BOARD_ENTRIES AS mainComs
JOIN homepage.PERSON AS users ON (users.person_id = mainComs.actor_uuid)
WHERE category_type = 5 
UNION ALL
SELECT socialProfilesComments.content AS content, socialProfilesComments.creation_date AS created, comment_id AS id, socialProfilesComments.update_date AS last_updated, USERS.EXID 
FROM homepage.BOARD_COMMENTS AS socialProfilesComments
JOIN homepage.BOARD_ENTRIES AS boardEntries ON (socialProfilesComments.entry_id = boardEntries.entry_id)
JOIN homepage.PERSON AS users ON (users.person_id = socialProfilesComments.actor_uuid)
WHERE category_type = 5  
"""

sqlSocialProfileCommentLike= """SELECT likes.recommendation_id AS id, likes.creation_date AS created, socPComments.entry_id, users.exid
FROM (SELECT item_id, entry_id FROM Homepage.BOARD_ENTRIES 
	WHERE category_type = 5 
		UNION
	SELECT bCom.item_id, bCom.entry_id FROM HOMEPAGE.BOARD_COMMENTS AS bCom
	JOIN HOMEPAGE.BOARD_ENTRIES AS parent ON bCom.entry_id = parent.entry_id
	WHERE parent.category_type = 5) AS socPComments
JOIN HOMEPAGE.BOARD_RECOMMENDATIONS AS likes ON likes.item_id = socPComments.item_id
JOIN HOMEPAGE.PERSON AS users ON (users.person_id = likes.recommender_id)
"""

sqlSocialProfileCommentAttachment = """SELECT ATTACH.OBJECT_ID AS id, ATTACH.CREATION_DATE AS created, ATTACH.DISPLAY_NAME AS title, USERS.EXID 
FROM (SELECT item_id, entry_id, ACTOR_UUID  FROM Homepage.BOARD_ENTRIES 
	WHERE category_type = 5 
		UNION
	SELECT bCom.item_id, bCom.entry_id, BCOM.ACTOR_UUID  FROM HOMEPAGE.BOARD_COMMENTS AS bCom
	JOIN HOMEPAGE.BOARD_ENTRIES AS parent ON bCom.entry_id = parent.entry_id
	WHERE parent.category_type = 5) AS socPComments
JOIN HOMEPAGE.BOARD_OBJECT_REFERENCE AS ATTACH ON ATTACH.ITEM_ID = socPComments.entry_id
JOIN HOMEPAGE.PERSON AS users ON (USERs.PERSON_ID = socPComments.ACTOR_UUID) 
"""

sqlSocialProfileCommentAttachmentLike = """SELECT  likes.recommendation_id AS id, LIKES.creation_date AS created,  ATTACH.OBJECT_ID, users.exid
FROM (SELECT item_id, entry_id FROM Homepage.BOARD_ENTRIES 
	WHERE category_type = 5 
		UNION
	SELECT bCom.item_id, bCom.entry_id FROM HOMEPAGE.BOARD_COMMENTS AS bCom
	JOIN HOMEPAGE.BOARD_ENTRIES AS parent ON bCom.entry_id = parent.entry_id
	WHERE parent.category_type = 5 ) AS socPComments
JOIN HOMEPAGE.BOARD_OBJECT_REFERENCE AS ATTACH ON ATTACH.ITEM_ID = socPComments.entry_id
JOIN HOMEPAGE.BOARD_RECOMMENDATIONS AS likes ON likes.item_id = socPComments.item_id
JOIN HOMEPAGE.PERSON AS users ON (users.person_id = likes.recommender_id) 
"""


#Einlesen der Daten aus den SQL Queries in die Dataframes
dfMicroblogPost = pd.read_sql(sqlMicroblogPost, connhomepage)
dfMicroblog = pd.read_sql(sqlMicroblog, connhomepage)
dfMicroblogPostComment= pd.read_sql(sqlMicroblogPostComment, connhomepage)
dfMicroblogPostAttachment = pd.read_sql(sqlMicroblogPostAttachment, connhomepage)
dfMicroblogPostLike = pd.read_sql(sqlMicroblogPostLike, connhomepage)
dfMicroblogPostCommentLike = pd.read_sql(sqlMicroblogPostCommentLike, connhomepage)
dfSocialProfile = pd.read_sql(sqlSocialProfile, connhomepage)
dfSocialProfileFollow = pd.read_sql(sqlSocialProfileFollow, connhomepage)
dfSocialProfileComment = pd.read_sql(sqlSocialProfileComment, connhomepage)
dfSocialProfileCommentLike = pd.read_sql(sqlSocialProfileCommentLike, connhomepage)
dfSocialProfileCommentAttachment = pd.read_sql(sqlSocialProfileCommentAttachment, connhomepage)
dfSocialProfileCommentAttachmentLike = pd.read_sql(sqlSocialProfileCommentAttachmentLike, connhomepage)


#Datacleaning MicroblogPost
#Content
dfMicroblogPost['CONTENT'] = dfMicroblogPost['CONTENT'].fillna('NaN')
#print(dfMicroblogPost['CONTENT'])
dfMicroblogPost['CONTENT'] = dfMicroblogPost['CONTENT'].str.replace('\n', '')
dfMicroblogPost['CONTENT'] = dfMicroblogPost['CONTENT'].str.replace('\t', '')
dfMicroblogPost['CONTENT'] = dfMicroblogPost['CONTENT'].str.replace('\r', '')
dfMicroblogPost['CONTENT'] = dfMicroblogPost['CONTENT'].str.replace('\v', '')
dfMicroblogPost['CONTENT'] = dfMicroblogPost['CONTENT'].str.replace(';', ',')
dfMicroblogPost['CONTENT'] = dfMicroblogPost[['CONTENT']].applymap(lambda text: BeautifulSoup(text, 'html.parser').get_text())
#print(dfMicroblogPost['CONTENT'])
#Timestamp
#print(dfMicroblogPost['CREATED'])
dfMicroblogPost['CREATED'] = pd.to_datetime(dfMicroblogPost['CREATED'])
# Zeitzone setzen
dfMicroblogPost['CREATED'] = dfMicroblogPost['CREATED'].dt.tz_localize('CET')
#print(dfMicroblogPost['CREATED'])
#print(dfMicroblogPost['LAST_UPDATED'])
dfMicroblogPost['LAST_UPDATED'] = pd.to_datetime(dfMicroblogPost['LAST_UPDATED'])
# Zeitzone setzen
dfMicroblogPost['LAST_UPDATED'] = dfMicroblogPost['LAST_UPDATED'].dt.tz_localize('CET')
#print(dfMicroblogPost['LAST_UPDATED'])

#Datacleaning MicroblogPostComment
#Content
dfMicroblogPostComment['CONTENT'] = dfMicroblogPostComment['CONTENT'].fillna('NaN')
#print(dfMicroblogPostComment['CONTENT'])
dfMicroblogPostComment['CONTENT'] = dfMicroblogPostComment['CONTENT'].str.replace('\n', '')
dfMicroblogPostComment['CONTENT'] = dfMicroblogPostComment['CONTENT'].str.replace('\t', '')
dfMicroblogPostComment['CONTENT'] = dfMicroblogPostComment['CONTENT'].str.replace('\r', '')
dfMicroblogPostComment['CONTENT'] = dfMicroblogPostComment['CONTENT'].str.replace('\v', '')
dfMicroblogPostComment['CONTENT'] = dfMicroblogPostComment['CONTENT'].str.replace(';', ',')
dfMicroblogPostComment['CONTENT'] = dfMicroblogPostComment[['CONTENT']].applymap(lambda text: BeautifulSoup(text, 'html.parser').get_text())
#print(dfMicroblogPostComment['CONTENT'])
#Timestamp
#print(dfMicroblogPostComment['CREATED'])
dfMicroblogPostComment['CREATED'] = pd.to_datetime(dfMicroblogPostComment['CREATED'])
# Zeitzone setzen
dfMicroblogPostComment['CREATED'] = dfMicroblogPostComment['CREATED'].dt.tz_localize('CET')
#print(dfMicroblogPostComment['CREATED'])
#print(dfMicroblogPostComment['LAST_UPDATED'])
dfMicroblogPostComment['LAST_UPDATED'] = pd.to_datetime(dfMicroblogPostComment['LAST_UPDATED'])
# Zeitzone setzen
dfMicroblogPostComment['LAST_UPDATED'] = dfMicroblogPostComment['LAST_UPDATED'].dt.tz_localize('CET')
#print(dfMicroblogPostComment['LAST_UPDATED'])

#Data Cleaining MicroblogPostAttachment
#Timestamp
#print(dfMicroblogPostAttachment['CREATED'])
dfMicroblogPostAttachment['CREATED'] = pd.to_datetime(dfMicroblogPostAttachment['CREATED'])
# Zeitzone setzen
dfMicroblogPostAttachment['CREATED'] = dfMicroblogPostAttachment['CREATED'].dt.tz_localize('CET')
#print(dfMicroblogPostAttachment['CREATED'])

#Data Cleaining MicroblogPostLike
#Timestamp
#print(dfMicroblogPostLike['CREATED'])
dfMicroblogPostLike['CREATED'] = pd.to_datetime(dfMicroblogPostLike['CREATED'])
# Zeitzone setzen
dfMicroblogPostLike['CREATED'] = dfMicroblogPostLike['CREATED'].dt.tz_localize('CET')
#print(dfMicroblogPostLike['CREATED'])

#Data Cleaining MicroblogPostCommentLike
#Timestamp
#print(dfMicroblogPostCommentLike['CREATED'])
dfMicroblogPostCommentLike['CREATED'] = pd.to_datetime(dfMicroblogPostCommentLike['CREATED'])
# Zeitzone setzen
dfMicroblogPostCommentLike['CREATED'] = dfMicroblogPostCommentLike['CREATED'].dt.tz_localize('CET')
#print(dfMicroblogPostCommentLike['CREATED'])

#Data Cleaning SocialProfile
#Timestamp
#print(dfSocialProfile['CREATED'])
dfSocialProfile['CREATED'] = pd.to_datetime(dfSocialProfile['CREATED'])
# Zeitzone setzen
dfSocialProfile['CREATED'] = dfSocialProfile['CREATED'].dt.tz_localize('CET')
#print(dfSocialProfile['CREATED'])
#print(dfSocialProfile['LAST_UPDATED'])
dfSocialProfile['LAST_UPDATED'] = pd.to_datetime(dfSocialProfile['LAST_UPDATED'])
# Zeitzone setzen
dfSocialProfile['LAST_UPDATED'] = dfSocialProfile['LAST_UPDATED'].dt.tz_localize('CET')
#print(dfSocialProfile['LAST_UPDATED'])

#Datacleaning fSocialProfileComment
#Content
dfSocialProfileComment['CONTENT'] = dfSocialProfileComment['CONTENT'].fillna('NaN')
#print(dfSocialProfileComment['CONTENT'])
dfSocialProfileComment['CONTENT'] = dfSocialProfileComment['CONTENT'].str.replace('\n', '')
dfSocialProfileComment['CONTENT'] = dfSocialProfileComment['CONTENT'].str.replace('\t', '')
dfSocialProfileComment['CONTENT'] = dfSocialProfileComment['CONTENT'].str.replace('\r', '')
dfSocialProfileComment['CONTENT'] = dfSocialProfileComment['CONTENT'].str.replace('\v', '')
dfSocialProfileComment['CONTENT'] = dfSocialProfileComment['CONTENT'].str.replace(';', ',')
dfSocialProfileComment['CONTENT'] = dfSocialProfileComment[['CONTENT']].applymap(lambda text: BeautifulSoup(text, 'html.parser').get_text())
#print(dfSocialProfileComment['CONTENT'])
#Timestamp
#print(dfSocialProfileComment['CREATED'])
dfSocialProfileComment['CREATED'] = pd.to_datetime(dfSocialProfileComment['CREATED'])
# Zeitzone setzen
dfSocialProfileComment['CREATED'] = dfSocialProfileComment['CREATED'].dt.tz_localize('CET')
#print(dfSocialProfileComment['CREATED'])
#print(dfSocialProfileComment['LAST_UPDATED'])
dfSocialProfileComment['LAST_UPDATED'] = pd.to_datetime(dfSocialProfileComment['LAST_UPDATED'])
# Zeitzone setzen
dfSocialProfileComment['LAST_UPDATED'] = dfSocialProfileComment['LAST_UPDATED'].dt.tz_localize('CET')
#print(dfSocialProfileComment['LAST_UPDATED'])

#DataCleaing SocialProfileCommentLike
#Timestamp
#print(dfSocialProfileCommentLike['CREATED'])
dfSocialProfileCommentLike['CREATED'] = pd.to_datetime(dfSocialProfileCommentLike['CREATED'])
# Zeitzone setzen
dfSocialProfileCommentLike['CREATED'] = dfSocialProfileCommentLike['CREATED'].dt.tz_localize('CET')
#print(dfSocialProfileCommentLike['CREATED'])

#DataCleaing SocialProfileCommentAttachment
#Timestamp
#print(dfSocialProfileCommentAttachment['CREATED'])
dfSocialProfileCommentAttachment['CREATED'] = pd.to_datetime(dfSocialProfileCommentAttachment['CREATED'])
# Zeitzone setzen
dfSocialProfileCommentAttachment['CREATED'] = dfSocialProfileCommentAttachment['CREATED'].dt.tz_localize('CET')
#print(dfSocialProfileCommentAttachment['CREATED'])

#DataCleaing SocialProfileCommentAttachmentLike
#Timestamp
#print(dfSocialProfileCommentAttachmentLike['CREATED'])
dfSocialProfileCommentAttachmentLike['CREATED'] = pd.to_datetime(dfSocialProfileCommentAttachmentLike['CREATED'])
# Zeitzone setzen
dfSocialProfileCommentAttachmentLike['CREATED'] = dfSocialProfileCommentAttachmentLike['CREATED'].dt.tz_localize('CET')
#print(dfSocialProfileCommentAttachmentLike['CREATED'])

#Verbindung zu Neo4j
neodb = neointerface.NeoInterface(host="neo4j://ma-lschloemer.bas.uni-koblenz.de:7687" , credentials=("neo4j", "neo4jneo4j"))

#Importieren der Daten in den einzelnen Dataframes in Neo4j
#(Name Dataframe, Name Label, Aktivieren der Mergefunktion statt Create)
neodb.load_df(dfMicroblog, "Microblog", merge=True)
neodb.load_df(dfMicroblogPost, "MicroblogPost", merge=True)
neodb.load_df(dfMicroblogPostComment, "Comment", merge=True)
neodb.load_df(dfMicroblogPostAttachment, "Attachment", merge=True)
neodb.load_df(dfMicroblogPostLike, "Like", merge=True)
neodb.load_df(dfMicroblogPostCommentLike, "Like", merge=True)
neodb.load_df(dfSocialProfile, "SocialProfile", merge=True)
neodb.load_df(dfSocialProfileFollow, "Follow", merge=True)
neodb.load_df(dfSocialProfileComment, "Comment", merge=True)
neodb.load_df(dfSocialProfileCommentLike, "Like", merge=True)
neodb.load_df(dfSocialProfileCommentAttachment, "Attachment", merge=True)
neodb.load_df(dfSocialProfileCommentAttachmentLike, "Like", merge=True)
