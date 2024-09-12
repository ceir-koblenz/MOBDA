SELECT CONCAT(WIKIPAGE.id, CONCAT(' - ', likes.user_id)) AS id, likes.create_date AS created, wikiPage.id AS wiki_id, users.directory_id 
FROM WIKIS.MEDIA_RECOMMEND AS likes
JOIN WIKIS.MEDIA_REVISION AS wikiPage ON wikiPage.media_id = likes.media_id
JOIN Wikis.USER AS users ON (users.id = likes.user_id)