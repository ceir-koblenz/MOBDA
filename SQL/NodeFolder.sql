SELECT c.ID AS id, c.CREATE_DATE  AS created, c.last_update AS last_updated, c.TITLE  AS title, REPLACE(c.ID , ' ', '') AS match_folder_id
FROM files.COLLECTION c 
