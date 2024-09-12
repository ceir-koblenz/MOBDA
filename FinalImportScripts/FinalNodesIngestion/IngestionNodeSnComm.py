#Skript zum Import der Daten aus der Homepage Datenbank
#Libraries
#Database Connector
from ibm_db import connect
import ibm_db_dbi
#Pandas ist für den Dataframe 
import pandas as pd
#NeoInterface ist Schnittstelle zu Neo4j
import neointerface

#Verbindung zur UniConnect Datenbank Sncomm
cnxnsncomm = connect('DATABASE=sncomm;'
                 'HOSTNAME=db2.uniconnect.de;'  # localhost would work 
                 'PORT=50000;'
                 'PROTOCOL=TCPIP;'
                 'UID=reader19;'
                 'PWD=b2BwaRHN;', '', '')

connsncomm = ibm_db_dbi.Connection(cnxnsncomm)

#SQL Queries

sqlGroupWorkspace = """SELECT c.COMMUNITY_UUID AS ID, c.NAME AS title
FROM sncomm.COMMUNITY c   
"""

#Einlesen der Daten aus den SQL Queries in die Dataframes
dfGroupWorkspace = pd.read_sql(sqlGroupWorkspace, connsncomm)

#Verbindung zu Neo4j
neodb = neointerface.NeoInterface(host="neo4j://ma-lschloemer.bas.uni-koblenz.de:7687" , credentials=("neo4j", "neo4jneo4j"))

#Importieren der Daten aus den Dataframes in Neo4j
#(Name Dataframe, Name Label, Aktivieren der Mergefunktion statt Create)
neodb.load_df(dfGroupWorkspace, "GroupWorkspace", merge=True)
