//"MOBDA_Datastore".Relations.SocialProfiles."Uniconnect_Relation_SocialProfile_Comment_intellectual_entity_has_component"
SELECT socpro.PERSON_ID as socprofileid, comment.ENTRY_ID as commentid
FROM
(SELECT board.ENTRY_ID, board.CREATION_DATE, board.UPDATE_DATE, board.CONTENT, board.ACTOR_UUID FROM "Uniconnect_homepage".HOMEPAGE."BOARD_ENTRIES" as board
WHERE CATEGORY_TYPE = 5
UNION ALL
SELECT cboard.COMMENT_ID, cboard.CREATION_DATE, cboard.UPDATE_DATE, cboard.CONTENT, cboard.ACTOR_UUID FROM "Uniconnect_homepage".HOMEPAGE."BOARD_COMMENTS" as cboard JOIN "Uniconnect_homepage".HOMEPAGE."BOARD_ENTRIES" as entry ON cboard.ENTRY_ID = entry.ENTRY_ID WHERE entry.CATEGORY_TYPE = 5) as comment
JOIN Uniconnect_homepage.HOMEPAGE.PERSON as socpro ON comment.ACTOR_UUID = socpro.PERSON_ID
WHERE socpro.MEMBER_TYPE = 0

//"MOBDA_Datastore".Relations.SocialProfiles."Uniconnect_Relation_SocialProfiles_Follow_intellectul_entity_has_component"
SELECT follow.COMM_FOLLOW_ID as followid, person.PERSON_ID as socprofileid
FROM Uniconnect_homepage.HOMEPAGE.NR_COMM_FOLLOW as follow
JOIN Uniconnect_homepage.HOMEPAGE.PERSON as person ON person.PERSON_ID = follow.PERSON_ID

//"MOBDA_Datastore".Relations.SocialProfiles."Uniconnect_Relation_SocialProfiles_Tag_intellectuall_entity_has_component"
SELECT tag.PROF_TAG_ID as tagid, socprofile.PERSON_ID as socprofileid
FROM Uniconnect_peopledb.EMPINST.PEOPLE_TAG as tag
JOIN Uniconnect_peopledb.EMPINST.EMPLOYEE as acc ON tag.PROF_SOURCE_KEY = acc.PROF_KEY
JOIN Uniconnect_homepage.HOMEPAGE.PERSON as socprofile ON socprofile.EXID = acc.prof_guid
WHERE socprofile.MEMBER_TYPE = 0

//"MOBDA_Datastore".Relations.SocialProfiles."Uniconnect_Relation_SocialProfilesComment_Like_intellectual_component_has_simple_component"
SELECT likes.recommendation_id as likeid, socPComments.ENTRY_ID as commentid
FROM (SELECT item_id, entry_id FROM "Uniconnect_homepage".HOMEPAGE."BOARD_ENTRIES" 
	WHERE category_type = 5 
		UNION
	SELECT bCom.item_id, bCom.entry_id FROM "Uniconnect_homepage".HOMEPAGE."BOARD_COMMENTS" AS bCom) 
	AS socPComments
JOIN "Uniconnect_homepage".HOMEPAGE."BOARD_RECOMMENDATIONS" AS likes ON likes.item_id = socPComments.item_id

