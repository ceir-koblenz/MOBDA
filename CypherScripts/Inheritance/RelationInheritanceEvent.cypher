MATCH (evc:Event_Concept)
MATCH (ev:Event)
MERGE (ev)-[re:is_a]->(evc)