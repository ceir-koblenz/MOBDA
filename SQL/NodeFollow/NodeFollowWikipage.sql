SELECT CONCAT(wikiarticles.ID , CONCAT(' - ',follows.user_id)) AS id, follows.create_date AS created, users.DIRECTORY_ID, WIKIARTICLES.id AS wiki_id, REPLACE(WIKIARTICLES.media_id, ' ', '') AS match_media_id
FROM wikis.LIBRARY_NOTIFICATION AS follows
JOIN WIKIS.MEDIA_REVISION AS wikiarticles ON follows.library_id = wikiarticles.library_id
JOIN WIKIS.USER AS users ON (users.id = follows.user_id)
