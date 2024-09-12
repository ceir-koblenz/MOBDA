SELECT wikiComs.COMMENT AS content, wikiComs.create_date AS created, wikiComs.id AS id, wikiComs.last_update AS last_updated, wikiComs.title AS title, users.DIRECTORY_ID, WIKICOMS.MEDIA_ID, REPLACE(WIKICOMS.id, ' ', '') AS match_com_id
FROM WIKIS.MEDIA_COMMENT AS wikiComs
JOIN WIKIS."USER" AS users ON (users.id = wikiComs.owner_user_id)