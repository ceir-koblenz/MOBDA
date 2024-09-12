SELECT likes.recommendation_id AS id, likes.creation_date AS created,  comments.comment_id, users.exid
FROM HOMEPAGE.BOARD_RECOMMENDATIONS AS likes
JOIN HOMEPAGE.BOARD_COMMENTS AS comments ON likes.item_id = comments.item_id
JOIN HOMEPAGE.PERSON AS users ON (users.person_id = likes.recommender_id)
