MATCH (coc:Container_Concept)
MATCH (wbc:Weblog_Concept)
WITH [coc, wbc] AS ConWBC
UNWIND ConWBC as conWBC
MATCH (wb:Weblog)
MERGE (wb)-[rwb:is_a]->(conWBC)
