MATCH (syc:System_Concept)
MATCH (sy:System)
MERGE (sy)-[rsy:is_a]->(syc)