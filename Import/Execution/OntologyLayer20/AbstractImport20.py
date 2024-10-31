import pandas as pd
import pyodbc
import numpy
import time
from pyneoinstance import Neo4jInstance
from pyneoinstance import load_yaml_file
import logging

logging.basicConfig(level=logging.INFO)

def importingAbstractNodes(graph) -> None:
    """
    creating nodes and relations of the ontology layer
    1 cypher queries
    2 execution of those cypher queries
    """
    start_time = time.time()


    queryAbstractStructureA = """
    //Abstract Strucutre
    //Abstract Concepts
    MERGE (c:Collection_Concept {name: "Collection_Concept"})
    MERGE (sd:SocialDocument_Concept {name: "SocialDocument_Concept"})
    MERGE (it:Item_Concept {name: "Item_Concept"})
    MERGE (ie:IntellectualEntity_Concept {name: "IntellectualEntity_Concept"})
    MERGE (cm:Component_Concept {name: "Component_Concept"})
    MERGE (sc:SimpleComponent_Concept {name: "SimpleComponent_Concept"})
    MERGE (ic:IntellectualComponent_Concept {name: "IntellectualComponent_Concept"})
    MERGE (co:Container_Concept {name: "Container_Concept"})
    MERGE (sp:Space_Concept {name: "Space_Concept"})
    MERGE (sy:System_Concept {name: "System_Concept"})
    MERGE (dw:DigitalWorkspace_Concept {name: "DigitalWorkspace_Concept"})

    //Concepts IntellectualEntity
    MERGE (b:BlogPost_Concept {name: "BlogPost_Concept"})
    MERGE (wip:WikiPage_Concept {name: "WikiPage_Concept"})
    MERGE (ta:Task_Concept {name: "Task_Concept"})
    MERGE (sop:SocialProfile_Concept {name: "SocialProfile_Concept"})
    MERGE (mbp:MicroblogPost_Concept {name: "MicroblogPost_Concept"})
    MERGE (bp:BoardPost_Concept {name: "BoardPost_Concept"})
    MERGE (mame:MailMessage_Concept {name: "MailMessage_Concept"}) 
    MERGE (fol:Folder_Concept {name: "Folder_Concept "})
    MERGE (fil:File_Concept {name: "File_Concept"})
    MERGE (chme:ChatMessage_Concept {name: "ChatMessage_Concept"})
    MERGE (met:Meeting_Concept {name: "Meeting_Concept"})
    MERGE (caen:CalendarEntry_Concept {name: "CalendarEntry_Concept"})

    //Subclass Relations
    //Major Entities
    MERGE (ic)-[riccm:sub_class_of]->(cm)
    MERGE (sc)-[rsccm:sub_class_of]->(cm)
    MERGE (cm)-[rcmit:sub_class_of]->(it)
    MERGE (ie)-[rieit:sub_class_of]->(it)

    // Subclass IE Concept to IE
    WITH [b, wip, ta, sop, mbp, bp, mame, fol, fil, chme, met, caen] AS ConIEIT //Concept InterlectualEntity to InterlectualEntity
    UNWIND ConIEIT as conIEIT
    MATCH (ie:IntellectualEntity_Concept)
    MERGE (conIEIT)-[rcie:sub_class_of]->(ie)

    //Subclass IE Concept to IT (UNWIND from Subclass IE)
    //MATCH (it:Item_Concept)
    MERGE (conIEIT)-[rcit:sub_class_of]->(it)
    """
    queryAbstractStructureB = """
    //Concepts Container
    MERGE (w:Weblog_Concept {name: "Weblog_Concept"})
    MERGE (wi:Wiki_Concept {name: "Wiki_Concept"})
    MERGE (taco:TaskContainer_Concept {name: "TaskContainer_Concept"})
    MERGE (spc:SocialProfileContainer_Concept {name: "SocialProfileContainer_Concept"})
    MERGE (mibl:Microblog_Concept {name: "Microblog_Concept"})
    MERGE (mebo:MessageBoard_Concept {name: "MessageBoard_Concept"})
    MERGE (maco:MailContainer_Concept {name: "MailContainer_Concept"})
    MERGE (fili:FileLibrary_Concept {name: "FileLibrary_Concept"})
    MERGE (chach:ChatChannel_Concept {name: "ChatChannel_Concept"})
    MERGE (meco:MeetingContainer_Concept {name: "MeetingContainer_Concept"})
    MERGE (cal:Calendar_Concept {name: "Calendar_Concept"})

    //Subclass CO Concept to Container
    WITH [w, wi, taco, spc, mibl, mebo, maco, fili, chach, meco, cal] AS ConCOCO
    UNWIND ConCOCO as conCOCO
    MATCH (co:Container_Concept)
    MERGE (conCOCO)-[rcco:sub_class_of]->(co)

    //Concepts SimpleComponent
    MERGE (foll:Follow_Concept {name: "Follow_Concept"})
    MERGE (like:Like_Concept {name: "Like_Concept"})
    MERGE (rea:Reaction_Concept {name: "Reaction_Concept"})
    MERGE (subs:Subscription_Concept {name: "Subscription_Concept"})
    MERGE (tag:Tag_Concept {name: "Tag_Concept"})
    MERGE (vote:Vote_Concept {name: "Vote_Concept"})

    //Subclass SC Concept to SimpleComponents 
    WITH[foll, like, rea, subs, tag, vote] AS ConSC
    UNWIND ConSC as conSC
    MATCH (sc:SimpleComponent_Concept)
    MERGE (conSC)-[rcsc:sub_class_of]->(sc)

    //Subclass SimpleComponent Concept to Component
    //MATCH (cm:Component_Concept)
    MERGE (conSC)-[rcsccm:sub_class_of]->(cm)

    //Subclass SimpleComponent Concept to Item
    //MATCH (it:Item_Concept)
    MERGE (conSC)-[rcscit:sub_class_of]->(it)
    """
    queryAbstractStructureC = """
    //Concepts IntellectualComponent
    MERGE (att:Attachment_Concept {name: "Attachment_Concept"})
    MERGE (comm:Comment_Concept {name: "Comment_Concept"})

    //Subclass IntellectualComponent Concept to IntellecutalComponent
    WITH [att, comm] AS ConIC 
    UNWIND ConIC as conIC
    MATCH (ic:IntellectualComponent_Concept)
    MERGE (conIC)-[rcicic:sub_class_of]->(ic)

    //Subclass IntellctualComponent Concept to Component
    MERGE (conIC)-[rcicc:sub_class_of]->(cm)

    //Subclass IntellctualComponent Concept to item
    MERGE (conIC)-[rcicit:sub_class_of]->(it)

    //Concept Space
    MERGE (gws:GroupWorkspace_Concept {name: "GroupWorkspace_Concept"})
    MERGE (op:OrganisationalPlatform_Concept {name: "OrganisationalPlatform_Concept"})
    MERGE (us:UserWorkspace_Concept {name: "UserWorkspace_Concept"})

    //Sublass Space Concept to Space
    WITH [gws, op, us] AS ConSP 
    UNWIND ConSP as conSP
    MATCH (sp:Space_Concept)
    MERGE (conSP)-[rcspsp:sub_class_of]->(sp)

    //Concepts Event (rot)
    MERGE (ev:Event_Concept {name: "Event_Concept"})

    //Concepts Account (gelb)
    MERGE (acc:Account_Concept {name: "Account_Concept"})
    MERGE (role:Role_Concept {name: "Role_Concept"})
    MERGE (gro:Group_Concept {name: "Group_Concept"})
    MERGE (ogro:OrganisationalGroup_Concept {name: "OrganisationalGroup_Concept"})
    MERGE (ag:Agent_Concept {name: "Agent_Concept"})
    MERGE (arag:ArtifcialAgent_Concept {name: "ArtifcialAgent_Concept"})
    MERGE (org:Organisation_Concept {name: "Organisation_Concept"})
    MERGE (per:Person_Concept {name: "Person_Concept"})

    //Sublass  Agent 
    WITH [arag, org, per] AS ConAG
    UNWIND ConAG AS conAG 
    MATCH (ag:Agent_Concept)
    MERGE (conAG)-[rcag:sub_class_of]->(ag)
    """

    queryRelationAbstractAccountItemIntellectualEnity = """
    //abstract Relation Account <-> Item & IntellectualEntity + Childs

    //Concepts Abstract
    MATCH (it:Item_Concept)
    MATCH (cm:Component_Concept)
    MATCH (scm:SimpleComponent_Concept)
    MATCH (itcm:IntellectualComponent_Concept)
    MATCH (ie:IntellectualEntity_Concept)

    //Concepts IntellecutalEntity
    MATCH (b:BlogPost_Concept)
    MATCH (wip:WikiPage_Concept)
    MATCH (ta:Task_Concept)
    MATCH (sop:SocialProfile_Concept)
    MATCH (mbp:MicroblogPost_Concept)
    MATCH (bp:BoardPost_Concept)
    MATCH (mame:MailMessage_Concept)
    MATCH (fol:Folder_Concept)
    MATCH (fil:File_Concept)
    MATCH (chme:ChatMessage_Concept)
    MATCH (met:Meeting_Concept)
    MATCH (caen:CalendarEntry_Concept)

    //Concepts SimpleComponent
    MATCH  (foll:Follow_Concept)
    MATCH  (like:Like_Concept)
    MATCH  (rea:Reaction_Concept)
    MATCH  (subs:Subscription_Concept)
    MATCH  (tag:Tag_Concept)
    MATCH  (vote:Vote_Concept)

    //Concepts IntellcutalComponent
    MATCH  (att:Attachment_Concept)
    MATCH  (comm:Comment_Concept)
    //Realtions 
    WITH [cm, it, scm, itcm, ie, b, wip, ta, sop, mbp, bp, mame, fol, fil, chme, met, caen, foll, like, rea, subs, tag, vote, att, comm] AS ConAI
    UNWIND ConAI AS conAI 
    MATCH (acc:Account_Concept)
    MATCH (ev:Event_Concept)
    //Account <-> Item
    MERGE (acc)-[raci:account_created_item]->(conAI)
    MERGE (conAI)-[ricba:item_createdd_by_account]->(acc)

    //Event <-> Item
    MERGE (ev)-[reai:event_affects_item {cardinality: "maximal 1"}]->(conAI)
    MERGE (conAI)-[riabe:item_affected_by_event]->(ev)
    //Reset zwischen MATCH und MERGE
    WITH [] AS GoOn

    //Concepts IntellecutalEntity
    MATCH (ie:IntellectualEntity_Concept)
    MATCH (b:BlogPost_Concept)
    MATCH (wip:WikiPage_Concept)
    MATCH (ta:Task_Concept)
    MATCH (sop:SocialProfile_Concept)
    MATCH (mbp:MicroblogPost_Concept)
    MATCH (bp:BoardPost_Concept)
    MATCH (mame:MailMessage_Concept)
    MATCH (fol:Folder_Concept)
    MATCH (fil:File_Concept)
    MATCH (chme:ChatMessage_Concept)
    MATCH (met:Meeting_Concept)
    MATCH (caen:CalendarEntry_Concept)

    WITH [ie, b, wip, ta, sop, mbp, bp, mame, fol, fil, chme, met, caen] AS ConAIE
    UNWIND ConAIE AS conAIE 
    MATCH (acc:Account_Concept)
    MERGE (acc)-[ractie:account_contributed_to_intellectual_entity]->(conAIE)
    MERGE (conAIE)-[riecba:intellectual_entity_contributed_by_account]->(acc)
    MERGE (acc)-[ramico:account_mentioned_intectual_entity]->(conAIE)
    MERGE (conAIE)-[riemba:intellectual_entity_mentioned_by_account]->(acc)
    """
    queryRelationAbstractAccountYellow = """
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
    """

    queryRelationAbstractCollection = """
    //Relation of Concept Collection + Collection <-> SocialDocument + Item
    MATCH (c:Collection_Concept)
    MATCH (sd:SocialDocument_Concept)
    MERGE (c)-[rccsd:collection_contains_social_document {cardinality: "minimal 2"}]->(sd)
    MERGE (sd)-[rcsdc:social_document_contained_in_collection]->(c)
    MERGE (c)-[rchp:collection_has_parent {cardinality: "maximal 1"}]->(c)
    MERGE (c)-[rchc:collection_has_child]->(c)
    """
    queryRelationAbstractContainerSpace = """
    //Space_Concept <-> Container_Concept with Childs
    //Container_Concept with Childs
    MATCH (co:Container_Concept)
    MATCH (w:Weblog_Concept)
    MATCH (wi:Wiki_Concept)
    MATCH (taco:TaskContainer_Concept)
    MATCH (spc:SocialProfileContainer_Concept)
    MATCH (mibl:Microblog_Concept)
    MATCH (mebo:MessageBoard_Concept)
    MATCH (maco:MailContainer_Concept)
    MATCH (fili:FileLibrary_Concept)
    MATCH (chach:ChatChannel_Concept)
    MATCH (meco:MeetingContainer_Concept)
    MATCH (cal:Calendar_Concept)

    WITH [co, w, wi, taco, spc, mibl, mebo, maco, fili, chach, meco, cal] AS ConCOCO
    UNWIND ConCOCO as conCOCO
    //Space_Concept with Childs
    MATCH (spc:Space_Concept)
    MATCH (gws:GroupWorkspace_Concept)
    MATCH (op:OrganisationalPlatform_Concept)
    MATCH (us:UserWorkspace_Concept)

    //Erstellung Relations Space <-> Container und Childs
    MERGE (conCOCO)-[rccisspc:container_contained_in_space {cardinality: "exactly 1"}]->(spc)
    MERGE (spc)-[rsccspc:space_contains_container]->(conCOCO)
    MERGE (conCOCO)-[rccisgws:container_contained_in_space {cardinality: "exactly 1"}]->(gws)
    MERGE (gws)-[rsccgws:space_contains_container]->(conCOCO)
    MERGE (conCOCO)-[rccisop:container_contained_in_space {cardinality: "exactly 1"}]->(op)
    MERGE (op)-[rsccop:space_contains_container]->(conCOCO)
    MERGE (conCOCO)-[rccisus:container_contained_in_space {cardinality: "exactly 1"}]->(us)
    MERGE (us)-[rsccus:space_contains_container]->(conCOCO)
    """
    queryRelationAbstractIntellectualEntitySelf = """
    //Abstract Relations with itself
    MATCH (ie:IntellectualEntity_Concept)
    MATCH (b:BlogPost_Concept)
    MATCH (wip:WikiPage_Concept)
    MATCH (ta:Task_Concept)
    MATCH (sop:SocialProfile_Concept)
    MATCH (mbp:MicroblogPost_Concept)
    MATCH (bp:BoardPost_Concept)
    MATCH (mame:MailMessage_Concept)
    MATCH (fol:Folder_Concept)
    MATCH (fil:File_Concept)
    MATCH (chme:ChatMessage_Concept)
    MATCH (met:Meeting_Concept)
    MATCH (caen:CalendarEntry_Concept)
    WITH [ie, b, wip, ta, sop, mbp, bp, mame, fol, fil, chme, met, caen] AS ConIES
    UNWIND ConIES AS conIES

    MERGE (conIES)-[riesrv:intellecutal_entity_has_recent_version {cardinality: "exactly 1"}]->(conIES)
    MERGE (conIES)-[riesnv:intellecutal_entity_has_next_version {cardinality: "maximal 1"}]->(conIES)
    MERGE (conIES)-[riespv:intellecutal_entity_has_previous_version {cardinality: "maximal 1"}]->(conIES)
    MERGE (conIES)-[riesov:intellecutal_entity_has_old_version]->(conIES)
    """

    queryRelationAbstractIntellectualEntityComponent = """
    //Relation Component <-> IntellecutalEntity

    //Concepts IntellecutalEntity
    MATCH (ie:IntellectualEntity_Concept)
    MATCH (b:BlogPost_Concept)
    MATCH (wip:WikiPage_Concept)
    MATCH (ta:Task_Concept)
    MATCH (sop:SocialProfile_Concept)
    MATCH (mbp:MicroblogPost_Concept)
    MATCH (bp:BoardPost_Concept)
    MATCH (mame:MailMessage_Concept)
    MATCH (fol:Folder_Concept)
    MATCH (fil:File_Concept)
    MATCH (chme:ChatMessage_Concept)
    MATCH (met:Meeting_Concept)
    MATCH (caen:CalendarEntry_Concept)
    //Collect Concepts IntellctualEntity
    WITH [ie, b, wip, ta, sop, mbp, bp, mame, fol, fil, chme, met, caen] AS ConIEC
    UNWIND ConIEC AS conIEC
    //Concepts Components
    MATCH (foll:Follow_Concept)
    MATCH (scm:SimpleComponent_Concept)
    MATCH (like:Like_Concept)
    MATCH (rea:Reaction_Concept)
    MATCH (subs:Subscription_Concept)
    MATCH (tag:Tag_Concept)
    MATCH (vote:Vote_Concept)
    MATCH (itcm:IntellectualComponent_Concept)
    MATCH (att:Attachment_Concept)
    MATCH (comm:Comment_Concept)

    //Relation Concepts SimpleComponent
    MERGE (scm)-[rcoiescm:component_of_intellectual_entity]->(conIEC)
    MERGE (conIEC)-[riehcscm:intellectual_entity_has_component]->(scm)
    MERGE (foll)-[rcoiefoll:component_of_intellectual_entity]->(conIEC)
    MERGE (conIEC)-[riehcfoll:intellectual_entity_has_component]->(foll)
    MERGE (like)-[rcoielike:component_of_intellectual_entity]->(conIEC)
    MERGE (conIEC)-[riehclike:intellectual_entity_has_component]->(like)
    MERGE (rea)-[rcoierea:component_of_intellectual_entity]->(conIEC)
    MERGE (conIEC)-[riehcrea:intellectual_entity_has_component]->(rea)
    MERGE (subs)-[rcoiesubs:component_of_intellectual_entity]->(conIEC)
    MERGE (conIEC)-[riehcsubs:intellectual_entity_has_component]->(subs)
    MERGE (tag)-[rcoietag:component_of_intellectual_entity]->(conIEC)
    MERGE (conIEC)-[riehctag:intellectual_entity_has_component]->(tag)
    MERGE (vote)-[rcoievote:component_of_intellectual_entity]->(conIEC)
    MERGE (conIEC)-[riehcvote:intellectual_entity_has_component]->(vote)

    //Relation Concepts IntellecutalComponent
    MERGE (itcm)-[rcoieitcm:component_of_intellectual_entity]->(conIEC)
    MERGE (conIEC)-[riehcitcm:intellectual_entity_has_component]->(itcm)
    MERGE (att)-[rcoieatt:component_of_intellectual_entity]->(conIEC)
    MERGE (conIEC)-[riehcatt:intellectual_entity_has_component]->(att)
    MERGE (comm)-[rcoiecomm:component_of_intellectual_entity]->(conIEC)
    MERGE (conIEC)-[riehccomm:intellectual_entity_has_component]->(comm)
    """
    queryRelationAbstractIntellectualEntityContainerChilds = """
    //Relations IntellecutalEntity <-> Container + Childs
    //Main Relation
    MATCH (ie:IntellectualEntity_Concept)
    MATCH (co:Container_Concept)
    MERGE (ie)-[riecic:intellectual_entity_contained_in_container {cardinality: "exactly 1"}]->(co)
    MERGE (co)-[rccie:container_contains_intellectual_entity]->(ie)
    //CalendarEntry <-> Calendar
    WITH [] AS GoOn
    MATCH (caen:CalendarEntry_Concept)
    MATCH (cal:Calendar_Concept)
    MERGE (caen)-[rcecic:calendar_entry_contained_in_calendar {cardinality: "exactly 1"}]->(cal)
    MERGE (cal)-[rccce:calendar_contains_calendar_entry]->(caen)
    //Meeting <-> MeetingContainer
    WITH [] AS GoOn
    MATCH (met:Meeting_Concept)
    MATCH (meco:MeetingContainer_Concept)
    MERGE (met)-[rmcimc:meeting_contained_in_meeting_container {cardinality: "exactly 1"}]->(meco)
    MERGE (meco)-[rmccm:meeting_container_contains_meeting]->(met)
    //ChatMessage <-> ChatChannel
    WITH [] AS GoOn
    MATCH (chme:ChatMessage_Concept)
    MATCH (chach:ChatChannel_Concept)
    MERGE (chme)-[rcmcicc:chat_message_contained_in_chat_channel {cardinality: "exactly 1"}]->(chach)
    MERGE (chach)-[rccccm:chat_channel_contains_chat_message]->(chme)
    //File/Folder <-> FileLirary
    WITH [] AS GoOn
    MATCH (fil:File_Concept)
    MATCH (fol:Folder_Concept)
    MATCH (fili:FileLibrary_Concept)
    MERGE (fil)-[rfcifl:file_contained_in_file_library {cardinality: "exactly 1"}]->(fili)
    MERGE (fil)-[rfcif:file_contained_in_folder]->(fol)
    MERGE (fol)-[rfcifll:folder_contained_in_file_library {cardinality: "exactly 1"}]->(fili)
    MERGE (fol)-[rfcf:folder_contains_file]->(fil)
    MERGE (fol)-[rfhp:folder_has_parent {cardinality: "maximal 1"}]-(fol)
    MERGE (fol)-[rfhc:folder_has_child]->(fol)
    MERGE (fili)-[rflcf:file_library_contains_file]->(fil)
    MERGE (fili)-[rflcfo:file_library_contains_folder]->(fol)
    //MailMessage <-> MailContainer
    WITH [] AS GoOn
    MATCH (mame:MailMessage_Concept)
    MATCH (maco:MailContainer_Concept)
    MERGE (mame)-[rmmcimc:mail_message_contained_in_mail_container{cardinality: "exactly 1"}]->(maco)
    MERGE (maco)-[rmccmm:mail_container_contains_mail_message]->(mame)
    //BoardPost <-> MessageBoard
    WITH [] AS GoOn
    MATCH (bp:BoardPost_Concept)
    MATCH (mebo:MessageBoard_Concept)
    MERGE (bp)-[rbpcimb:board_post_contained_in_message_board {cardinality: "exactly 1"}]->(mebo)
    MERGE (mebo)-[rmbcbp:message_board_contains_board_post]->(bp)
    //MicroblogPost <-> Mircoblog
    WITH [] AS GoOn
    MATCH (mbp:MicroblogPost_Concept)
    MATCH (mibl:Microblog_Concept)
    MERGE (mbp)-[rmpcim:microblog_post_contained_in_microblog {cardinality: "exactly 1"}]->(mibl)
    MERGE (mibl)-[rmcmp:microblog_contains_microblog_post]->(mbp)
    //SocialProfile <-> SocialProfileContainer
    WITH [] AS GoOn
    MATCH (sop:SocialProfile_Concept)
    MATCH (sprco:SocialProfileContainer_Concept)
    MERGE (sop)-[rcpcispc:social_profile_contained_in_social_profile_container {cardinality: "exactly 1"}]->(sprco)
    MERGE (sprco)-[rspccsp:social_profile_container_contains_social_profile]->(sop)
    // Task <-> TaskContainer + Task
    WITH [] AS GoOn
    MATCH (ta:Task_Concept)
    MATCH (taco:TaskContainer_Concept)
    MERGE (ta)-[rtcitc:task_contained_in_task_container {cardinality: "exactly 1"}]->(taco)
    MERGE (taco)-[rtcct:task_container_contains_task]->(ta)
    MERGE (ta)-[rthp:task_has_parent {cardinality: "maximal 1"}]->(ta)
    MERGE (ta)-[rthc:task_has_child]->(ta)
    //BlogPost <-> Weblog
    WITH [] AS GoOn
    MATCH (bp:BlogPost_Concept)
    MATCH (wb:Weblog_Concept)
    MERGE (bp)-[rbpciw:blog_post_contained_in_weblog {cardinality: "exactly 1"}]->(wb)
    MERGE (wb)-[rwcbp:weblog_contains_blog_post]->(bp)
    // WikiPage <-> Wiki + WikiPage 
    WITH [] AS GoOn
    MATCH (wip:WikiPage_Concept)
    MATCH (wi:Wiki_Concept)
    MERGE (wip)-[rwpciw:wiki_page_contained_in_wiki {cardinality: "exactly 1"}]->(wi)
    MERGE (wi)-[rwcwp:wiki_contains_wiki_page]->(wip)
    MERGE (wip)-[rwphp:wiki_page_has_parent {cardinality: "maximal 1"}]->(wip)
    MERGE (wip)-[rwphc:wiki_page_has_child]-> (wip)
    """
    queryRelationAbstractSimpleComponentIntellectualComponent = """
    //Abstract Relation SimpleComponent <-> IntellectualComponent

    //Concepts SimpleComponents
    MATCH (foll:Follow_Concept)
    MATCH (scm:SimpleComponent_Concept)
    MATCH (like:Like_Concept)
    MATCH (rea:Reaction_Concept)
    MATCH (subs:Subscription_Concept)
    MATCH (tag:Tag_Concept)
    MATCH (vote:Vote_Concept)
    WITH [scm, foll, like, rea, subs, tag, vote] AS ConICHSC
    UNWIND ConICHSC AS conICHSC

    //Concepts IntellecutalComponent
    MATCH (itcm:IntellectualComponent_Concept)
    MATCH (att:Attachment_Concept)
    MATCH (comm:Comment_Concept)

    //MERGE Relations
    MERGE (itcm)-[richscitcm:intellectual_component_has_simple_component]->(conICHSC)
    MERGE (conICHSC)-[rscoicitcm:simple_component_of_intellectual_component {cardinality: "maximal 1"}]->(itcm)

    MERGE (att)-[richscatt:intellectual_component_has_simple_component]->(conICHSC)
    MERGE (conICHSC)-[rscoicatt:simple_component_of_intellectual_component {cardinality: "maximal 1"}]->(att)

    MERGE (comm)-[richsccomm:intellectual_component_has_simple_component]->(conICHSC)
    MERGE (conICHSC)-[rscoiccomm:simple_component_of_intellectual_component {cardinality: "maximal 1"}]->(comm)
    """

    queryRelationAbstractSocialDocumentContainer = """
    //MATCH (sd:SocialDocument_Concept)
    MATCH (con:Container_Concept)
    MATCH (cal:Calendar_Concept)
    MATCH (meco:MeetingContainer_Concept)
    MATCH (chach:ChatChannel_Concept)
    MATCH (fili:FileLibrary_Concept)
    MATCH (maco:MailContainer_Concept)
    MATCH (mebo:MessageBoard_Concept)
    MATCH (miblo:Microblog_Concept)
    MATCH (spc:SocialProfileContainer_Concept)
    MATCH (taco:TaskContainer_Concept)
    MATCH (web:Weblog_Concept)
    MATCH (wi:Wiki_Concept)
    WITH [con, cal, meco, chach,  fili, maco, mebo, miblo,spc, taco, web, wi] AS Consdcic
    UNWIND Consdcic AS consdcic
    MATCH (sd:SocialDocument_Concept)
    MERGE (sd)-[rsdcic:social_document_contained_in_container]->(consdcic)
    MERGE (consdcic)-[rccsd:container_contains_social_document]->(sd)
    """

    queryRelationAbstractSocialDocumentItem = """
    //Concepts Abstract
    MATCH (it:Item_Concept)
    MATCH (cm:Component_Concept)
    MATCH (scm:SimpleComponent_Concept)
    MATCH (itcm:IntellectualComponent_Concept)
    MATCH (ie:IntellectualEntity_Concept)

    //Concepts IntellecutalEntity
    MATCH (b:BlogPost_Concept)
    MATCH (wip:WikiPage_Concept)
    MATCH (ta:Task_Concept)
    MATCH (sop:SocialProfile_Concept)
    MATCH (mbp:MicroblogPost_Concept)
    MATCH (bp:BoardPost_Concept)
    MATCH (mame:MailMessage_Concept)
    MATCH (fol:Folder_Concept)
    MATCH (fil:File_Concept)
    MATCH (chme:ChatMessage_Concept)
    MATCH (met:Meeting_Concept)
    MATCH (caen:CalendarEntry_Concept)

    //Concepts SimpleComponent
    MATCH  (foll:Follow_Concept)
    MATCH  (like:Like_Concept)
    MATCH  (rea:Reaction_Concept)
    MATCH  (subs:Subscription_Concept)
    MATCH  (tag:Tag_Concept)
    MATCH  (vote:Vote_Concept)

    //Concepts IntellcutalComponent
    MATCH  (att:Attachment_Concept)
    MATCH  (comm:Comment_Concept)
    //Realtions 
    WITH [it, cm, scm, itcm, ie, b, wip, ta, sop, mbp, bp, mame, fol, fil, chme, met, caen, foll, like, rea, subs, tag, vote, att, comm] AS ConSDCI
    UNWIND ConSDCI AS conSDCI 
    MATCH (sd:SocialDocument_Concept)
    MERGE (sd)-[rsdci:social_document_contains_item]->(conSDCI)
    MERGE (conSDCI)-[ricisd:item_contained_in_social_document]->(sd)
    """
    queryRelationAbstractSystemSpaceDigitalWorkspace = """
    MATCH (sy:System_Concept)
    MATCH (dw:DigitalWorkspace_Concept)
    MATCH (co:Container_Concept)
    //Concept Space
    MATCH (spc:Space_Concept)
    MATCH (gws:GroupWorkspace_Concept)
    MATCH (op:OrganisationalPlatform_Concept)
    MATCH (us:UserWorkspace_Concept)
    //Relation System_Concept <-> Space_Concept
    MERGE (sy)-[rscs:system_contains_space]->(spc)
    MERGE (spc)-[rscis:space_contained_in_system {cardinality: "exactly 1"}]->(sy)
    //Relation System_Concept <-> DigitalWorspace_Concept
    MERGE (sy)-[rscidw:system_contained_in_digital_workspace]->(dw)
    MERGE (dw)-[rdwcs:digital_workspace_contains_system]->(sy)
    //Relation Container_Concept <-> Space_Concept
    MERGE (co)-[rccis:container_contained_in_space {cardinality: "exactly 1"}]->(spc)
    MERGE (spc)-[rscc:space_contains_container]->(co)

    //VERERBUNGEN
    //System_Concept <-> Space_Concept Childs
    //UNWIND
    WITH [gws, op, us, spc] AS ConSP 
    UNWIND ConSP as conSP
    MATCH (sy:System_Concept)
    MERGE (sy)-[rscs:system_contains_space]->(conSP)
    MERGE (conSP)-[rscis:space_contained_in_system {cardinality: "exactly 1"}]->(sy)
    """

    queryRelationsAbstractIntellecutalComponentSelf = """
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
    MERGE (conICS)-[richrv:intellectual_component_has_recent_version {cardinality: "exactly 1"}]->(conICS)
    MERGE (conICS)-[richnv:intellectual_component_has_next_version]->(conICS)
    MERGE (conICS)-[richov:intellectual_component_has_old_version]->(conICS)
    MERGE (conICS)-[richpv:intellectual_component_has_previous_version]->(conICS)
    """
    graph.execute_write_query(queryAbstractStructureA, "neo4j")
    graph.execute_write_query(queryAbstractStructureB, "neo4j")
    graph.execute_write_query(queryAbstractStructureC, "neo4j")

    graph.execute_write_query(queryRelationAbstractAccountItemIntellectualEnity, "neo4j")
    graph.execute_write_query(queryRelationAbstractAccountYellow, "neo4j")
    graph.execute_write_query(queryRelationAbstractCollection, "neo4j")
    graph.execute_write_query(queryRelationAbstractContainerSpace, "neo4j")
    graph.execute_write_query(queryRelationAbstractIntellectualEntitySelf, "neo4j")
    graph.execute_write_query(queryRelationAbstractIntellectualEntityComponent, "neo4j")
    graph.execute_write_query(queryRelationAbstractIntellectualEntityContainerChilds, "neo4j")
    graph.execute_write_query(queryRelationAbstractSimpleComponentIntellectualComponent, "neo4j")
    graph.execute_write_query(queryRelationAbstractSocialDocumentContainer, "neo4j")
    graph.execute_write_query(queryRelationAbstractSocialDocumentItem, "neo4j")
    graph.execute_write_query(queryRelationAbstractSystemSpaceDigitalWorkspace, "neo4j")
    graph.execute_write_query(queryRelationsAbstractIntellecutalComponentSelf, "neo4j")

    ("ProcessEvent finished --- %s seconds ---" % (time.time() - start_time))
    logging.info(("Process finished --- %s seconds ---" % (time.time() - start_time)))

#Main Method
if __name__ == "__main__":
    importingAbstractNodes()
