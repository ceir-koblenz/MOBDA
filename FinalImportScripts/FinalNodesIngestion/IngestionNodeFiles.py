#Skript um alle Nodes aus der Files Datenbank zu laden
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


#Aufbau der Verbindung zur UniConnect Datenbank files
cnxnfiles = connect('DATABASE=files;'
                 'HOSTNAME=db2.uniconnect.de;'  # localhost would work 
                 'PORT=50000;'
                 'PROTOCOL=TCPIP;'
                 'UID=reader19;'
                 'PWD=b2BwaRHN;', '', '')

connfiles = ibm_db_dbi.Connection(cnxnfiles)

#SQL Queries

sqlFile = """SELECT  mr.ID AS id, mr.create_date AS created,  mr.LAST_UPDATE AS last_updated, mr.media_label AS title, 
mr.MEDIA_ID, USER.DIRECTORY_ID, m.CURRENT_REVISION_ID, REPLACE(mr.MEDIA_ID, ' ', '') AS match_media_id, previous.sub_id, 
previous.previousid
FROM FILES.MEDIA_REVISION mr
JOIN FILES.MEDIA m ON mr.MEDIA_ID = m.ID 
JOIN FILES.USER USER ON USER.ID = m.OWNER_USER_ID 
JOIN (
SELECT subselect.id AS sub_id, cofiMR.id AS previousid
                FROM (SELECT id, media_id, (SELECT MAX(revision_number)
                                            FROM FILES.MEDIA_REVISION AS sub
                                            WHERE sub.media_id = main.media_id AND sub.revision_number < main.revision_number
                                            ) AS previous_revision_number
                      FROM FILES.media_revision AS main) AS subselect
                  JOIN FILES.media_revision AS cofiMR ON cofiMR.media_id = subselect.media_id AND revision_number = previous_revision_number
                  )AS previous ON previous.sub_id = mr.id 
"""

sqlFileLibrary = """SELECT c.ID  AS id, c.TITLE AS title, c.EXTERNAL_CONTAINER_ID 
FROM files.COLLECTION c 
WHERE c.owner_user_id LIKE X'00000000000000000000000000000000'
 """

sqlFolder = """SELECT c.ID AS id, c.CREATE_DATE  AS created, c.last_update AS last_updated, c.TITLE  AS title, 
REPLACE(c.ID , ' ', '') AS match_folder_id
FROM files.COLLECTION c   
"""

sqlFileComment = """ SELECT fileComs.id AS id, fileComs.COMMENT AS content, fileComs.create_date AS created,  
fileComs.last_update AS last_updated, fileComs.title AS title, USERS.DIRECTORY_ID, FILECOMS.MEDIA_ID,  
REPLACE(FILECOMS.ID, ' ', '') AS match_comment_id
FROM files.MEDIA_COMMENT AS fileComs
JOIN files."USER" AS users ON (users.id = fileComs.owner_user_id)
"""

sqlFileFollow = """SELECT CONCAT(fileFollow.media_id, CONCAT(' - ', fileFollow.user_id)) AS id, fileFollow.create_date AS created, users.directory_id,  REPLACE(FILEFOLLOW.MEDIA_ID, ' ', '') AS match_media_id
FROM FILES.MEDIA_NOTIFICATION AS fileFollow
JOIN FILES.USER AS users ON (users.id = fileFollow.user_id)
"""

sqlFileLike="""SELECT CONCAT(FILES.ID , CONCAT( ' - ', likes.user_id)) AS id, likes.create_date AS created, 
users.directory_id, files.id AS file_id, REPLACE(LIKES.MEDIA_ID, ' ', '') AS match_media_id
FROM FILES.MEDIA_RECOMMEND AS likes
JOIN FILES.MEDIA_REVISION AS files ON likes.media_id = files.media_id
JOIN FILES.USER AS users ON (users.id = likes.user_id) 
"""

sqlMicrblogPostAttachmentLike = """SELECT CONCAT(likes.media_id, CONCAT(' - ', likes.user_id)) AS id, likes.create_date AS created, 
users.directory_id, REPLACE(likes.media_id, ' ', '')AS match_media_id
FROM FILES.MEDIA_RECOMMEND AS likes
JOIN FILES.USER  AS users ON (users.id = likes.user_id) 
"""

sqlFolderFollow= """SELECT CONCAT(folderFollow.collection_id, CONCAT(' - ' , folderFollow.user_id)) AS id, folderFollow.create_date AS created, 
users.directory_id, FOLDERFOLLOW.COLLECTION_ID, REPLACE(FOLDERFOLLOW.COLLECTION_ID, ' ', '') AS match_folder_id
FROM FILES.COLLECTION_NOTIFICATION AS folderFollow
JOIN FILES.USER AS users ON (users.id = folderFollow.user_id) 
"""


#Einlesen der Daten aus den SQL Queries in die Dataframes
dfFile = pd.read_sql(sqlFile, connfiles)
dfFolder = pd.read_sql(sqlFolder, connfiles)
dfFileLike = pd.read_sql(sqlFileLike, connfiles)
dfFileComment = pd.read_sql(sqlFileComment, connfiles)
dfFileFollow = pd.read_sql(sqlFileFollow, connfiles)
dfFolderFollow = pd.read_sql(sqlFolderFollow, connfiles)
dfFileLibrary = pd.read_sql(sqlFileLibrary, connfiles) 
dfMicroblogPostAttachmentLike = pd.read_sql(sqlMicrblogPostAttachmentLike, connfiles)


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

#Methode um das die kombinierte ConCat ID in 2 Teil IDs aufzuspliten
def split_bytes_at_separator(byte_data, separator):
    index = byte_data.find(separator)
    if index != -1:
        part1 = byte_data[:index]
        part2 = byte_data[index + len(separator):]
        return part1, part2
    else:
        return byte_data, b''


#Data Cleaing File
dfFile['ID'] = dfFile['ID'].apply(binary_to_uuidleng)
dfFile['MEDIA_ID'] = dfFile['MEDIA_ID'].apply(binary_to_uuidleng)
dfFile['CURRENT_REVISION_ID'] = dfFile['CURRENT_REVISION_ID'].apply(binary_to_uuidleng)
dfFile['MATCH_MEDIA_ID'] = dfFile['MATCH_MEDIA_ID'].apply(binary_to_uuidleng)
dfFile['SUB_ID'] = dfFile['SUB_ID'].apply(binary_to_uuidleng)
dfFile['PREVIOUSID'] = dfFile['PREVIOUSID'].apply(binary_to_uuidleng)
#Timestamp
#print(dfFile['CREATED'])
dfFile['CREATED'] = pd.to_datetime(dfFile['CREATED'])
# Zeitzone setzen
dfFile['CREATED'] = dfFile['CREATED'].dt.tz_localize('CET')
#print(dfFile['CREATED'])
#print(dfFile['LAST_UPDATED'])
dfFile['LAST_UPDATED'] = pd.to_datetime(dfFile['LAST_UPDATED'])
# Zeitzone setzen
dfFile['LAST_UPDATED'] = dfFile['LAST_UPDATED'].dt.tz_localize('CET')
#print(dfFile['LAST_UPDATED'])
#print(dfFile)

#Data Cleaning Folder
#print(dfFolder['ID'])
#print(dfFolder['MATCH_FOLDER_ID'])
dfFolder['ID'] = dfFolder['ID'].apply(binary_to_uuidleng)
dfFolder['MATCH_FOLDER_ID'] = dfFolder['MATCH_FOLDER_ID'].apply(binary_to_uuidleng) 
#print(dfFolder['ID'])
#print(dfFolder['MATCH_FOLDER_ID'])
#Timestamp
#print(dfFolder['CREATED'])
dfFolder['CREATED'] = pd.to_datetime(dfFolder['CREATED'])
# Zeitzone setzen
dfFolder['CREATED'] = dfFolder['CREATED'].dt.tz_localize('CET')
#print(dfFolder['CREATED'])
#print(dfFolder['LAST_UPDATED'])
dfFolder['LAST_UPDATED'] = pd.to_datetime(dfFolder['LAST_UPDATED'])
# Zeitzone setzen
dfFolder['LAST_UPDATED'] = dfFolder['LAST_UPDATED'].dt.tz_localize('CET')
#print(dfFolder['LAST_UPDATED'])
#print(dfFolder)


#Data Cleaning FileLibrary
#print(dfFileLibrary['ID'])
dfFileLibrary['ID'] = dfFileLibrary['ID'].apply(binary_to_uuidleng)
#print(dfFileLibrary['ID'])
#print(dfFileLibrary['EXTERNAL_CONTAINER_ID'])
#print(dfFileLibrary)

#Data Cleaning FileComment
#print(dfFileComment['ID'])
#print(dfFileComment['DIRECTORY_ID'])
#print(dfFileComment['MEDIA_ID'])
#print(dfFileComment['MATCH_COMMENT_ID'])
dfFileComment['ID'] = dfFileComment['ID'].apply(binary_to_uuidleng)
dfFileComment['MEDIA_ID'] = dfFileComment['MEDIA_ID'].apply(binary_to_uuidleng)
dfFileComment['MATCH_COMMENT_ID'] = dfFileComment['MATCH_COMMENT_ID'].apply(binary_to_uuidleng) 
#print(dfFileComment['ID'])
#print(dfFileComment['MEDIA_ID'])
#print(dfFileComment['MATCH_COMMENT_ID'])
#Content
dfFileComment['CONTENT'] = dfFileComment['CONTENT'].fillna('NaN')
#print(dfFileComment['CONTENT'])
dfFileComment['CONTENT'] = dfFileComment['CONTENT'].str.replace('\n', '')
dfFileComment['CONTENT'] = dfFileComment['CONTENT'].str.replace('\t', '')
dfFileComment['CONTENT'] = dfFileComment['CONTENT'].str.replace('\r', '')
dfFileComment['CONTENT'] = dfFileComment['CONTENT'].str.replace('\v', '')
dfFileComment['CONTENT'] = dfFileComment['CONTENT'].str.replace(';', ',')
dfFileComment['CONTENT'] = dfFileComment[['CONTENT']].applymap(lambda text: BeautifulSoup(text, 'html.parser').get_text())
#print(dfFileComment['CONTENT'])
#Timestamp
#print(dfFileComment['CREATED'])
dfFileComment['CREATED'] = pd.to_datetime(dfFileComment['CREATED'])
# Zeitzone setzen
#dfFileComment['CREATED'] = dfFileComment['CREATED'].dt.tz_localize('CET')
#print(dfFileComment['CREATED'])
#print(dfFileComment['LAST_UPDATED'])
dfFileComment['LAST_UPDATED'] = pd.to_datetime(dfFileComment['LAST_UPDATED'])
# Zeitzone setzen
dfFileComment['LAST_UPDATED'] = dfFileComment['LAST_UPDATED'].dt.tz_localize('CET')
#print(dfFileComment['LAST_UPDATED'])
#print(dfFileComment)

#Data Cleaning File Follow
#print(dfFileFollow['ID'])
#print(dfFileFollow['DIRECTORY_ID'])
#print(dfFileFollow['MEDIA_ID']) 
#print(dfFileFollow['MATCH_MEDIA_ID'])
dfFileFollow['ID'] = dfFileFollow['ID'].apply(binary_to_uuidleng) 
dfFileFollow['MATCH_MEDIA_ID'] = dfFileFollow['MATCH_MEDIA_ID'].apply(binary_to_uuidleng)
#print(dfFileFollow['ID'])
#print(dfFileFollow['MEDIA_ID'])
#print(dfFileFollow['MATCH_MEDIA_ID'])
#Timestamp
#print(dfFileComment['CREATED'])
dfFileComment['CREATED'] = pd.to_datetime(dfFileComment['CREATED'])
# Zeitzone setzen
dfFileComment['CREATED'] = dfFileComment['CREATED'].dt.tz_localize('CET')
#print(dfFileComment['CREATED'])
#print(dfFileFollow)

#Data Cleaning File Like
#print(dfFileLike['ID'])
#print(dfFileLike['DIRECTORY_ID']) # fine
#print(dfFileLike['FILE_ID'])
#print(dfFileLike['MATCH_MEDIA_ID'])
dfFileLike['ID'] = dfFileLike['ID'].apply(binary_to_uuidleng)# ToDo
dfFileLike['FILE_ID'] = dfFileLike['FILE_ID'].apply(binary_to_uuidleng)
dfFileLike['MATCH_MEDIA_ID'] = dfFileLike['MATCH_MEDIA_ID'].apply(binary_to_uuidleng) 
#print(dfFileLike['ID'])
#print(dfFileLike['DIRECTORY_ID']) # fine
#print(dfFileLike['FILE_ID'])
#print(dfFileLike['MATCH_MEDIA_ID'])
#Timestamp
#print(dfFileLike['CREATED'])
dfFileLike['CREATED'] = pd.to_datetime(dfFileLike['CREATED'])
# Zeitzone setzen
dfFileComment['CREATED'] = dfFileLike['CREATED'].dt.tz_localize('CET')
#print(dfFileLike['CREATED'])
#print(dfFileLike)


#Data Cleaning MicroblogPostAttachmentLike
#print(dfMicroblogPostAttachmentLike['ID'])
#print(dfMicroblogPostAttachmentLike['DIRECTORY_ID']) # fine
#print(dfMicroblogPostAttachmentLike['MATCH_MEDIA_ID'])
dfMicroblogPostAttachmentLike['ID'] = dfMicroblogPostAttachmentLike['ID'].apply(binary_to_uuidleng) # toDo to long
dfMicroblogPostAttachmentLike['MATCH_MEDIA_ID'] = dfMicroblogPostAttachmentLike['MATCH_MEDIA_ID'].apply(binary_to_uuidleng) #toDo 
#print(dfMicroblogPostAttachmentLike['ID'])
#print(dfMicroblogPostAttachmentLike['MATCH_MEDIA_ID'])
#Timestamp
#print(dfMicroblogPostAttachmentLike['CREATED'])
dfMicroblogPostAttachmentLike['CREATED'] = pd.to_datetime(dfMicroblogPostAttachmentLike['CREATED'])
# Zeitzone setzen
dfMicroblogPostAttachmentLike['CREATED'] = dfMicroblogPostAttachmentLike['CREATED'].dt.tz_localize('CET')
#print(dfMicroblogPostAttachmentLike['CREATED'])
#print(dfMicroblogPostAttachmentLike)

#Data Cleaning Folder Follow
#print(dfFolderFollow['ID'])
#print(dfFolderFollow['DIRECTORY_ID']) # fine
#print(dfFolderFollow['MATCH_FOLDER_ID'])
#print(dfFolderFollow['COLLECTION_ID'])
dfFolderFollow['ID'] = dfFolderFollow['ID'].apply(binary_to_uuidleng) 
dfFolderFollow['MATCH_FOLDER_ID'] = dfFolderFollow['MATCH_FOLDER_ID'].apply(binary_to_uuidleng) 
dfFolderFollow['COLLECTION_ID'] = dfFolderFollow['COLLECTION_ID'].apply(binary_to_uuidleng) 
#print(dfFolderFollow['ID'])
#print(dfFolderFollow['MATCH_FOLDER_ID'])
#print(dfFolderFollow['COLLECTION_ID'])
#Timestamp
#print(dfFolderFollow['CREATED'])
dfFolderFollow['CREATED'] = pd.to_datetime(dfFolderFollow['CREATED'])
# Zeitzone setzen
dfFolderFollow['CREATED'] = dfFolderFollow['CREATED'].dt.tz_localize('CET')
#print(dfFolderFollow['CREATED'])
#print(dfFolderFollow)


#Verbindung zu Neo4j aufbauen
neodb = neointerface.NeoInterface(host="neo4j://ma-lschloemer.bas.uni-koblenz.de:7687" , credentials=("neo4j", "neo4jneo4j"))

#Datenimport von Dataframe in Neo4j
#(Name Dataframe, Name Label, Aktivieren der Mergefunktion statt Create)
neodb.load_df(dfFile, "File", merge=True)
neodb.load_df(dfFolder, "Folder", merge=True)
neodb.load_df(dfFileComment, "Comment", merge=True)
neodb.load_df(dfFileLike, "Like", merge=True)
neodb.load_df(dfFileFollow, "Follow", merge=True)
neodb.load_df(dfFolderFollow, "Follow", merge=True)
neodb.load_df(dfFileLibrary, "FileLibrary", merge=True) 