//Relations to Class Account

MATCH (acc:Account_Concept)
MATCH (role:Role_Concept)
MATCH (gro:Group_Concept)
MATCH (ag:Agent_Concept)
MATCH (arag:ArtifcialAgent_Concept)
MATCH (org:Organisation_Concept)
MATCH (per:Person_Concept)
MATCH (sop:SocialProfile_Concept)
MATCH (ev:Event_Concept)

//Relations Account
MERGE (acc)-[rakba:account_known_by_account]->(acc)
MERGE (acc)-[raka:account_knows_account]->(acc)
MERGE (acc)-[rahr:account_has_role]->(role)
MERGE (role)-[rroc:role_of_account]->(acc)
MERGE (acc)-[racig:account_contained_in_group]->(gro)
MERGE (gro)-[rgca:group_contains_account]->(acc)
MERGE (acc)-[rahsp:account_has_social_profile]->(sop)
MERGE (sop)-[rcpoc:social_profile_of_account]->(acc)
MERGE (ev)-[rape:account_performed_event {cardinality: "maximal 1" }]->(acc)
MERGE (acc)-[repba:event_performed_by_account]->(ev)

//All Relations of Agent an Childs
WITH [ag, arag, org, per] AS ConAG
UNWIND ConAG AS conAG
MATCH (acc:Account_Concept)
MATCH (orgo:OrganisationalGroup_Concept)
MATCH (sp:Space_Concept)
MATCH (dw:DigitalWorkspace_Concept)
MATCH (gro:Group_Concept)
MATCH (role:Role_Concept)
MATCH (org:Organisation_Concept)
MATCH (sy:System_Concept)
MERGE (acc)-[raoa:accont_of_agent {cardinality: "maximal 1"}]->(conAG)
MERGE (conAG)-[raha:agent_has_account]->(acc)

//Relation Organisation to Agent + Childs
MERGE (org)-[rorta:organisation_related_to_agent]->(conAG)
MERGE (conAG)-[rartg:agent_related_to_organisation]->(org)

//Realtions OrganisationalGroup
MERGE (conAG)-[raoog:agent_of_organisational_group]->(orgo)
MERGE (orgo)-[rogha:organisational_group_has_agent]->(conAG)
MERGE (orgo)-[rogodw:organisational_group_of_digital_workspace]->(dw)
MERGE (dw)-[rdwhog:digital_workspace_has_organisational_group]->(orgo)

//DigitalWorkspace
MERGE (dw)-[rdwha:digital_workspace_has_agent {cardinality: "minimal 1"}]->(conAG)
MERGE (conAG)-[raodw:agent_of_digital_workspace]->(dw)
//System
MERGE (sy)-[rsca:system_contains_account {cardinality: "minimal 1"}]-(acc)
MERGE (acc)-[racis:account_contained_in_system {cardinality: "exactly 1"}]-(sy)
//Relation Groupe <-> Role/Space
MERGE (role)-[rrog:role_of_group]->(gro) 
MERGE (gro)-[rghr:group_has_role]->(role)
MERGE (sp)-[rshg:space_has_group]->(gro)
MERGE (gro)-[rghs:group_has_space]->(sp)

//Relation Account <-> IntellectualComponent
WITH [] AS GoOn
MATCH (ic: IntellectualComponent_Concept)
MATCH (like:Like_Concept)
MATCH (comm:Comment_Concept)
WITH [ic, like, comm] AS ConIES 
UNWIND ConIES AS conIES
MATCH (acc:Account_Concept)

MERGE (acc)-[ractic:account_contributed_to_intellectual_component]->(conIES)
MERGE (conIES)-[riccba:intellectual_component_contributed_by_account]->(acc)

MERGE (acc)-[ramic2:account_mentioned_intellectual_component]->(conIES)
MERGE (conIES)-[ramic:intellectual_component_mentioned_by_account]->(acc)
