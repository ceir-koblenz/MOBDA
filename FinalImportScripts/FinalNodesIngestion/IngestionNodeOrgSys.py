#Skript um Organisation und System Node zu erstellen
#Beide sind aktuell noch Hardcoded, da sie nicht aus der Datenbank ersichtlich sind

#Library für Neointerface zum Ausführen der Query
import neointerface

#Verbindung zu Neo4j
neodb = neointerface.NeoInterface(host="neo4j://ma-lschloemer.bas.uni-koblenz.de:7687" , credentials=("neo4j", "neo4jneo4j"))

#Cypher Queries
queryOrganisation ="""
MERGE (o:Organisation {ID: 1})
    SET
    o.TITLE = 'Universität Koblenz-Landau',
    o.PHONE = '0261 2871667',
    o.EMAIL =  'asta.uni-koblenz.de'
"""

querySystem = """
MERGE (s:System {INSTANCETITLE: 'UniConnect'})
    SET
    s.SOFTWAREPRODUCT = 'HCL Connections',
    s.SOFTWARETYPE = 'ECS',
    s.SOFTWAREVENDOR = 'HCL Technologies',
    s.SOFTWAREVERSION = '6.0.0.0'
"""

#Ausführen der Queries mit NeoInterface
neodb.query(querySystem)
neodb.query(queryOrganisation)