//"MOBDA_Datastore".Relations.GroupWorkspaces."Uniconnect_Relation_GroupWorkspace_Filelibrary_space_contains_container"
SELECT gws.COMMUNITY_UUID as workspaceid, hexedToID(LOWER(HEX(filelib.id))) as libid
FROM Uniconnect_files."FILES".LIBRARY as filelib
JOIN Uniconnect_sncomm.SNCOMM.COMMUNITY as gws ON gws.COMMUNITY_UUID = filelib.EXTERNAL_CONTAINER_ID

//"MOBDA_Datastore".Relations.GroupWorkspaces."Uniconnect_Relation_GroupWorkspaces_MessageBoard_space_contains_container"
SELECT grospace.COMMUNITY_UUID as workspaceid, mboard.FORUMUUID as mboardid
FROM "Uniconnect_sncomm".SNCOMM.COMMUNITY as grospace
JOIN Uniconnect_forum.FORUM.DF_NODECOMMMAP as mboard ON mboard.COMMUNITYUUID = grospace.COMMUNITY_UUID

//"MOBDA_Datastore".Relations.GroupWorkspaces."Uniconnect_Relation_GroupWorkspaces_Microblog_space_contains_container"
SELECT gws.COMMUNITY_UUID as workspaceid, mblog.BOARD_CONTAINER_ID mblogid
FROM Uniconnect_sncomm.SNCOMM.COMMUNITY as gws
JOIN Uniconnect_homepage.HOMEPAGE.PERSON as person ON gws.COMMUNITY_UUID = person.EXID
JOIN Uniconnect_homepage.HOMEPAGE.BOARD as mblog ON person.PERSON_ID = mblog.BOARD_CONTAINER_ID

//"MOBDA_Datastore".Relations.GroupWorkspaces."Uniconnect_Relation_GroupWorkspaces_TaskContainer_space_contains_container"
SELECT gws.COMMUNITY_UUID as workspaceid, users.objectuuid as tcontainerid
FROM Uniconnect_sncomm.SNCOMM.COMMUNITY as gws
JOIN Uniconnect_opnact.ACTIVITIES.OA_MEMBERPROFILE as usera ON gws.COMMUNITY_UUID = usera.EXID
JOIN (SELECT DISTINCT acl.objectuuid, memberdisp AS subMemberDisp  
        FROM Uniconnect_opnact.ACTIVITIES.OA_ACLENTRY as acl
        JOIN Uniconnect_opnact.ACTIVITIES.OA_MEMBERPROFILE as userb ON acl.memberid = userb.MEMBERID) as users
        ON subMemberDisp = usera.MEMBERDISP
    JOIN (SELECT DISTINCT ACTIVITYUUID 
        FROM Uniconnect_opnact.ACTIVITIES.OA_NODE as tcon
        WHERE NODETYPE = 'activities/task') As tconwithtask
        ON tconwithtask.ACTIVITYUUID = users.OBJECTUUID

//"MOBDA_Datastore".Relations.GroupWorkspaces."Uniconnect_Relation_GroupWorkspaces_Wiki_space_contains_container"
SELECT gws.COMMUNITY_UUID as workspaceid, hexedToID(LOWER(HEX(wiki.ID))) as wikiid
FROM Uniconnect_wikis.WIKIS.LIBRARY as wiki
JOIN Uniconnect_sncomm.SNCOMM.COMMUNITY as gws ON wiki.EXTERNAL_CONTAINER_ID = gws.COMMUNITY_UUID

//"MOBDA_Datastore".Relations.GroupWorkspaces."Uniconnect_Relations_GroupWorkspaces_Weblog_space_contains_container"
SELECT gws.COMMUNITY_UUID as workspaceid, weblog.id as weblogid
FROM "Uniconnect_blogs".BLOGS.WEBSITE as weblog
JOIN Uniconnect_blogs.BLOGS.WEBSITEASSOC as assoc ON assoc.WEBSITEID = weblog.ID
JOIN Uniconnect_sncomm.SNCOMM.COMMUNITY as gws ON gws.COMMUNITY_UUID = assoc.ASSOCID