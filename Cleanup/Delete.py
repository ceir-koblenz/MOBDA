import pyodbc
import time
from pyneoinstance import Neo4jInstance
from pyneoinstance import load_yaml_file


start_time = time.time()

# Set up connections 

config = load_yaml_file('C:/Users/lschloemer/Nextcloud/MOBDA 2.0/VSCodeMOBDARepository/Python/a.yaml')
db_info = config['db_infoneo']
graph = Neo4jInstance(db_info['uri'],db_info['database'],db_info['password'])

DSN = "Arrow Flight SQL ODBC DSN"
cnxn = pyodbc.connect(DSN=DSN ,autocommit=True)


#Cypher Queries

deleteGraphEvent15 = """
//für erste 1500000 Nodes Event mit Relations
MATCH (ev:Event)
WHERE ev.id <=1500000
DETACH DELETE ev
"""

deleteGraphEvent1520 = """
//für erste über 15000000 is 25000000 mit Relations
MATCH (ev:Event)
WHERE ev.id > 1500000 AND ev.id <=2000000
DETACH DELETE ev
"""
deleteGraphEvent2030 ="""
//für Nodes über 2500000 is 4000000 mit Relations
MATCH (ev:Event)
WHERE ev.id > 2000000 AND ev.id <=3000000
DETACH DELETE ev
"""

deleteGraphEvent3040 ="""
//Für Nodes mit id über 4000000 und unter 5000000 mit Relatoins
MATCH (ev:Event)
WHERE ev.id > 3000000 AND ev.id <=4000000
DETACH DELETE ev
"""

deleteGraphEvent4050 ="""
//Für Nodes mit id über 5000000 und unter 6000000 mit Relatoins
MATCH (ev:Event)
WHERE ev.id > 4000000 AND ev.id <=5000000
DETACH DELETE ev
"""

deleteGraphEvent5060 ="""
//Für Nodes mit id über 6000000 und unter 7000000 mit Relatoins
MATCH (ev:Event)
WHERE ev.id > 5000000 AND ev.id <= 6000000
DETACH DELETE ev
"""

deleteGraphEvent6070 ="""
//Für Nodes mit id über 7000000 und unter 8000000 mit Relatoins
MATCH (ev:Event)
WHERE ev.id > 6000000 AND ev.id <= 7000000
DETACH DELETE ev
"""

deleteGraphEvent7080 ="""
//Für Nodes mit id über 8000000 und unter 9000000 mit Relatoins
MATCH (ev:Event)
WHERE ev.id > 7000000 AND ev.id <= 8000000
DETACH DELETE ev
"""

deleteGraphEvent8090 = """
// Für Nodes mit id über 9000000 und unter 10000000 mit Relatoins
MATCH (ev:Event)
WHERE ev.id > 8000000 AND ev.id <= 9000000
DETACH DELETE ev
"""
deleteGraphEvent9010 = """
// Für Nodes mit id über 9000000 und unter 10000000 mit Relatoins
MATCH (ev:Event)
WHERE ev.id > 9000000 AND ev.id <= 10000000
DETACH DELETE ev
"""

deleteGraphEvent100 = """
// Für Nodes mit id über 10000000 mit Relations
MATCH (ev:Event)
WHERE ev.id > 10000000
DETACH DELETE ev
"""

deleteGraphAccount = """
//Für den Rest der Nodes mit Relations
MATCH (n:Account)
DETACH DELETE n
"""

deleteGraphFile = """
//Für den Rest der Nodes mit Relations
MATCH (n:File)
DETACH DELETE n
"""

deleteGraphWiki = """
//Für den Rest der Nodes mit Relations
MATCH (n:WikiPage)
DETACH DELETE n
"""
deleteGraphBlogPost = """
//Für den Rest der Nodes mit Relations
MATCH (n:BlogPost)
DETACH DELETE n
"""
deleteGraphBoardPost = """
//Für den Rest der Nodes mit Relations
MATCH (n:BoardPost)
DETACH DELETE n
"""

deleteGraphRest = """
//Für den Rest der Nodes mit Relations
MATCH (n)
DETACH DELETE n
"""

graph.execute_write_query(deleteGraphEvent15, "neo4j")
graph.execute_write_query(deleteGraphEvent1520, "neo4j")
graph.execute_write_query(deleteGraphEvent2030, "neo4j")
graph.execute_write_query(deleteGraphEvent3040, "neo4j")
graph.execute_write_query(deleteGraphEvent4050, "neo4j")
graph.execute_write_query(deleteGraphEvent5060, "neo4j")
graph.execute_write_query(deleteGraphEvent6070, "neo4j")
graph.execute_write_query(deleteGraphEvent7080, "neo4j")
graph.execute_write_query(deleteGraphEvent8090, "neo4j")
graph.execute_write_query(deleteGraphEvent9010, "neo4j")
graph.execute_write_query(deleteGraphEvent100, "neo4j")
graph.execute_write_query(deleteGraphAccount, "neo4j")
graph.execute_write_query(deleteGraphFile, "neo4j")
graph.execute_write_query(deleteGraphBoardPost, "neo4j")
graph.execute_write_query(deleteGraphBlogPost, "neo4j")
graph.execute_write_query(deleteGraphWiki, "neo4j")
graph.execute_write_query(deleteGraphRest, "neo4j")

("ProcessEvent finished --- %s seconds ---" % (time.time() - start_time))

# Close the Neo4j driver
print("Process finished --- %s seconds ---" % (time.time() - start_time))