SELECT likes.creation_date AS created, likes.recommendation_id AS id, microblogposts.entry_id, users.exid
FROM HOMEPAGE.BOARD_RECOMMENDATIONS AS likes
JOIN HOMEPAGE.BOARD_ENTRIES AS microblogposts ON likes.item_id = microblogposts.item_id
JOIN HOMEPAGE.PERSON AS users ON (users.person_id = likes.recommender_id)