MATCH (agc:Agent_Concept)
MATCH (ogc:Organisation_Concept)
WITH [ogc, agc] AS ConORCIN
UNWIND ConORCIN as conORCIN
MATCH (og:Organisation)
MERGE (og)-[rog:is_a]->(conORCIN)