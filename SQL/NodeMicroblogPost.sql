SELECT be.ENTRY_ID AS id, be.CREATION_DATE AS created, be.UPDATE_DATE  AS last_updated, be.CONTENT AS content, be.CONTAINER_ID, person.EXID 
FROM HOMEPAGE.BOARD_ENTRIES be 
JOIN HOMEPAGE.PERSON person ON PERSON.PERSON_ID = BE.actor_uuid
WHERE source <> 'PROFILES'