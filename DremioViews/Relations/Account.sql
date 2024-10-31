//Account SQL queries

//"MOBDA_Datastore".Relations.Account."Uniconnect_Relation_Account_AttachmentBoardPost_account_created_item"
SELECT node.nodeuuid as id, acc.prof_guid as accountid, mem.exid
FROM "Uniconnect_forum".FORUM."DF_NODE" as node JOIN "Uniconnect_forum".FORUM."DF_MEMBERPROFILE" as mem ON node.CREATEDBY = mem.MEMBERID
JOIN Uniconnect_peopledb.EMPINST.EMPLOYEE as acc ON mem.EXID = acc.PROF_GUID WHERE node.NODETYPE = 'application/field'

//"MOBDA_Datastore".Relations.Account."Uniconnect_Relation_Account_AttachmentSocialProfileComment_account_created_item"
SELECT acc.prof_guid as accountid, attach.OBJECT_ID as id, person.EXID
FROM (
    SELECT ENTRY_ID
    FROM Uniconnect_homepage.HOMEPAGE.BOARD_ENTRIES as entry
    WHERE entry.CATEGORY_TYPE = 5
        UNION
    SELECT ENTRY_ID
    FROM Uniconnect_homepage.HOMEPAGE.BOARD_COMMENTS as com
    ) as soc
JOIN "Uniconnect_homepage".HOMEPAGE."BOARD_OBJECT_REFERENCE" as attach ON attach.ITEM_ID = soc.entry_id
JOIN Uniconnect_homepage.HOMEPAGE.PERSON as person ON person.PERSON_ID = attach.AUTHOR_ID
JOIN Uniconnect_peopledb.EMPINST.EMPLOYEE as acc ON acc.prof_guid = person.EXID

//"MOBDA_Datastore".Relations.Account."Uniconnect_Relation_Account_AttachmentTask_account_created_item"
SELECT acc.prof_guid as accountid, task.nodeuuid as id, tuser.exid
FROM Uniconnect_opnact.ACTIVITIES.OA_NODE as task
JOIN Uniconnect_opnact.ACTIVITIES.OA_MEMBERPROFILE as tuser
ON tuser.MEMBERID = task.CREATEDBY
JOIN Uniconnect_peopledb.EMPINST.EMPLOYEE as acc
ON acc.prof_guid = tuser.EXID
WHERE task.NODETYPE = 'application/activityfield'

//"MOBDA_Datastore".Relations.Account."Uniconnect_Relation_Account_AttachmentWikiPage_account_created_item"
SELECT acc.prof_guid as accountid, hexedToID(LOWER(HEX(att.ID))) as id , wuser.DIRECTORY_ID
FROM Uniconnect_wikis.WIKIS.MEDIA_ADDITIONAL_FILE as att
JOIN Uniconnect_wikis.WIKIS."USER" as wuser 
ON att.LAST_UPDATE_USER_ID = wuser.ID
JOIN Uniconnect_peopledb.EMPINST.EMPLOYEE as acc
ON acc.prof_guid = wuser.DIRECTORY_ID

//"MOBDA_Datastore".Relations.Account."Uniconnect_Relation_Account_BlogPost_account_created_item"
SELECT blog.id, acc.PROF_GUID, buser.EXTID FROM "Uniconnect_blogs".BLOGS.WEBLOGENTRY as blog
JOIN "Uniconnect_blogs".BLOGS.ROLLERUSER as buser ON blog.USERID = buser.ID
JOIN "Uniconnect_peopledb".EMPINST.EMPLOYEE as acc ON buser.extid = acc.PROF_GUID

//"MOBDA_Datastore".Relations.Account."Uniconnect_Relation_Account_BoardPost_account_created_item"
SELECT board.nodeuuid, acc.prof_guid, bprofile.exid
FROM "Uniconnect_forum".FORUM."DF_NODE" as board
JOIN "Uniconnect_forum".FORUM."DF_MEMBERPROFILE" bprofile ON board.CREATEDBY = bprofile.MEMBERID
JOIN "Uniconnect_peopledb".EMPINST.EMPLOYEE as acc ON acc.prof_guid = bprofile.EXID
WHERE board.nodetype = 'forum/topic'

//"MOBDA_Datastore".Relations.Account."Uniconnect_Relation_Account_CommentBlogPost_account_created_item"
SELECT acc.PROF_GUID as accountid, com.id as id, ruser.extid
FROM Uniconnect_blogs.BLOGS.ROLLER_COMMENT as com
JOIN Uniconnect_blogs.BLOGS.ROLLERUSER as ruser ON com.USERID = ruser.ID
JOIN Uniconnect_peopledb.EMPINST.EMPLOYEE as acc ON acc.PROF_GUID = ruser.EXTID

//"MOBDA_Datastore".Relations.Account."Uniconnect_Relation_Account_CommentBoardPost_account_created_item"
SELECT acc.prof_guid as accountid, node.NODEUUID as id, dfuser.EXID
FROM "Uniconnect_forum".FORUM."DF_NODE" as node
JOIN Uniconnect_forum.FORUM.DF_MEMBERPROFILE as dfuser ON node.CREATEDBY = dfuser.MEMBERID
JOIN Uniconnect_peopledb.EMPINST.EMPLOYEE as acc ON acc.prof_guid = dfuser.EXID
WHERE node.nodetype = 'forum/reply'

//"MOBDA_Datastore".Relations.Account."Uniconnect_Relation_Account_CommentFiles_account_created_item"
SELECT acc.PROF_GUID as accountid, hexedToID(LOWER(HEX(com.ID))) as id, fuser.DIRECTORY_ID
FROM Uniconnect_files."FILES".MEDIA_COMMENT as com
JOIN Uniconnect_files."FILES"."USER" as fuser ON com.OWNER_USER_ID = fuser.ID
JOIN Uniconnect_peopledb.EMPINST.EMPLOYEE as acc ON acc.prof_guid = fuser.DIRECTORY_ID

//"MOBDA_Datastore".Relations.Account."Uniconnect_Relation_Account_CommentMicroblogPost_account_created_item"
SELECT acc.prof_guid as accountid, com.COMMENT_ID as id, person.exid
FROM Uniconnect_homepage.HOMEPAGE.BOARD_COMMENTS as com
JOIN Uniconnect_homepage.HOMEPAGE.BOARD_ENTRIES as entry ON entry.ENTRY_ID = com.ENTRY_ID
JOIN Uniconnect_homepage.HOMEPAGE.PERSON as person ON person.PERSON_ID = com.ACTOR_UUID
JOIN Uniconnect_peopledb.EMPINST.EMPLOYEE as acc ON acc.PROF_GUID = person.EXID
WHERE entry.CATEGORY_TYPE = 3

//"MOBDA_Datastore".Relations.Account."Uniconnect_Relation_Account_CommentSocialProfileComment_account_created_item"
SELECT mainacc.prof_guid as accountid, main.ENTRY_ID as id, mainuser.EXID
FROM Uniconnect_homepage.HOMEPAGE.BOARD_ENTRIES as main
JOIN Uniconnect_homepage.HOMEPAGE.PERSON as mainuser ON main.ACTOR_UUID = mainuser.PERSON_ID
JOIN Uniconnect_peopledb.EMPINST.EMPLOYEE as mainacc ON mainuser.EXID = mainacc.PROF_GUID
WHERE main.CATEGORY_TYPE = 5
UNION
SELECT comacc.prof_guid as accountid, com.COMMENT_ID as id,  comuser.exid
FROM Uniconnect_homepage.HOMEPAGE.BOARD_COMMENTS as com
JOIN Uniconnect_homepage.HOMEPAGE.BOARD_ENTRIES as comentry ON com.ENTRY_ID = comentry.ENTRY_ID
JOIN Uniconnect_homepage.HOMEPAGE.PERSON as comuser ON comentry.ACTOR_UUID = comuser.PERSON_ID
JOIN Uniconnect_peopledb.EMPINST.EMPLOYEE as comacc ON comuser.EXID = comacc.PROF_GUID
WHERE comentry.CATEGORY_TYPE = 5

//"MOBDA_Datastore".Relations.Account."Uniconnect_Relation_Account_CommentTask_account_created_item"
SELECT acc.prof_guid as accountid, node.NODEUUID as id, cuser.exid
FROM Uniconnect_opnact.ACTIVITIES.OA_NODE as node
JOIN Uniconnect_opnact.ACTIVITIES.oa_memberprofile as cuser ON cuser.MEMBERID = node.CREATEDBY
JOIN Uniconnect_peopledb.EMPINST.EMPLOYEE as acc ON acc.prof_guid = cuser.EXID
WHERE node.nodetype = 'activities/reply'

//"MOBDA_Datastore".Relations.Account."Uniconnect_Relation_Account_CommentWikiPage_account_created_item"
SELECT hexedToID(LOWER(HEX(wikicom.id))) as id, acc.PROF_GUID as accountid,  wuser.DIRECTORY_ID
FROM "Uniconnect_wikis".WIKIS."MEDIA_COMMENT" as wikicom
JOIN Uniconnect_wikis.WIKIS."USER" as wuser ON wuser.id = wikicom.OWNER_USER_ID
JOIN Uniconnect_peopledb.EMPINST.EMPLOYEE as acc ON acc.PROF_GUID = wuser.DIRECTORY_ID

//"MOBDA_Datastore".Relations.Account."Uniconnect_Relation_Account_Event_account_performed_event"
SELECT "Account ID" as prof_guid, "Event ID" as event_id, "System Instance" 
FROM CLog.public.clogTest as clog 
WHERE "System Instance" ='UniConnect'

//"MOBDA_Datastore".Relations.Account."Uniconnect_Relation_Account_File_account_created_item"
SELECT hexedToID(LOWER(HEX(mr.id))) as id, acc.prof_guid, us.directory_id
FROM "Uniconnect_files"."FILES"."MEDIA_REVISION" as mr
JOIN "Uniconnect_files"."FILES".MEDIA as m ON mr.MEDIA_ID = m.ID
JOIN "Uniconnect_files"."FILES"."USER" as us ON us.ID = m.OWNER_USER_ID
JOIN "Uniconnect_peopledb".EMPINST.EMPLOYEE as acc ON acc.PROF_GUID = us.DIRECTORY_ID

//"MOBDA_Datastore".Relations.Account."Uniconnect_Relation_Account_Folder_account_created_item"
SELECT hexedToID(LOWER(HEX(coll.id))) as id, acc.prof_guid, usme.directory_id
FROM "Uniconnect_files"."FILES".COLLECTION as coll
JOIN "Uniconnect_files"."FILES"."USER" as usme ON usme.ID = coll.OWNER_USER_ID 
JOIN "Uniconnect_peopledb".EMPINST.EMPLOYEE as acc ON acc.prof_guid = usme.DIRECTORY_ID

//"MOBDA_Datastore".Relations.Account."Uniconnect_Relation_Account_LikeBoardPost_account_creatded_item"
SELECT acc.PROF_GUID as accountid, blike.uuid as id, buser.EXID
FROM Uniconnect_forum.FORUM.DF_NODE as forum
JOIN Uniconnect_forum.FORUM.DF_RECOMMENDATION as blike ON forum.NODEUUID = blike.NODEID
JOIN Uniconnect_forum.FORUM.DF_MEMBERPROFILE as buser ON buser.MEMBERID = blike.CREATEDBY
JOIN Uniconnect_peopledb.EMPINST.EMPLOYEE as acc ON acc.PROF_GUID = buser.EXID
WHERE forum.NODETYPE = 'forum/topic'

//"MOBDA_Datastore".Relations.Account."Uniconnect_Relation_Account_LikeBoardPostComment_account_created_item"
SELECT acc.PROF_GUID as accountid, blike.uuid as id, buser.EXID
FROM Uniconnect_forum.FORUM.DF_NODE as forum
JOIN Uniconnect_forum.FORUM.DF_RECOMMENDATION as blike ON forum.NODEUUID = blike.NODEID
JOIN Uniconnect_forum.FORUM.DF_MEMBERPROFILE as buser ON buser.MEMBERID = blike.CREATEDBY
JOIN Uniconnect_peopledb.EMPINST.EMPLOYEE as acc ON acc.PROF_GUID = buser.EXID
WHERE forum.NODETYPE = 'forum/reply'

//"MOBDA_Datastore".Relations.Account."Uniconnect_Relation_Account_LikeFile_account_created_item"
SELECT CONCAT(hexedToID(LOWER(HEX(USER_ID))), CONCAT('-', hexedToID(LOWER(HEX(MEDIA_ID))))) as id, acc.PROF_GUID as accountid, luser.DIRECTORY_ID
FROM Uniconnect_files."FILES".MEDIA_RECOMMEND as likes
JOIN Uniconnect_files."FILES"."USER" as luser ON likes.user_id = luser.ID
JOIN Uniconnect_peopledb.EMPINST.EMPLOYEE as acc ON acc.prof_guid =luser.DIRECTORY_ID

//"MOBDA_Datastore".Relations.Account."Uniconnect_Relation_Account_LikeMicroblogPost_account_created_item"
SELECT mlike.RECOMMENDATION_ID as id, acc.PROF_GUID as accountid, luser.EXID
FROM Uniconnect_homepage.HOMEPAGE.BOARD_RECOMMENDATIONS as mlike
JOIN Uniconnect_homepage.HOMEPAGE.BOARD_ENTRIES as mblog ON  mlike.ITEM_ID = mblog.ITEM_ID
JOIN "Uniconnect_homepage".HOMEPAGE.PERSON as luser ON luser.person_id = mlike.RECOMMENDER_ID
JOIN Uniconnect_peopledb.EMPINST.EMPLOYEE as acc ON acc.PROF_GUID = luser.EXID
WHERE mblog.CATEGORY_TYPE = 3

//"MOBDA_Datastore".Relations.Account."Uniconnect_Relation_Account_LikeMircoblogPostComment_account_created_item"
SELECT mlike.RECOMMENDATION_ID as id, acc.PROF_GUID as accountid, luser.EXID
FROM Uniconnect_homepage.HOMEPAGE.BOARD_RECOMMENDATIONS as mlike
JOIN Uniconnect_homepage.HOMEPAGE.BOARD_COMMENTS as com ON com.ITEM_ID = mlike.ITEM_ID
JOIN Uniconnect_homepage.HOMEPAGE.BOARD_ENTRIES as mblog ON  com.entry_id = mblog.ENTRY_ID
JOIN "Uniconnect_homepage".HOMEPAGE.PERSON as luser ON luser.person_id = mlike.RECOMMENDER_ID
JOIN Uniconnect_peopledb.EMPINST.EMPLOYEE as acc ON acc.PROF_GUID = luser.EXID
WHERE mblog.CATEGORY_TYPE = 3

//"MOBDA_Datastore".Relations.Account."Uniconnect_Relation_Account_LikeSocialProfileComment_account_created_item"
SELECT likes.recommendation_id AS id, acc.prof_guid as accountid, users.exid
FROM (SELECT entry.item_id, entry.entry_id FROM Uniconnect_homepage.HOMEPAGE.BOARD_ENTRIES as entry 
	WHERE entry.category_type = 5 /*eq: SOURCE = 'PROFILES' */
		UNION
	SELECT bCom.item_id, bCom.entry_id 
    FROM Uniconnect_homepage.HOMEPAGE.BOARD_COMMENTS AS bCom
	) AS com
JOIN Uniconnect_homepage.HOMEPAGE.BOARD_RECOMMENDATIONS AS likes ON likes.item_id = com.item_id
JOIN Uniconnect_homepage.HOMEPAGE.PERSON AS users ON (users.person_id = likes.recommender_id)
JOIN Uniconnect_peopledb.EMPINST.EMPLOYEE as acc ON acc.PROF_GUID = users.EXID

//"MOBDA_Datastore".Relations.Account."Uniconnect_Relation_Account_LikeSocialProifileCommentAttachment_account_created_item"
SELECT likes.recommendation_id AS id, acc.prof_guid as accountid, users.exid
FROM (SELECT entry.item_id, entry.entry_id FROM Uniconnect_homepage.HOMEPAGE.BOARD_ENTRIES as entry 
	WHERE entry.category_type = 5 /*eq: SOURCE = 'PROFILES' */
		UNION
	SELECT bCom.item_id, bCom.entry_id 
    FROM Uniconnect_homepage.HOMEPAGE.BOARD_COMMENTS AS bCom
	) AS com
JOIN Uniconnect_homepage.HOMEPAGE.BOARD_OBJECT_REFERENCE as att ON att.ITEM_ID = com.ENTRY_ID
JOIN Uniconnect_homepage.HOMEPAGE.BOARD_RECOMMENDATIONS AS likes ON likes.item_id = com.item_id
JOIN Uniconnect_homepage.HOMEPAGE.PERSON AS users ON (users.person_id = likes.recommender_id)
JOIN Uniconnect_peopledb.EMPINST.EMPLOYEE as acc ON acc.PROF_GUID = users.EXID

//"MOBDA_Datastore".Relations.Account."Uniconnect_Relation_Account_LikeWikiPage_account_created_item"
SELECT CONCAT(hexedToID(LOWER(HEX(USER_ID))), CONCAT('-', hexedToID(LOWER(HEX(MEDIA_ID))))) as id, acc.PROF_GUID as accountid, luser.DIRECTORY_ID
FROM "Uniconnect_wikis".WIKIS."MEDIA_RECOMMEND" as likes
JOIN Uniconnect_wikis.WIKIS."USER" as luser ON luser.id = likes.USER_ID
JOIN Uniconnect_peopledb.EMPINST.EMPLOYEE as acc ON acc.PROF_GUID = luser.DIRECTORY_ID

//"MOBDA_Datastore".Relations.Account."Uniconnect_Relation_Account_MicroblogPost_account_created_item"
SELECT bentry.entry_id, acc.prof_guid, pers.exid
FROM "Uniconnect_homepage".HOMEPAGE."BOARD_ENTRIES" as bentry
JOIN "Uniconnect_homepage".HOMEPAGE.PERSON as pers ON pers.PERSON_ID = bentry.ACTOR_UUID
JOIN "Uniconnect_peopledb".EMPINST.EMPLOYEE as acc ON acc.prof_guid = pers.exid
WHERE bentry.CATEGORY_TYPE = 3

//"MOBDA_Datastore".Relations.Account."Uniconnect_Relation_Account_Person_account_of_agent"
SELECT acc.PROF_MAIL_LOWER as accountmail, acc.prof_guid as accountid, person.prof_guid as personid, person.PROF_MAIL_LOWER as personmail
FROM "Uniconnect_peopledb".EMPINST.EMPLOYEE as acc
JOIN "Uniconnect_peopledb".EMPINST.EMPLOYEE as person
ON person.PROF_MAIL_LOWER = acc.PROF_MAIL_LOWER

//"MOBDA_Datastore".Relations.Account."Uniconnect_Relation_Account_SocialProfile_account_has_soical_profile"
SELECT social.person_id, acc.prof_guid, social.exid
FROM "Uniconnect_homepage".HOMEPAGE.PERSON social
JOIN "Uniconnect_peopledb".EMPINST.EMPLOYEE as acc ON acc.PROF_GUID = social.EXID
WHERE MEMBER_TYPE = 0

//"MOBDA_Datastore".Relations.Account."Uniconnect_Relation_Account_TagBlogPost_account_created_item"
SELECT acc.PROF_GUID as accountid, tag.id as id, users.extid 
FROM "Uniconnect_blogs".BLOGS."ROLLER_WEBLOGENTRYTAG" as tag
JOIN Uniconnect_blogs.BLOGS.ROLLERUSER as users ON tag.USERID = users.ID
JOIN Uniconnect_peopledb.EMPINST.EMPLOYEE as acc ON acc.PROF_GUID = users.EXTID

//"MOBDA_Datastore".Relations.Account."Uniconnect_Relation_Account_TagBoardPost_account_created_item"
SELECT tag.TAGUUID as id, acc.prof_guid as accountid, users.EXID
FROM Uniconnect_forum.FORUM.DF_TAG as tag
JOIN Uniconnect_forum.FORUM.DF_MEMBERPROFILE as users ON users.MEMBERID = tag.CREATEDBY
JOIN Uniconnect_peopledb.EMPINST.EMPLOYEE as acc ON acc.prof_guid = users.EXID

//"MOBDA_Datastore".Relations.Account."Uniconnect_Relation_Account_TagFile_account_created_item"
SELECT DISTINCT CONCAT((hexedToID(LOWER(HEX(mediatag.OWNER_user_id)))), CONCAT('-', (hexedToID(LOWER(HEX(mediatag.tag_id)))))) as id, acc.prof_guid as accountid, users.DIRECTORY_ID
FROM Uniconnect_files."FILES".MEDIA_TO_TAG as mediatag
JOIN Uniconnect_files."FILES"."USER" as users ON mediatag.OWNER_USER_ID = users.ID
JOIN Uniconnect_peopledb.EMPINST.EMPLOYEE as acc ON acc.prof_guid = users.DIRECTORY_ID

//"MOBDA_Datastore".Relations.Account."Uniconnect_Relation_Account_TagSocialProfile_account_created_item"
SELECT tag.PROF_TAG_ID as id , acc.prof_guid as accountid
FROM Uniconnect_peopledb.EMPINST.PEOPLE_TAG as tag
JOIN Uniconnect_peopledb.EMPINST.EMPLOYEE as acc ON tag.PROF_SOURCE_KEY = acc.PROF_KEY

//"MOBDA_Datastore".Relations.Account."Uniconnect_Relation_Account_TagTask_account_created_item"
SELECT tag.TAGUUID as id, acc.PROF_GUID as accountid, users.EXID
FROM "Uniconnect_opnact".ACTIVITIES."OA_TAG" as tag
JOIN Uniconnect_opnact.ACTIVITIES.OA_MEMBERPROFILE as users ON tag.OWNER = users.MEMBERID
JOIN Uniconnect_peopledb.EMPINST.EMPLOYEE as acc ON acc.PROF_GUID = users.EXID

//"MOBDA_Datastore".Relations.Account."Uniconnect_Relation_Account_TagWikiPage_account_created_item"
SELECT DISTINCT CONCAT((hexedToID(LOWER(HEX(mediatag.OWNER_user_id)))), CONCAT('-', (hexedToID(LOWER(HEX(mediatag.tag_id)))))) as id, acc.PROF_GUID as accountid, users.DIRECTORY_ID
FROM Uniconnect_wikis.WIKIS.TAG AS tag 
JOIN Uniconnect_wikis.WIKIS.media_to_tag AS mediatag  ON tag.ID = MEDIATAG.TAG_ID 
JOIN Uniconnect_wikis.WIKIS."USER" AS users ON users.ID = mediatag.OWNER_USER_ID 
JOIN Uniconnect_peopledb.EMPINST.EMPLOYEE as acc ON acc.PROF_GUID = users.DIRECTORY_ID

//"MOBDA_Datastore".Relations.Account."Uniconnect_Relation_Account_Task_account_created_item"
SELECT node.nodeuuid, acc.prof_guid, mem.exid
FROM "Uniconnect_opnact".ACTIVITIES."OA_NODE" as node
JOIN "Uniconnect_opnact".ACTIVITIES."OA_MEMBERPROFILE" as mem ON mem.MEMBERID = node.CREATEDBY
JOIN "Uniconnect_peopledb".EMPINST.EMPLOYEE as acc ON acc.prof_guid = mem.EXID
WHERE node.NODETYPE = 'activities/task'

//"MOBDA_Datastore".Relations.Account."Uniconnect_Relation_Account_WikiPage_account_created_item"
SELECT hexedToID(LOWER(HEX(mr.ID))) as id, acc.prof_guid, us.DIRECTORY_ID
FROM "Uniconnect_wikis".WIKIS."MEDIA_REVISION" as mr
JOIN "Uniconnect_wikis".WIKIS.MEDIA as m ON m.id = mr.MEDIA_ID
JOIN "Uniconnect_wikis".WIKIS."USER" as us ON us.id = m.OWNER_USER_ID
JOIN"Uniconnect_peopledb".EMPINST.EMPLOYEE as acc ON acc.prof_guid = us.DIRECTORY_ID