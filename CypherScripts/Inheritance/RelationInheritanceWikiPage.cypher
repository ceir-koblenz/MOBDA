MATCH (wikipc:WikiPage_Concept)
MATCH (itc:Item_Concept)
MATCH (iec:IntellectualEntity_Concept)
WITH [wikipc, itc, iec] AS ConWIKIPIN
UNWIND ConWIKIPIN as conWIKIPIN
MATCH (wikip:WikiPage)
MERGE (wikip)-[rwikip:is_a]->(conWIKIPIN)