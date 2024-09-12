#Skript um alle Mapping IDs zu bereinigen
#Alle Properties die nicht in der ColActDOnt vorgesehen sind werden auf "null" gesetzt und damit gelöcht

import neointerface

neodb = neointerface.NeoInterface(host="neo4j://ma-lschloemer.bas.uni-koblenz.de:7687" , credentials=("neo4j", "neo4jneo4j"))

#Queries für den Purge der MappingIDs

queryPurgeAccount = """
//Purge von Mapping Properties von Account
MATCH (acc:Account)
SET acc.PROF_GUID = null
"""
queryPurgePerson = """
//Purge von Mapping Properties von Person
MATCH (per:Person)
SET per.PROF_GUID = null
"""

neodb.query(queryPurgeAccount)
neodb.query(queryPurgePerson)
