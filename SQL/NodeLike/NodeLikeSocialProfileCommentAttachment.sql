SELECT  likes.recommendation_id AS id, LIKES.creation_date AS created,  ATTACH.OBJECT_ID, users.exid
FROM (SELECT item_id, entry_id FROM Homepage.BOARD_ENTRIES 
	WHERE category_type = 5 /*eq: SOURCE = 'PROFILES' */
		UNION
	SELECT bCom.item_id, bCom.entry_id FROM HOMEPAGE.BOARD_COMMENTS AS bCom
	JOIN HOMEPAGE.BOARD_ENTRIES AS parent ON bCom.entry_id = parent.entry_id
	WHERE parent.category_type = 5 /*eq: SOURCE = 'PROFILES' */) AS socPComments
JOIN HOMEPAGE.BOARD_OBJECT_REFERENCE AS ATTACH ON ATTACH.ITEM_ID = socPComments.entry_id
JOIN HOMEPAGE.BOARD_RECOMMENDATIONS AS likes ON likes.item_id = socPComments.item_id
JOIN HOMEPAGE.PERSON AS users ON (users.person_id = likes.recommender_id)