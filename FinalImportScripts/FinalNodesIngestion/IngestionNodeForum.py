#Skript zum Import der Daten aus der Forum Datenbank
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

#Verbindung zur UniConnect Datenbank forum

cnxnforum = connect('DATABASE=forum;'
                 'HOSTNAME=db2.uniconnect.de;'  # localhost would work 
                 'PORT=50000;'
                 'PROTOCOL=TCPIP;'
                 'UID=reader19;'
                 'PWD=b2BwaRHN;', '', '')

connforum = ibm_db_dbi.Connection(cnxnforum)

#SQL Queries

sqlBoardPost = """SELECT BOARDPOST.NODEUUID AS id, BOARDPOST.DESCRIPTION AS content, BOARDPOST.CREATED AS created, 
BOARDPOST.NAME AS title, BOARDPOST.LASTMOD AS last_updated, 
BOARDPOST.FORUMUUID AS forumuuid, MEMBERPROFILE.EXID, BOARDPOST.TOPICID 
FROM FORUM.DF_NODE AS BoardPost JOIN FORUM.DF_MEMBERPROFILE AS Memberprofile ON BOARDPOST.CREATEDBY = MEMBERPROFILE.MEMBERID 
WHERE BOARDPOST.NODETYPE = 'forum/topic'
"""

sqlBoardPostAttachment = """SELECT BPOST.nodeuuid AS id, BPOST.FIELDNAME AS title, ATTACHMENT.content AS content,
 BPOST.CREATED AS created, BPOST.LASTMOD AS last_updated, PROFILE.exid
FROM (SELECT crefuuid, CASE WHEN Forum.DF_CONTENTREF.MIMETYPE = 'text/html' THEN forum.DF_CONTENTREF.DESCOFLOW ELSE forum.DF_CONTENTREF.CURI || '/' || 
forum.DF_CONTENTREF.FILENAME END AS content FROM FORUM.DF_CONTENTREF) AS attachment 
JOIN FORUM.DF_NODE AS BPOST ON attachment.CREFUUID  = BPOST.CCREFUUID  
JOIN FORUM.df_memberprofile AS profile ON PROFILE.memberid = BPOST.createdby
WHERE BPOST.NODETYPE = 'application/field'
"""

sqlBoardPostComment = """SELECT boardP.nodeuuid AS id, boardP.created AS created, boardP.description AS content, boardP.lastmod AS last_updated, boardP.name AS title, USERS.exid
FROM forum.df_node AS boardP
JOIN forum.df_memberprofile AS users ON (users.memberid = boardP.createdby)
WHERE nodetype = 'forum/reply'
"""

sqlBoardPostCommentLike= """ SELECT likes.created AS created, likes.uuid AS id, likes.nodeid, USERS.exid
FROM FORUM.DF_NODE AS boardP
JOIN FORUM.DF_RECOMMENDATION AS likes ON boardP.nodeuuid = likes.nodeid
JOIN FORUM.DF_MEMBERPROFILE AS users ON (users.memberid = likes.createdby)
WHERE boardP.nodetype = 'forum/reply' 
"""

sqlBoardPostFollow = """SELECT boardPFollow.uuid AS id, boardPFollow.created AS created, USERS.exid, BOARDPFOLLOW.TOPICID 
FROM FORUM.DF_SUBSCRIPTION AS boardPFollow
JOIN FORUM.df_memberprofile AS users ON (users.memberid = boardPFollow.createdby) 
"""

sqlBoardPostLike = """SELECT likes.uuid AS id, likes.created AS created, likes.nodeid, USERS.EXID 
FROM FORUM.DF_NODE AS boardP
JOIN FORUM.DF_RECOMMENDATION AS likes ON boardP.nodeuuid = likes.nodeid
JOIN FORUM.DF_MEMBERPROFILE AS users ON (users.memberid = likes.createdby)
WHERE boardP.nodetype = 'forum/topic' 
"""

sqlBoardPostTag = """ SELECT tags.taguuid AS id, tags.created AS created, tags.name AS label, tags.nodeuuid, users.exid
FROM FORUM.DF_NODE AS boardposts
JOIN FORUM.DF_TAG AS tags ON boardposts.nodeuuid = tags.nodeuuid
JOIN FORUM.DF_MEMBERPROFILE AS users ON (users.memberid = tags.createdby)
WHERE boardposts.nodetype = 'forum/topic' 
"""

sqlMessageBoard = """SELECT MESSAGEBOARD.FORUMUUID AS id, MESSAGEBOARD.COMMUNITYUUID 
FROM FORUM.DF_NODECOMMMAP AS MessageBoard 
"""


#Einlesen der Daten aus den SQL Queries in die Dataframes
dfBoardPost = pd.read_sql(sqlBoardPost, connforum)
dfMessageBoard = pd.read_sql(sqlMessageBoard, connforum)
dfBoardPostAttachment= pd.read_sql(sqlBoardPostAttachment, connforum)
dfBoardPostComment = pd.read_sql(sqlBoardPostComment, connforum)
dfBoardPostCommentLike = pd.read_sql(sqlBoardPostCommentLike, connforum)
dfBoardPostFollow = pd.read_sql(sqlBoardPostFollow, connforum)
dfBoardPostLike = pd.read_sql(sqlBoardPostLike, connforum)
dfBoardPostTag = pd.read_sql(sqlBoardPostTag, connforum)


#Datacleaning BoardPost
#Content
dfBoardPost['CONTENT'] = dfBoardPost['CONTENT'].fillna('NaN')
#print(dfBoardPost['CONTENT'])
dfBoardPost['CONTENT'] = dfBoardPost['CONTENT'].str.replace('\n', '')
dfBoardPost['CONTENT'] = dfBoardPost['CONTENT'].str.replace('\t', '')
dfBoardPost['CONTENT'] = dfBoardPost['CONTENT'].str.replace('\r', '')
dfBoardPost['CONTENT'] = dfBoardPost['CONTENT'].str.replace('\v', '')
dfBoardPost['CONTENT'] = dfBoardPost['CONTENT'].str.replace(';', ',')
dfBoardPost['CONTENT'] = dfBoardPost[['CONTENT']].applymap(lambda text: BeautifulSoup(text, 'html.parser').get_text())
#print(dfBoardPost['CONTENT'])
#Timestamp
#print(dfBoardPost['CREATED'])
dfBoardPost['CREATED'] = pd.to_datetime(dfBoardPost['CREATED'])
# Zeitzone setzen
dfBoardPost['CREATED'] = dfBoardPost['CREATED'].dt.tz_localize('CET')
#print(dfBoardPost['CREATED'])
#print(dfBoardPost['LAST_UPDATED'])
dfBoardPost['LAST_UPDATED'] = pd.to_datetime(dfBoardPost['LAST_UPDATED'])
# Zeitzone setzen
dfBoardPost['LAST_UPDATED'] = dfBoardPost['LAST_UPDATED'].dt.tz_localize('CET')
#print(dfBoardPost['LAST_UPDATED'])

#Datacleaning BoardPostAttachment
#Content
dfBoardPostAttachment['CONTENT'] = dfBoardPostAttachment['CONTENT'].fillna('NaN')
#print(dfBoardPostAttachment['CONTENT'])
dfBoardPostAttachment['CONTENT'] = dfBoardPostAttachment['CONTENT'].str.replace('\n', '')
dfBoardPostAttachment['CONTENT'] = dfBoardPostAttachment['CONTENT'].str.replace('\t', '')
dfBoardPostAttachment['CONTENT'] = dfBoardPostAttachment['CONTENT'].str.replace('\r', '')
dfBoardPostAttachment['CONTENT'] = dfBoardPostAttachment['CONTENT'].str.replace('\v', '')
dfBoardPostAttachment['CONTENT'] = dfBoardPostAttachment['CONTENT'].str.replace(';', ',')
dfBoardPostAttachment['CONTENT'] = dfBoardPostAttachment[['CONTENT']].applymap(lambda text: BeautifulSoup(text, 'html.parser').get_text())
#print(dfBoardPostAttachment['CONTENT'])
#Timestamp
#print(dfBoardPostAttachment['CREATED'])
dfBoardPostAttachment['CREATED'] = pd.to_datetime(dfBoardPostAttachment['CREATED'])
# Zeitzone setzen
dfBoardPostAttachment['CREATED'] = dfBoardPostAttachment['CREATED'].dt.tz_localize('CET')
#print(dfBoardPostAttachment['CREATED'])
#print(dfBoardPostAttachment['LAST_UPDATED'])
dfBoardPostAttachment['LAST_UPDATED'] = pd.to_datetime(dfBoardPostAttachment['LAST_UPDATED'])
# Zeitzone setzen
dfBoardPostAttachment['LAST_UPDATED'] = dfBoardPostAttachment['LAST_UPDATED'].dt.tz_localize('CET')
#print(dfBoardPostAttachment['LAST_UPDATED'])

#Datacleaning BoardPostComment
#Content
dfBoardPostComment['CONTENT'] = dfBoardPostComment['CONTENT'].fillna('NaN')
#print(dfBoardPostComment['CONTENT'])
dfBoardPostComment['CONTENT'] = dfBoardPostComment['CONTENT'].str.replace('\n', '')
dfBoardPostComment['CONTENT'] = dfBoardPostComment['CONTENT'].str.replace('\t', '')
dfBoardPostComment['CONTENT'] = dfBoardPostComment['CONTENT'].str.replace('\r', '')
dfBoardPostComment['CONTENT'] = dfBoardPostComment['CONTENT'].str.replace('\v', '')
dfBoardPostComment['CONTENT'] = dfBoardPostComment['CONTENT'].str.replace(';', ',')
dfBoardPostComment['CONTENT'] = dfBoardPostComment[['CONTENT']].applymap(lambda text: BeautifulSoup(text, 'html.parser').get_text())
#print(dfBoardPostComment['CONTENT'])
#Timestamp
#print(dfBoardPostComment['CREATED'])
dfBoardPostComment['CREATED'] = pd.to_datetime(dfBoardPostComment['CREATED'])
# Zeitzone setzen
dfBoardPostComment['CREATED'] = dfBoardPostComment['CREATED'].dt.tz_localize('CET')
#print(dfBoardPostComment['CREATED'])
#print(dfBoardPostComment['LAST_UPDATED'])
dfBoardPostComment['LAST_UPDATED'] = pd.to_datetime(dfBoardPostComment['LAST_UPDATED'])
# Zeitzone setzen
dfBoardPostComment['LAST_UPDATED'] = dfBoardPostComment['LAST_UPDATED'].dt.tz_localize('CET')
#print(dfBoardPostComment['LAST_UPDATED'])

#Datacleaning BoardPostCommentLike
#Timestamp
#print(dfBoardPostCommentLike['CREATED'])
dfBoardPostCommentLike['CREATED'] = pd.to_datetime(dfBoardPostCommentLike['CREATED'])
# Zeitzone setzen
dfBoardPostCommentLike['CREATED'] = dfBoardPostCommentLike['CREATED'].dt.tz_localize('CET')
#print(dfBoardPostCommentLike['CREATED'])

#Datacleaning BoardPostFollow
#Timestamp
#print(dfBoardPostFollow['CREATED'])
dfBoardPostFollow['CREATED'] = pd.to_datetime(dfBoardPostFollow['CREATED'])
# Zeitzone setzen
dfBoardPostFollow['CREATED'] = dfBoardPostFollow['CREATED'].dt.tz_localize('CET')
#print(dfBoardPostFollow['CREATED'])

#Datacleaning BoardPostLike
#Timestamp
#print(dfBoardPostLike['CREATED'])
dfBoardPostLike['CREATED'] = pd.to_datetime(dfBoardPostLike['CREATED'])
# Zeitzone setzen
dfBoardPostLike['CREATED'] = dfBoardPostLike['CREATED'].dt.tz_localize('CET')
#print(dfBoardPostLike['CREATED'])

#Datacleaning BoardPostTag
#Timestamp
#print(dfBoardPostTag['CREATED'])
dfBoardPostTag['CREATED'] = pd.to_datetime(dfBoardPostTag['CREATED'])
# Zeitzone setzen
dfBoardPostTag['CREATED'] = dfBoardPostTag['CREATED'].dt.tz_localize('CET')
#print(dfBoardPostTag['CREATED'])

#Verbindung zu Neo4j
neodb = neointerface.NeoInterface(host="neo4j://ma-lschloemer.bas.uni-koblenz.de:7687" , credentials=("neo4j", "neo4jneo4j"))

#Import von Daten aus den Dataframes in Neo4j
#(Name Dataframe, Name Label, Aktivieren der Mergefunktion statt Create)
neodb.load_df(dfBoardPost, "BoardPost", merge=True)
neodb.load_df(dfMessageBoard, "MessageBoard", merge=True)
neodb.load_df(dfBoardPostComment, "Comment", merge=True)
neodb.load_df(dfBoardPostAttachment, "Attachment", merge=True)
neodb.load_df(dfBoardPostLike, "Like", merge=True)
neodb.load_df(dfBoardPostTag, "Tag", merge=True)
neodb.load_df(dfBoardPostCommentLike, "Like", merge=True)
neodb.load_df(dfBoardPostFollow, "Follow", merge=True)