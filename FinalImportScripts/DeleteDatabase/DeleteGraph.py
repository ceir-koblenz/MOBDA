#Cypher Skript um die ganze Datenbank zu löschen
#Es muss wegen Event gestückelt werden
#Event.ID ist als einzige ID eine durchlauftende Zahl, dadurch ist die Stücklung so möglich

import neointerface
#Verbindung zu Neo4j 
neodb = neointerface.NeoInterface(host="neo4j://ma-lschloemer.bas.uni-koblenz.de:7687" , credentials=("neo4j", "neo4jneo4j"))


deleteGraphEvent25 = """
//für erste 2500000 Nodes Event mit Relations
MATCH (ev:Event)
WHERE ev.ID <=2500000
DETACH DELETE ev
"""
deleteGraphEvent2540 ="""
//für Nodes über 25000000 is 40000000 mit Relations
MATCH (ev:Event)
WHERE ev.ID > 2500000 AND ev.ID <=4000000
DETACH DELETE ev
"""

deleteGraphEvent4050 ="""
//Für Nodes mit ID über 4000000 und unter 5000000 mit Relatoins
MATCH (ev:Event)
WHERE ev.ID > 4000000 AND ev.ID <=5000000
DETACH DELETE ev
"""

deleteGraphEvent5060 ="""
//Für Nodes mit ID über 5000000 und unter 6000000 mit Relatoins
MATCH (ev:Event)
WHERE ev.ID > 5000000 AND ev.ID <=6000000
DETACH DELETE ev
"""

deleteGraphEvent6070 ="""
//Für Nodes mit ID über 6000000 und unter 7000000 mit Relatoins
MATCH (ev:Event)
WHERE ev.ID > 6000000 AND ev.ID <= 7000000
DETACH DELETE ev
"""

deleteGraphEvent7080 ="""
//Für Nodes mit ID über 7000000 und unter 8000000 mit Relatoins
MATCH (ev:Event)
WHERE ev.ID > 7000000 AND ev.ID <= 8000000
DETACH DELETE ev
"""

deleteGraphEvent8090 ="""
//Für Nodes mit ID über 8000000 und unter 9000000 mit Relatoins
MATCH (ev:Event)
WHERE ev.ID > 8000000 AND ev.ID <= 9000000
DETACH DELETE ev
"""
deleteGraphEvent90 = """
// Für Nodes mit ID über 9000000 mit Relations
MATCH (ev:Event)
WHERE ev.ID > 9000000
DETACH DELETE ev
"""

deleteGraphRest = """
//Für den Rest der Nodes mit Relations
MATCH (n)
DETACH DELETE n
"""

neodb.query(deleteGraphEvent25)
neodb.query(deleteGraphEvent2540)
neodb.query(deleteGraphEvent4050)
neodb.query(deleteGraphEvent5060)
neodb.query(deleteGraphEvent6070)
neodb.query(deleteGraphEvent7080)
neodb.query(deleteGraphEvent8090)
neodb.query(deleteGraphEvent90)
neodb.query(deleteGraphRest)