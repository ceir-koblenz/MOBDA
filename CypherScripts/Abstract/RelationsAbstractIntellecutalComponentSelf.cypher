//Relations Abstract IntellectualComponent
MATCH (itcm:IntellectualComponent_Concept)
MATCH (att:Attachment_Concept)
MATCH (comm:Comment_Concept)


// Relation Attachment <-> Comment
MERGE (att)-[racic:attachment_contained_in_comment {cardinality: "maximal 1"}]->(comm)
MERGE (comm)-[rcca:comment_contains_attachment]->(att)
MERGE (att)-[rahc:attachment_has_comment]->(comm)
MERGE (comm)-[rcoa:comment_of_attachment {cardinality: "maximal 1"}]->(att)
MERGE (comm)-[rchc:comment_has_child]->(comm)
MERGE (comm)-[rchp:comment_has_parent {cardinality: "maximal 1"}]->(comm)

WITH [itcm, att, comm] AS ConICS
UNWIND ConICS AS conICS

//Recent Version 2x?
MERGE (conICS)-[richrv:intellectual_component_has_recent_version {cardinality: "exactly 1"}]->(conICS)
MERGE (conICS)-[richnv:intellectual_component_has_next_version]->(conICS)
MERGE (conICS)-[richov:intellectual_component_has_old_version]->(conICS)
MERGE (conICS)-[richpv:intellectual_component_has_previous_version]->(conICS)


