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