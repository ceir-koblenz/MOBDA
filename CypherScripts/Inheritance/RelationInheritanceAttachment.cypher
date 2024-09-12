//Inheritance of Attachment 
MATCH (atc:Attachement_Concept)
MATCH (itc:Item_Concept)
MATCH (coc:Component_Concept)
MATCH (icc:IntellectualComponent_Concept)
WITH [atc, itc, coc, icc] AS ConATIN 
UNWIND ConATIN as conATIN
MATCH (at:Attachment)
MERGE (at)-[rat:is_a]->(conATIN)