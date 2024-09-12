//Relation of Concept Collection + Collection <-> SocialDocument + Item
MATCH (c:Collection_Concept)
MATCH (sd:SocialDocument_Concept)
MERGE (c)-[rccsd:collection_contains_social_document {cardinality: "minimal 2"}]->(sd)
MERGE (sd)-[rcsdc:social_document_contained_in_collection]->(c)
MERGE (c)-[rchp:collection_has_parent {cardinality: "maximal 1"}]->(c)
MERGE (c)-[rchc:collection_has_child]->(c)
