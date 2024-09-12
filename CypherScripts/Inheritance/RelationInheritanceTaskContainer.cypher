MATCH (coc:Container_Concept)
MATCH (taskcc:TaskContainer_Concept)
WITH [coc, taskcc] AS ConTASKCIN
UNWIND ConTASKCIN as conTASKCIN
MATCH (taskc:TaskContainer)
MERGE (taskc)-[rtaskc:is_a]->(conTASKCIN)