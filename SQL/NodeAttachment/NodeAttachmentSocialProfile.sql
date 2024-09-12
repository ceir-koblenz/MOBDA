SELECT ATTACH.OBJECT_ID AS id, ATTACH.CREATION_DATE AS created, ATTACH.DISPLAY_NAME AS title, USERS.EXID, socPComments.entry_id
FROM (SELECT item_id, entry_id, ACTOR_UUID  FROM Homepage.BOARD_ENTRIES 
	WHERE category_type = 5 /*eq: SOURCE = 'PROFILES' */
		UNION
	SELECT bCom.item_id, bCom.entry_id, BCOM.ACTOR_UUID  FROM HOMEPAGE.BOARD_COMMENTS AS bCom
	JOIN HOMEPAGE.BOARD_ENTRIES AS parent ON bCom.entry_id = parent.entry_id
	WHERE parent.category_type = 5 /*eq: SOURCE = 'PROFILES' */) AS socPComments
JOIN HOMEPAGE.BOARD_OBJECT_REFERENCE AS ATTACH ON ATTACH.ITEM_ID = socPComments.entry_id
JOIN HOMEPAGE.PERSON AS users ON (USERs.PERSON_ID = socPComments.ACTOR_UUID)
