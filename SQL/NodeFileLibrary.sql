SELECT DISTINCT c.ID  AS id, c.TITLE AS title, c.EXTERNAL_CONTAINER_ID 
FROM files.COLLECTION c   
WHERE c.owner_user_id LIKE X'00000000000000000000000000000000'