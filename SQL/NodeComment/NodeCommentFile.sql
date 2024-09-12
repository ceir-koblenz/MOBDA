SELECT fileComs.id AS id, fileComs.COMMENT AS content, fileComs.create_date AS created,  fileComs.last_update AS last_updated, fileComs.title AS title, USERS.DIRECTORY_ID, FILECOMS.MEDIA_ID,  REPLACE(FILECOMS.ID, ' ', '') AS match_comment_id
FROM files.MEDIA_COMMENT AS fileComs
JOIN files."USER" AS users ON (users.id = fileComs.owner_user_id)