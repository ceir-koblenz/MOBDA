SELECT microblogPostComments.comment_id AS id, microblogPostComments.content AS content, microblogPostComments.creation_date AS created, microblogPostComments.entry_id, microblogPostComments.update_date AS last_updated, users.exid, MICROBLOGPOSTCOMMENTS.ITEM_ID 
FROM homepage.BOARD_COMMENTS AS microblogPostComments
JOIN homepage.BOARD_ENTRIES AS boardEntries ON (microblogPostComments.entry_id = boardEntries.entry_id)
JOIN homepage.PERSON AS users ON (users.person_id = microblogPostComments.actor_uuid)
WHERE category_type = 3 