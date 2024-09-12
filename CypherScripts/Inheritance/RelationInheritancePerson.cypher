MATCH (agc:Agent_Concept)
MATCH (pec:Person_Concept)
WITH [agc, pec] AS ConPERIN
UNWIND ConPERIN as conPERIN
MATCH (pe:Person)
MERGE (pe)-[rpe:is_a]->(conPERIN)