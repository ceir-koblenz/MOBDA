#Skript zum Import der Daten aus der Homepage Datenbank
#Libraries
#Database Connector
from ibm_db import connect
import ibm_db_dbi
#Pandas ist für den Dataframe 
import pandas as pd
#NeoInterface ist Schnittstelle zu Neo4j
import neointerface

#Verbindung zu UniConnect Datenbank Peopledb
cnxnpeopledb = connect('DATABASE=peopledb;'
                 'HOSTNAME=db2.uniconnect.de;'  # localhost would work 
                 'PORT=50000;'
                 'PROTOCOL=TCPIP;'
                 'UID=reader19;'
                 'PWD=b2BwaRHN;', '', '')

connpeopledb = ibm_db_dbi.Connection(cnxnpeopledb)

#SQL Queries

sqlAccount = """SELECT e.prof_mail_lower AS email, e.prof_guid AS id, CONCAT(e.prof_given_name, CONCAT(' ', e.prof_surname)) AS publicName,
 e.PROF_UID AS privateName, e.Prof_GUID
FROM EMPINST.EMPLOYEE e
"""

sqlPerson = """SELECT prof_mail_lower AS email, prof_surname AS family_name, prof_given_name AS given_name, prof_guid AS id, 
prof_telephone_number AS phone, PROF_GUID 
FROM EMPINST.employee
"""

sqlSocialProfileTag = """SELECT prof_tag_id AS id, prof_tag as label, people.prof_guid
FROM EMPINST.PEOPLE_TAG AS tags
JOIN EMPINST.employee As people ON (people.prof_key = tags.prof_source_key)
"""


#Einlesen der Daten aus den SQL Queries in die Dataframes
dfAccount= pd.read_sql(sqlAccount, connpeopledb)
dfPerson= pd.read_sql(sqlPerson, connpeopledb)
dfSocialProfileTag = pd.read_sql(sqlSocialProfileTag, connpeopledb)


#Verbindung zu Neo4j
neodb = neointerface.NeoInterface(host="neo4j://ma-lschloemer.bas.uni-koblenz.de:7687" , credentials=("neo4j", "neo4jneo4j"))

#Importieren der Daten aus den Dataframes in Neo4j
#(Name Dataframe, Name Label, Aktivieren der Mergefunktion statt Create)
neodb.load_df(dfAccount, "Account", merge=True)
neodb.load_df(dfPerson, "Person", merge=True)
neodb.load_df(dfSocialProfileTag, "Tag", merge=True)

