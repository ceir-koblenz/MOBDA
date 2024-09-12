SELECT CONCAT(FILES.ID , CONCAT( ' - ', likes.user_id)) AS id, likes.create_date AS created, users.directory_id, files.id AS file_id, REPLACE(LIKES.MEDIA_ID, ' ', '') AS match_media_id
FROM FILES.MEDIA_RECOMMEND AS likes
JOIN FILES.MEDIA_REVISION AS files ON likes.media_id = files.media_id
JOIN FILES.USER AS users ON (users.id = likes.user_id)