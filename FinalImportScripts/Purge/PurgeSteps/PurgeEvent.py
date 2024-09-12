#Skript um alle Mapping IDs zu bereinigen
#Alle Properties die nicht in der ColActDOnt vorgesehen sind werden auf "null" gesetzt und damit gelöcht

import neointerface

neodb = neointerface.NeoInterface(host="neo4j://ma-lschloemer.bas.uni-koblenz.de:7687" , credentials=("neo4j", "neo4jneo4j"))

#Queries für den Purge der MappingIDs

queryPurgeEvent25 = """
//Purge von Mapping Properties von Event
MATCH (ev:Event)
WHERE ev.ID <= 2500000
SET ev.UUID = null
SET ev.ITEM_UUID = null
SET ev.SOURCE_ID = null
SET ev.MATCH_ITEM_UUID = null
"""

queryPurgeEvent2565 = """
//Purge von Mapping Properties von Event
MATCH (ev:Event)
WHERE ev.ID > 2500000 AND ev.ID <=6500000
SET ev.UUID = null
SET ev.ITEM_UUID = null
SET ev.SOURCE_ID = null
SET ev.MATCH_ITEM_UUID = null
"""

queryPurgeEvent65 = """
//Purge von Mapping Properties von Event
MATCH (ev:Event)
WHERE ev.ID > 6500000 
SET ev.UUID = null
SET ev.ITEM_UUID = null
SET ev.SOURCE_ID = null
SET ev.MATCH_ITEM_UUID = null
"""

neodb.query(queryPurgeEvent25)
neodb.query(queryPurgeEvent2565)
neodb.query(queryPurgeEvent65)