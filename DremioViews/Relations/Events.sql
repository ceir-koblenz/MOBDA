//"MOBDA_Datastore".Relations.Events."Uniconnect_Relation_Events_MicroblogPost_event_affects_item"
SELECT "Event ID" as eventid, "IntellectualEntity ID" as mblogid, "IntellectualEntity Type"
FROM CLog.public.clogTest
WHERE "IntellectualEntity Type" = 'MicroblogPost'
AND "System Instance" = 'UniConnect'

//"MOBDA_Datastore".Relations.Events."Uniconnect_Relation_Events_SocialProfile_event_affects_item"
SELECT "Event ID" as eventid, "IntellectualEntity ID" as sprofileid, "IntellectualEntity Type"
FROM CLog.public.clogTest
WHERE "IntellectualEntity Type" = 'SocialProfile'
AND "System Instance" = 'UniConnect'

//"MOBDA_Datastore".Relations.Events."Uniconnect_Relation_Events_Task_event_affects_item"
SELECT "Event ID" as eventid, "IntellectualEntity ID" as taskid, "IntellectualEntity Type"
FROM CLog.public.clogTest
WHERE "IntellectualEntity Type" = 'Task'
AND "System Instance" = 'UniConnect'
AND "IntellectualEntity ID" <> 'ACTIVITIES'

//"MOBDA_Datastore".Relations.Events."Uniconnect_Relation_Events_WikiPage_event_affects_item"
SELECT "Event ID" as eventid, "IntellectualEntity ID" as wikiid, "IntellectualEntity Type"
FROM CLog.public.clogTest
WHERE "IntellectualEntity Type" = 'WikiPage'
AND "System Instance" = 'UniConnect'

//"MOBDA_Datastore".Relations.Events."Uniconnect_Relation_Events_Attachment_event_affects_item"
SELECT clog."Event ID" as eventid, clog."IntellectualComponent ID" as attid, clog."IntellectualComponent Type"
FROM CLog.public.clogTest as clog
WHERE clog."IntellectualComponent Type" = 'Attachment' AND clog."System Instance" = 'UniConnect'

//"MOBDA_Datastore".Relations.Events."Uniconnect_Relation_Events_BlogPost_event_affects_item"
SELECT clog."IntellectualEntity ID" as itemid, clog."IntellectualEntity Type", clog."Event ID" as eventid
FROM CLog.public.clogTest as clog
WHERE clog."IntellectualEntity Type" = 'BlogPost' 
AND clog."IntellectualEntity ID" <> 'BLOGS'  
AND clog."System Instance" = 'UniConnect'

//"MOBDA_Datastore".Relations.Events."Uniconnect_Relation_Events_BoardPost_event_affects_item"
SELECT clog."Event ID" as eventid, clog."IntellectualEntity ID" as boardid, clog."IntellectualEntity Type"
FROM CLog.public.clogTest as clog
WHERE clog."IntellectualEntity Type" = 'BoardPost'
AND clog."IntellectualEntity ID" <> 'FORUMS'
AND clog."System Instance" = 'UniConnect'

//"MOBDA_Datastore".Relations.Events."Uniconnect_Relation_Events_Comment_event_affects_item"
SELECT clog."Event ID" as eventid, clog."IntellectualComponent ID" as comid, clog."IntellectualComponent Type"
FROM CLog.public.clogTest as clog
WHERE clog."IntellectualComponent Type" = 'Comment'
AND clog."System Instance" = 'UniConnect'

//"MOBDA_Datastore".Relations.Events."Uniconnect_Relation_Events_File_event_affects_item"
SELECT "Event ID" as eventid,"IntellectualEntity ID" as fileid,"IntellectualEntity Type"
FROM CLog.public.clogTest
WHERE "IntellectualEntity Type" = 'File'
AND "System Instance" = 'UniConnect'

//"MOBDA_Datastore".Relations.Events."Uniconnect_Relation_Events_Folder_event_affects_item"
SELECT "Event ID" as eventid, "IntellectualEntity ID" as folderid, "IntellectualEntity Type"
FROM CLog.public.clogTest
WHERE "IntellectualEntity Type" = 'Folder'
AND "System Instance" = 'UniConnect'

//"MOBDA_Datastore".Relations.Events."Uniconnect_Relation_Events_Follow_event_affects_item"
SELECT "Event ID" as eventid, "SimpleComponent ID" as followid, "SimpleComponent Type"
FROM CLog.public.clogTest
WHERE "SimpleComponent Type" = 'Follow'
AND "System Instance" = 'UniConnect'

//"MOBDA_Datastore".Relations.Events."Uniconnect_Relation_Events_Like_event_affects_item"
SELECT "Event ID" as eventid, "SimpleComponent ID" as likeid, "SimpleComponent Type"
FROM CLog.public.clogTest
WHERE "SimpleComponent Type" = 'Like'
AND "System Instance" = 'UniConnect'