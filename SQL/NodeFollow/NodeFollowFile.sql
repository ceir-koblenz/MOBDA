SELECT CONCAT(fileFollow.media_id, CONCAT(' - ', fileFollow.user_id)) AS id, fileFollow.create_date AS created, users.directory_id,  REPLACE(FILEFOLLOW.MEDIA_ID, ' ', '') AS match_media_id
FROM FILES.MEDIA_NOTIFICATION AS fileFollow
JOIN FILES.USER AS users ON (users.id = fileFollow.user_id)


SELECT CONCAT(fileFollow.media_id, CONCAT(' - ', fileFollow.user_id)) AS id, fileFollow.create_date AS created, users.directory_id
FROM FILES.MEDIA_NOTIFICATION AS fileFollow
JOIN FILES.USER AS users ON (users.id = fileFollow.user_id)
