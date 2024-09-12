from ibm_db import connect
import pandas as pd
import ibm_db_dbi
#import html
#import io
from bs4 import BeautifulSoup
import neointerface
import numpy as np
import uuid
from datetime import datetime, timezone, timedelta
from dateutil import tz

#Datenbanverbindung anpassen
cnxnpatch = connect('DATABASE=wikis;'
                 'HOSTNAME=db2.uniconnect.de;'  # localhost would work 
                 'PORT=50000;'
                 'PROTOCOL=TCPIP;'
                 'UID=reader19;'
                 'PWD=b2BwaRHN;', '', '')
#database Connections immer gleich Variable bei der Datenbankverbindung
connpatch = ibm_db_dbi.Connection(cnxnpatch)

#SQL Query anpassen
sqlPatchWork = """SELECT CONCAT(wikiarticles.ID , CONCAT(' - ',follows.user_id)) AS id, follows.create_date AS created, 
users.DIRECTORY_ID, WIKIARTICLES.id AS wiki_id, REPLACE(WIKIARTICLES.media_id, ' ', '') AS match_media_id
FROM wikis.LIBRARY_NOTIFICATION AS follows
JOIN WIKIS.MEDIA_REVISION AS wikiarticles ON follows.library_id = wikiarticles.library_id
JOIN WIKIS.USER AS users ON (users.id = follows.user_id)
"""

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
        # b vor dem Bindestrich wichitg wegen Dateityp, SQL muss auch diese Formatierung verwenden
    
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


#Einlesen der Daten in den Dataframe
dfPatchWork = pd.read_sql(sqlPatchWork, connpatch)
#dfPatchWork2 = pd.read_sql(sqlTask, connblogs)

#Patchwork Basteine:
#Füllen von Null/leeren Werten
#dfPatchWork['ID'] = dfPatchWork['ID'].fillna('NaN')
#Breinigen von Files/Wikis IDs
#dfPatchWork['ID'] = dfPatchWork['ID'].apply(binary_to_uuidleng)
#Timestamp
#dfPatchWork['CREATED'] = pd.to_datetime(dfPatchWork['CREATED'])
# Zeitzone setzen
#dfPatchWork['CREATED'] = dfPatchWork['CREATED'].dt.tz_localize('CET')
#Content bereinigen
#dfPatchWork['CONTENT'] = dfPatchWork['CONTENT'].fillna('NaN')
#dfPatchWork['CONTENT'] = dfPatchWork['CONTENT'].str.replace('\n', '')
#dfPatchWork['CONTENT'] = dfPatchWork['CONTENT'].str.replace('\t', '')
#dfPatchWork['CONTENT'] = dfPatchWork['CONTENT'].str.replace('\r', '')
#dfPatchWork['CONTENT'] = dfPatchWork['CONTENT'].str.replace('\v', '')
#dfPatchWork['CONTENT'] = dfPatchWork['CONTENT'].str.replace(';', ',')
#dfPatchWork['CONTENT'] = dfPatchWork[['CONTENT']].applymap(lambda text: BeautifulSoup(text, 'html.parser').get_text())

dfPatchWork['ID'] = dfPatchWork['ID'].fillna('NaN')
dfPatchWork['ID'] = dfPatchWork['ID'].apply(binary_to_uuidleng)
dfPatchWork['WIKI_ID'] = dfPatchWork['WIKI_ID'].fillna('NaN')
dfPatchWork['WIKI_ID'] = dfPatchWork['WIKI_ID'].apply(binary_to_uuidleng)
dfPatchWork['MATCH_MEDIA_ID'] = dfPatchWork['MATCH_MEDIA_ID'].apply(binary_to_uuidleng)
dfPatchWork['CREATED'] = pd.to_datetime(dfPatchWork['CREATED'])
#dfPatchWork['CREATED'] = dfPatchWork['CREATED'].dt.tz_localize('CET')
dfPatchWork['CREATED'] = dfPatchWork['CREATED'].dt.tz_localize(tz.tzlocal())
print(dfPatchWork)

#Data Cleaning SocialProfile
#Timestamp
#print(dfSocialProfile['CREATED'])
#dfPatchWork['CREATED'] = pd.to_datetime(dfPatchWork['CREATED'])
# Zeitzone setzen
#dfPatchWork['CREATED'] = dfPatchWork['CREATED'].dt.tz_localize('CET')
#print(dfSocialProfile['CREATED'])
#print(dfSocialProfile['LAST_UPDATED'])
#dfPatchWork['LAST_UPDATED'] = pd.to_datetime(dfPatchWork['LAST_UPDATED'])
# Zeitzone setzen
#dfPatchWork['LAST_UPDATED'] = dfPatchWork['LAST_UPDATED'].dt.tz_localize('CET')
#print(dfSocialProfile['LAST_UPDATED'])

#dfPatchWork['MEDIA_ID'] = dfPatchWork['MEDIA_ID'].apply(binary_to_uuidleng) #todo
#print(dfPatchWork['ID'])
#print(dfPatchWork['MEDIA_ID'])
#dfPatchWork['MEDIA_ID'] = dfPatchWork['MEDIA_ID'].fillna('NaN')
#dfPatchWork['MEDIA_ID'].replace(to_replace=[None], value=np.nan, inplace=True)
#dfPatchWork['MEDIA_ID'] = dfPatchWork['MEDIA_ID'].fillna(value=np.nan)
#print(dfPatchWork['MEDIA_ID'])
#dfPatchWork['MEDIA_ID'] = dfPatchWork['MEDIA_ID'].apply(binary_to_uuidleng)
#print(dfPatchWork['MEDIA_ID'])
#dfPatchWork['ID'] = dfPatchWork['ID'].apply(binary_to_uuidleng)
#dfPatchWork['WIKI_ID'] = dfPatchWork['WIKI_ID'].apply(binary_to_uuidleng)
#print(dfPatchWork['ID'])
#print(dfPatchWork['WIKI_ID'])

#Verbindung zu Neo4j
neodb = neointerface.NeoInterface(host="neo4j://ma-lschloemer.bas.uni-koblenz.de:7687" , credentials=("neo4j", "neo4jneo4j"))

#Als dritte Variable Label des Nodes übergeben
neodb.load_df(dfPatchWork, "Follow", merge=True)