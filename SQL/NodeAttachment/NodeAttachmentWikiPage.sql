SELECT DISTINCT  wikiArt.id AS id, wikiArt.title AS title, wikiArt.create_date AS created, wikiArt.last_update AS last_updated,  users.directory_id, wikiArticles.media_id, REPLACE(WIKIART.id, ' ', '') AS match_id
FROM wikis.MEDIA_ADDITIONAL_FILE AS wikiArt
LEFT JOIN wikis.MEDIA_REVISION AS wikiArticles ON wikiArticles.media_id = wikiArt.media_id
LEFT JOIN wikis.USER AS users ON (users.id = wikiArt.last_update_user_id)

