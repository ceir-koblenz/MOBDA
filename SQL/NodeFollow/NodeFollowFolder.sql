SELECT CONCAT(folderFollow.collection_id, CONCAT(' - ', folderFollow.user_id)) AS id, folderFollow.create_date AS created, users.directory_id, FOLDERFOLLOW.COLLECTION_ID, REPLACE(FOLDERFOLLOW.COLLECTION_ID, ' ', '') AS match_folder_id
FROM FILES.COLLECTION_NOTIFICATION AS folderFollow
JOIN FILES.USER AS users ON (users.id = folderFollow.user_id)
 