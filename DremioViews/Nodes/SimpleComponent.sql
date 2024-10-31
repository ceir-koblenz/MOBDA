//Follow
//"MOBDA_Datastore".Nodes.Follow."Uniconnect_Node_Follow_BoardPost"
SELECT UUID, CREATED, TOPICID, FORUMID FROM "Uniconnect_forum".FORUM."DF_SUBSCRIPTION"

//"MOBDA_Datastore".Nodes.Follow."Uniconnect_Node_Follow_File"
SELECT CONCAT(hexedToID(LOWER(HEX(USER_ID))), CONCAT('-', hexedToID(LOWER(HEX(MEDIA_ID))))) as FOLLOW_ID, CREATE_DATE FROM "Uniconnect_files"."FILES"."MEDIA_NOTIFICATION"

//"MOBDA_Datastore".Nodes.Follow."Uniconnect_Node_Follow_Folder"
SELECT CONCAT(hexedToID(LOWER(HEX(USER_ID))), CONCAT('-', hexedToID(LOWER(HEX(COLLECTION_ID))))) as FOLLOW_ID, CREATE_DATE FROM "Uniconnect_files"."FILES"."COLLECTION_NOTIFICATION"

//"MOBDA_Datastore".Nodes.Follow."Uniconnect_Node_Follow_SocialProfile"
SELECT COMM_FOLLOW_ID FROM "Uniconnect_homepage".HOMEPAGE."NR_COMM_FOLLOW"

//"MOBDA_Datastore".Nodes.Follow."Uniconnect_Node_Follow_Task"
SELECT NMEMBERUUID, CREATED FROM "Uniconnect_opnact".ACTIVITIES."OA_NODEMEMBER"
WHERE FOLLOWING = 1

//"MOBDA_Datastore".Nodes.Follow."Uniconnect_Node_Follow_WikiPage"
SELECT CONCAT(hexedToID(LOWER(HEX(USER_ID))), CONCAT('-', hexedToID(LOWER(HEX(MEDIA_ID))))) as FOLLOW_ID, CREATE_DATE FROM "Uniconnect_wikis".WIKIS."MEDIA_NOTIFICATION"

//Like
//"MOBDA_Datastore".Nodes."Like"."Uniconnect_Node_Like_BlogPost"
SELECT CONCAT(USERID, CONCAT('-',ENTRYID)) as LIKE_ID, RATETIME  FROM "Uniconnect_blogs".BLOGS."ROLLER_WEBLOGENTRY_RATING"

//"MOBDA_Datastore".Nodes."Like"."Uniconnect_Node_Like_BlogPost_Comment"
SELECT CONCAT(USERID, CONCAT('-', COMMENTID)) as LIKE_ID, RATETIME FROM "Uniconnect_blogs".BLOGS."ROLLER_COMMENT_RATING"

//"MOBDA_Datastore".Nodes."Like"."Uniconnect_Node_Like_BoardPost"
SELECT lik.UUID, lik.CREATED FROM "Uniconnect_forum".FORUM."DF_RECOMMENDATION" as lik JOIN "Uniconnect_forum".FORUM."DF_NODE" as node ON lik.NODEID = node.NODEUUID
WHERE node.NODETYPE = 'forum/topic'

//"MOBDA_Datastore".Nodes."Like"."Uniconnect_Node_Like_BoardPost_Comment"
SELECT  lik.UUID, lik.CREATED 
FROM "Uniconnect_forum".FORUM."DF_RECOMMENDATION" as lik JOIN "Uniconnect_forum".FORUM."DF_NODE" as node ON lik.NODEID = node.NODEUUID
WHERE node.NODETYPE = 'forum/reply'

//"MOBDA_Datastore".Nodes."Like"."Uniconnect_Node_Like_File"
SELECT CONCAT(hexedToID(LOWER(HEX(USER_ID))), CONCAT('-', hexedToID(LOWER(HEX(MEDIA_ID))))) as LIKE_ID, CREATE_DATE FROM "Uniconnect_files"."FILES"."MEDIA_RECOMMEND"

"MOBDA_Datastore".Nodes."Like"."Uniconnect_Node_Like_MicroblogPost"
SELECT lik.RECOMMENDATION_ID, lik.CREATION_DATE,lik.RECOMMENDER_ID, lik.ITEM_ID FROM "Uniconnect_homepage".HOMEPAGE."BOARD_RECOMMENDATIONS" as lik JOIN "Uniconnect_homepage".HOMEPAGE."BOARD_ENTRIES"as entry ON entry.ITEM_ID = lik.ITEM_ID
WHERE entry.CATEGORY_TYPE = 3

//"MOBDA_Datastore".Nodes."Like"."Uniconnect_Node_Like_MicroblogPost_Comment"
SELECT lik.RECOMMENDATION_ID, lik.CREATION_DATE 
FROM "Uniconnect_homepage".HOMEPAGE."BOARD_RECOMMENDATIONS" as lik JOIN "Uniconnect_homepage".HOMEPAGE."BOARD_COMMENTS" as com ON lik.ITEM_ID = com.ITEM_ID JOIN "Uniconnect_homepage".HOMEPAGE."BOARD_ENTRIES" as entry ON entry.ENTRY_ID = com.ENTRY_ID
WHERE entry.CATEGORY_TYPE = 3

//"MOBDA_Datastore".Nodes."Like"."Uniconnect_Node_Like_SocialProfile_Comment"
SELECT likes.recommendation_id, likes.creation_date
FROM (SELECT item_id, entry_id FROM "Uniconnect_homepage".HOMEPAGE."BOARD_ENTRIES" 
	WHERE category_type = 5
		UNION
	SELECT bCom.item_id, bCom.entry_id 
    FROM "Uniconnect_homepage".HOMEPAGE."BOARD_COMMENTS" AS bCom) AS socPComments
JOIN "Uniconnect_homepage".HOMEPAGE."BOARD_RECOMMENDATIONS" AS likes ON likes.item_id = socPComments.item_id

//"MOBDA_Datastore".Nodes."Like"."Uniconnect_Node_Like_SocialProfile_Comment_Attachment"
SELECT DISTINCT likes.recommendation_id, LIKES.creation_date
FROM (SELECT item_id, entry_id FROM "Uniconnect_homepage".HOMEPAGE."BOARD_ENTRIES" 
	WHERE category_type = 5 
		UNION
	SELECT bCom.item_id, bCom.entry_id FROM "Uniconnect_homepage".HOMEPAGE."BOARD_COMMENTS" AS bCom) 
	AS socPComments
JOIN "Uniconnect_homepage".HOMEPAGE."BOARD_OBJECT_REFERENCE" AS ATTACH ON ATTACH.ITEM_ID = socPComments.entry_id
JOIN "Uniconnect_homepage".HOMEPAGE."BOARD_RECOMMENDATIONS" AS likes ON likes.item_id = ATTACH.item_id

//"MOBDA_Datastore".Nodes."Like"."Uniconnect_Node_Like_WikiPage"
SELECT CONCAT(hexedToID(LOWER(HEX(USER_ID))), CONCAT('-', hexedToID(LOWER(HEX(MEDIA_ID))))) as LIKE_ID, CREATE_DATE FROM "Uniconnect_wikis".WIKIS."MEDIA_RECOMMEND"

//Tag
//"MOBDA_Datastore".Nodes.Tag."Uniconnect_Node_Tag_BlogPost"
SELECT ID, NAME, "TIME" FROM "Uniconnect_blogs".BLOGS."ROLLER_WEBLOGENTRYTAG"

//"MOBDA_Datastore".Nodes.Tag."Uniconnect_Node_Tag_BoardPost"
SELECT TAGUUID, NAME, CREATED FROM "Uniconnect_forum".FORUM."DF_TAG"

//"MOBDA_Datastore".Nodes.Tag."Uniconnect_Node_Tag_File"
SELECT DISTINCT CONCAT((hexedToID(LOWER(HEX(mediatag.OWNER_user_id)))), CONCAT('-', (hexedToID(LOWER(HEX(mediatag.tag_id)))))) as id, tag.tag, tag.create_date 
FROM "Uniconnect_files"."FILES".TAG as tag
JOIN Uniconnect_files."FILES".MEDIA_TO_TAG as mediatag ON tag.id = mediatag.TAG_ID

//"MOBDA_Datastore".Nodes.Tag."Uniconnect_Node_Tag_SocialProfile"
SELECT PROF_TAG_ID, PROF_TAG FROM "Uniconnect_peopledb".EMPINST."PEOPLE_TAG"

//"MOBDA_Datastore".Nodes.Tag."Uniconnect_Node_Tag_Task"
SELECT TAGUUID, NAME, NODEUUID, OWNER FROM "Uniconnect_opnact".ACTIVITIES."OA_TAG"

//"MOBDA_Datastore".Nodes.Tag."Uniconnect_Node_Tag_WikiPage"
SELECT DISTINCT CONCAT((hexedToID(LOWER(HEX(mediatag.OWNER_user_id)))), CONCAT('-', (hexedToID(LOWER(HEX(mediatag.tag_id)))))) as id, tag.tag, tag.create_date 
FROM "Uniconnect_wikis".WIKIS.TAG as tag
JOIN Uniconnect_wikis."WIKIS".MEDIA_TO_TAG as mediatag ON tag.id = mediatag.TAG_ID