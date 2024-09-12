SELECT CONCAT(likes.media_id, CONCAT(' - ', likes.user_id)) AS id, likes.create_date AS created, users.directory_id, REPLACE(likes.media_id, ' ', '')AS match_media_id
FROM FILES.MEDIA_RECOMMEND AS likes
JOIN FILES.USER  AS users ON (users.id = likes.user_id)

