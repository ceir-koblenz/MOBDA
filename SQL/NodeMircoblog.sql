SELECT MICROBLOG.BOARD_CONTAINER_ID AS id, PERSON.EXID 
FROM homepage.BOARD microblog
JOIN HOMEPAGE.PERSON  AS person ON MICROBLOG.BOARD_OWNER_ASSOC_ID = PERSON.PERSON_ID 
