#Skript um alle Nodes aus der Wiki Datenbank zu laden
#Verbindung zur DB2
from ibm_db import connect
import ibm_db_dbi
#Dataframe 
import pandas as pd
#Library für Bereinigung von HTML Code im Content
from bs4 import BeautifulSoup
#Library für Neo4j
import neointerface
#Library für Umwandlung in UUIDs
import uuid
#Library für Timestamp Konvertierung
from datetime import datetime, timezone, timedelta
#Extralibraries wegen besonderer Timestamps von WikiPage
import pytz
from dateutil import tz

#Verbindung zur Wikis Datenbank

cnxnfiles = connect('DATABASE=wikis;'
                 'HOSTNAME=db2.uniconnect.de;'  # localhost would work 
                 'PORT=50000;'
                 'PROTOCOL=TCPIP;'
                 'UID=reader19;'
                 'PWD=b2BwaRHN;', '', '')

connfiles = ibm_db_dbi.Connection(cnxnfiles)

#SQL Queries

sqlWiki = """SELECT lib.id, lib.title, lib.EXTERNAL_CONTAINER_ID
FROM WIKIS.LIBRARY lib
"""

sqlWikiPage = """SELECT mr.ID AS id ,mr.CREATE_DATE AS created, mr.LAST_UPDATE AS last_updated, m.SUMMARY AS content, 
m.TITLE AS title, m.DOWNLOAD_CNT AS views, mr.MEDIA_ID, USER.directory_id, 
REPLACE(mr.media_id, ' ', '') AS match_media_id, previous.sub_id, previous.previous_id, m.CURRENT_REVISION_ID 
FROM WIKIS.MEDIA m 
JOIN WIKIS.MEDIA_REVISION mr ON m.id = mr.MEDIA_ID 
JOIN WIKIS.USER AS USER ON USER.id = m.OWNER_USER_ID 
JOIN (
SELECT subselect.id AS sub_id, cofiMR.id AS previous_id
                FROM (SELECT id, media_id, (SELECT MAX(revision_number)
                                            FROM WIKIS.MEDIA_REVISION AS sub
                                            WHERE sub.media_id = main.media_id AND sub.revision_number < main.revision_number
                                            ) AS previous_revision_number
                      FROM WIKIS.media_revision AS main) AS subselect
                  JOIN WIKIS.media_revision AS cofiMR ON cofiMR.media_id = subselect.media_id AND revision_number = previous_revision_number
                  )AS previous ON previous.sub_id = mr.ID

"""

sqlAttachmentWikiPage = """SELECT DISTINCT  wikiArt.id AS id, wikiArt.title AS title, wikiArt.create_date AS created, 
wikiArt.last_update AS last_updated,  users.directory_id, wikiArticles.media_id, REPLACE(WIKIART.id, ' ', '') AS match_id
FROM wikis.MEDIA_ADDITIONAL_FILE AS wikiArt
LEFT JOIN wikis.MEDIA_REVISION AS wikiArticles ON wikiArticles.media_id = wikiArt.media_id
LEFT JOIN wikis.USER AS users ON (users.id = wikiArt.last_update_user_id)  
"""

sqlCommentWikiPage = """ SELECT wikiComs.COMMENT AS content, wikiComs.create_date AS created, wikiComs.id AS id, 
wikiComs.last_update AS last_updated, wikiComs.title AS title, users.DIRECTORY_ID, WIKICOMS.MEDIA_ID, 
REPLACE(WIKICOMS.id, ' ', '') AS match_com_id
FROM WIKIS.MEDIA_COMMENT AS wikiComs
JOIN WIKIS."USER" AS users ON (users.id = wikiComs.owner_user_id)
"""

sqlFollowWikiPage = """SELECT CONCAT(wikiarticles.ID , CONCAT(' - ',follows.user_id)) AS id, follows.create_date AS created, 
users.DIRECTORY_ID, WIKIARTICLES.id AS wiki_id, REPLACE(WIKIARTICLES.media_id, ' ', '') AS match_media_id
FROM wikis.LIBRARY_NOTIFICATION AS follows
JOIN WIKIS.MEDIA_REVISION AS wikiarticles ON follows.library_id = wikiarticles.library_id
JOIN WIKIS.USER AS users ON (users.id = follows.user_id)
"""

sqlLikeWikiPage= """ SELECT CONCAT(WIKIPAGE.id, CONCAT(' - ', likes.user_id)) AS id, likes.create_date AS created, 
wikiPage.id AS wiki_id, users.directory_id 
FROM WIKIS.MEDIA_RECOMMEND AS likes
JOIN WIKIS.MEDIA_REVISION AS wikiPage ON wikiPage.media_id = likes.media_id
JOIN Wikis.USER AS users ON (users.id = likes.user_id)
LIMIT 10"""


#Einlesen der Daten aus den SQL Queries in die Dataframes
dfWiki = pd.read_sql(sqlWiki, connfiles)
dfWikiPage = pd.read_sql(sqlWikiPage, connfiles)
dfAttachmentWikiPage = pd.read_sql(sqlAttachmentWikiPage, connfiles)
dfCommentWikiPage = pd.read_sql(sqlCommentWikiPage, connfiles)
dfFollowWikiPage = pd.read_sql(sqlFollowWikiPage, connfiles)
dfLikeWikiPage = pd.read_sql(sqlLikeWikiPage, connfiles)

# Funktion zum ID cleaning/konvertieren
def binary_to_uuidleng(binary_data):
    #Filtern nach bestehnden NaN Werten
    if binary_data == 'NaN':
        return 'NaN'
    #Filtern und auf NaN setzen falls ID unter 16 ist, wegen einzelnen defekten IDs
    elif len(binary_data) < 16:
        return 'NaN'
    #Fall von zusammengesetzen ConCat IDs, die länger sind 
    if len(binary_data) > 16:
        # b vor dem Bindestrich wichitg wegen Dateityp
        seperator = b' - '
        #slice methode zum trennen der 2 IDs
        uuid1, uuid2 = split_bytes_at_separator(binary_data, seperator)
        #print(uuid1)
        #print(uuid2)
        #Konvertierung der beiden Einzelteile 
        if len(uuid1) != 16 or len(uuid2) != 16 :
            return 'NaN'
        else:
            part1 = uuid.UUID(bytes=bytes(uuid1))
            part2 = uuid.UUID(bytes=bytes(uuid2))
            #print(part1)
            #Umwandlung in String für Kombinierung der beiden Teil IDs
            part1 = str(part1)
            part2 = str(part2)
            #Kombinierung der beiden Teil IDs
            uuid_object = part1 + '-' + part2
            #print(uuid_object)
            return uuid_object
    #Normale ID Konvertierung falls normale ID
    else:
        uuid_object = uuid.UUID(bytes=bytes(binary_data))
        return str(uuid_object)
    
#Methode um das die kombinierte ID in 2 Teil IDs aufzuspliten
def split_bytes_at_separator(byte_data, separator):
    index = byte_data.find(separator)
    if index != -1:
        part1 = byte_data[:index]
        part2 = byte_data[index + len(separator):]
        return part1, part2
    else:
        return byte_data, b''



#Cleaning IDs Wiki
#print(dfWiki['ID'])
#print(dfWiki['EXTERNAL_CONTAINER_ID'])
dfWiki['ID'] = dfWiki['ID'].apply(binary_to_uuidleng)
#print(dfWiki['ID'])

#Cleaning IDs WikiPage
#IDs berichtigen
#print(dfWikiPage['ID']) #need cleaning
#print(dfWikiPage['MEDIA_ID']) #need cleaning
#print(dfWikiPage['DIRECTORY_ID']) #fine
#print(dfWikiPage['MATCH_MEDIA_ID']) #need cleaning
#print(dfWikiPage['SUB_ID']) #need cleaning
#print(dfWikiPage['PREVIOUS_ID']) #need cleaning
#print(dfWikiPage['CURRENT_REVISION_ID']) #need cleaning
dfWikiPage['CONTENT'] = dfWikiPage['CONTENT'].fillna('NaN')
dfWikiPage['CREATED'] = dfWikiPage['CREATED'].fillna('NaT') # unnötig
dfWikiPage['ID'] = dfWikiPage['ID'].apply(binary_to_uuidleng)
dfWikiPage['MEDIA_ID'] = dfWikiPage['MEDIA_ID'].apply(binary_to_uuidleng)
dfWikiPage['MATCH_MEDIA_ID'] = dfWikiPage['MATCH_MEDIA_ID'].apply(binary_to_uuidleng)
dfWikiPage['SUB_ID'] = dfWikiPage['SUB_ID'].apply(binary_to_uuidleng)
dfWikiPage['PREVIOUS_ID'] = dfWikiPage['PREVIOUS_ID'].apply(binary_to_uuidleng)
dfWikiPage['CURRENT_REVISION_ID'] = dfWikiPage['CURRENT_REVISION_ID'].apply(binary_to_uuidleng)
#print(dfWikiPage['ID'])
#print(dfWikiPage['MEDIA_ID']) #need cleaning
#print(dfWikiPage['MATCH_MEDIA_ID']) #need cleaning
#print(dfWikiPage['SUB_ID']) #need cleaning
#print(dfWikiPage['PREVIOUS_ID']) #need cleaning
#print(dfWikiPage['CURRENT_REVISION_ID']) #need cleaning
#Content
#print(dfWikiPage['CONTENT'])
dfWikiPage['CONTENT'] = dfWikiPage['CONTENT'].str.replace('\n', '')
dfWikiPage['CONTENT'] = dfWikiPage['CONTENT'].str.replace('\t', '')
dfWikiPage['CONTENT'] = dfWikiPage['CONTENT'].str.replace('\r', '')
dfWikiPage['CONTENT'] = dfWikiPage['CONTENT'].str.replace('\v', '')
dfWikiPage['CONTENT'] = dfWikiPage['CONTENT'].str.replace(';', ',')
dfWikiPage['CONTENT'] = dfWikiPage[['CONTENT']].applymap(lambda text: BeautifulSoup(text, 'html.parser').get_text())
#print(dfWikiPage['CONTENT'])
##Timestamp # Wegen Problemen mit der Timestamp Methode musste eine abweichende Methode verwendet werden
#print(dfWikiPage['CREATED'])
# Zeitzone setzen
dfWikiPage['CREATED'] = pd.to_datetime(dfWikiPage['CREATED'])
#Abweichend wegen besonderem Timestamp
dfWikiPage['CREATED'] = dfWikiPage['CREATED'].dt.tz_localize(tz.tzlocal())
#print(dfWikiPage['CREATED'])
#print(dfWikiPage['LAST_UPDATED'])
#Abweichend wegen besonderem Timestamp
dfWikiPage['LAST_UPDATED'] = pd.to_datetime(dfWikiPage['LAST_UPDATED'])
dfWikiPage['LAST_UPDATED'] = dfWikiPage['LAST_UPDATED'].dt.tz_localize(tz.tzlocal())
#print(dfWikiPage['LAST_UPDATED'])
#print(dfWikiPage)



#Cleaning IDs AttachmentWikiPage
#print(dfAttachmentWikiPage['ID'])  #need cleaning
#print(dfAttachmentWikiPage['DIRECTORY_ID']) #fine
#print(dfAttachmentWikiPage['MEDIA_ID'])  #need cleaning
#print(dfAttachmentWikiPage['MATCH_ID']) #need cleaning
dfAttachmentWikiPage['ID'] = dfAttachmentWikiPage['ID'].fillna('NaN')
dfAttachmentWikiPage['ID'] = dfAttachmentWikiPage['ID'].apply(binary_to_uuidleng)
dfAttachmentWikiPage['MEDIA_ID'] = dfAttachmentWikiPage['MEDIA_ID'].apply(binary_to_uuidleng)
dfAttachmentWikiPage['MATCH_ID'] = dfAttachmentWikiPage['MATCH_ID'].apply(binary_to_uuidleng)
#print(dfAttachmentWikiPage['ID'])  #need cleaning
#print(dfAttachmentWikiPage['MEDIA_ID'])  #need cleaning
#print(dfAttachmentWikiPage['MATCH_ID']) #need cleaning
#Timestamp
#print(dfAttachmentWikiPage['CREATED'])
dfAttachmentWikiPage['CREATED'] = pd.to_datetime(dfAttachmentWikiPage['CREATED'])
# Zeitzone setzen
dfAttachmentWikiPage['CREATED'] = dfAttachmentWikiPage['CREATED'].dt.tz_localize('CET')
#print(dfAttachmentWikiPage['CREATED'])
#print(dfAttachmentWikiPage['LAST_UPDATED'])
dfAttachmentWikiPage['LAST_UPDATED'] = pd.to_datetime(dfAttachmentWikiPage['LAST_UPDATED'])
# Zeitzone setzen
dfAttachmentWikiPage['LAST_UPDATED'] = dfAttachmentWikiPage['LAST_UPDATED'].dt.tz_localize('CET')
#print(dfAttachmentWikiPage['LAST_UPDATED'])
#print(dfAttachmentWikiPage)


#Cleaning IDs CommentWikiPage
#print(dfCommentWikiPage['ID']) #need cleaning
#print(dfCommentWikiPage['DIRECTORY_ID']) #fine
#print(dfCommentWikiPage['MEDIA_ID']) #need cleaning
#print(dfCommentWikiPage['MATCH_COM_ID']) #need cleaning
dfCommentWikiPage['CONTENT'] = dfCommentWikiPage['CONTENT'].fillna('NaN')
dfCommentWikiPage['ID'] = dfCommentWikiPage['ID'].apply(binary_to_uuidleng)
dfCommentWikiPage['MEDIA_ID'] = dfCommentWikiPage['MEDIA_ID'].apply(binary_to_uuidleng)
dfCommentWikiPage['MATCH_COM_ID'] = dfCommentWikiPage['MATCH_COM_ID'].apply(binary_to_uuidleng)
#print(dfCommentWikiPage['ID']) #need cleaning
#print(dfCommentWikiPage['MEDIA_ID']) #need cleaning
#print(dfCommentWikiPage['MATCH_COM_ID']) #need cleaning
#Content
#print(dfCommentWikiPage['CONTENT'])
dfCommentWikiPage['CONTENT'] = dfCommentWikiPage['CONTENT'].str.replace('\n', '')
dfCommentWikiPage['CONTENT'] = dfCommentWikiPage['CONTENT'].str.replace('\t', '')
dfCommentWikiPage['CONTENT'] = dfCommentWikiPage['CONTENT'].str.replace('\r', '')
dfCommentWikiPage['CONTENT'] = dfCommentWikiPage['CONTENT'].str.replace('\v', '')
dfCommentWikiPage['CONTENT'] = dfCommentWikiPage['CONTENT'].str.replace(';', ',')
dfCommentWikiPage['CONTENT'] = dfCommentWikiPage[['CONTENT']].applymap(lambda text: BeautifulSoup(text, 'html.parser').get_text())
#print(dfCommentWikiPage['CONTENT'])
#Timestamp
#print(dfCommentWikiPage['CREATED'])
dfCommentWikiPage['CREATED'] = pd.to_datetime(dfCommentWikiPage['CREATED'])
# Zeitzone setzen
dfCommentWikiPage['CREATED'] = dfCommentWikiPage['CREATED'].dt.tz_localize('CET')
#print(dfCommentWikiPage['CREATED'])
#print(dfCommentWikiPage['LAST_UPDATED'])
dfCommentWikiPage['LAST_UPDATED'] = pd.to_datetime(dfCommentWikiPage['LAST_UPDATED'])
# Zeitzone setzen
dfCommentWikiPage['LAST_UPDATED'] = dfCommentWikiPage['LAST_UPDATED'].dt.tz_localize('CET')
#print(dfCommentWikiPage['LAST_UPDATED'])
#print(dfCommentWikiPage)

#Cleaing IDs FollowWikiPage
#print(dfFollowWikiPage['ID']) #need cleaning
#print(dfFollowWikiPage['DIRECTORY_ID']) #need cleaning
#print(dfFollowWikiPage['WIKI_ID']) #need cleaning
#print(dfFollowWikiPage['MATCH_MEDIA_ID']) #need cleaning
dfFollowWikiPage['ID'] = dfFollowWikiPage['ID'].apply(binary_to_uuidleng)
dfFollowWikiPage['WIKI_ID'] = dfFollowWikiPage['WIKI_ID'].apply(binary_to_uuidleng)
dfFollowWikiPage['MATCH_MEDIA_ID'] = dfFollowWikiPage['MATCH_MEDIA_ID'].apply(binary_to_uuidleng)
#print(dfFollowWikiPage['ID']) #need cleaning
#print(dfFollowWikiPage['WIKI_ID']) #need cleaning
#print(dfFollowWikiPage['MATCH_MEDIA_ID']) #need cleaning
#Timestamp
#print(dfFollowWikiPage['CREATED'])
dfFollowWikiPage['CREATED'] = pd.to_datetime(dfFollowWikiPage['CREATED'])
# Zeitzone setzen
dfFollowWikiPage['CREATED'] = dfFollowWikiPage['CREATED'].dt.tz_localize('CET')
#print(dfFollowWikiPage['CREATED'])
#print(dfFollowWikiPage)

#Cleaning IDs LikeWikiPage
#print(dfLikeWikiPage['ID']) # needs cleaing
#print(dfLikeWikiPage['WIKI_ID']) # need cleaning
#print(dfLikeWikiPage['DIRECTORY_ID']) # fine
dfLikeWikiPage['ID'] = dfLikeWikiPage['ID'].apply(binary_to_uuidleng)
dfLikeWikiPage['WIKI_ID'] = dfLikeWikiPage['WIKI_ID'].apply(binary_to_uuidleng)
#print(dfLikeWikiPage['ID'])
#print(dfLikeWikiPage['WIKI_ID'])
#Timestamp
#print(dfLikeWikiPage['CREATED'])
dfLikeWikiPage['CREATED'] = pd.to_datetime(dfLikeWikiPage['CREATED'])
# Zeitzone setzen
dfLikeWikiPage['CREATED'] = dfLikeWikiPage['CREATED'].dt.tz_localize('CET')
#print(dfLikeWikiPage['CREATED'])
#print(dfLikeWikiPage)

#Verbindung zu Neo4j
neodb = neointerface.NeoInterface(host="neo4j://ma-lschloemer.bas.uni-koblenz.de:7687" , credentials=("neo4j", "neo4jneo4j"))

#Importieren der Daten aus den Dataframes in Neo4j
#(Name Dataframe, Name Label, Aktivieren der Mergefunktion statt Create)
neodb.load_df(dfWiki, "Wiki", merge=True)
neodb.load_df(dfWikiPage, "WikiPage", merge=True)
neodb.load_df(dfAttachmentWikiPage, "Attachment", merge=True)
neodb.load_df(dfCommentWikiPage, "Comment", merge=True)
neodb.load_df(dfFollowWikiPage, "Follow", merge=True)
