SELECT mainComs.content AS content, mainComs.creation_date AS created, mainComs.entry_id AS id, mainComs.update_date AS last_updated, USERS.exid
FROM homepage.BOARD_ENTRIES AS mainComs
JOIN homepage.PERSON AS users ON (users.person_id = mainComs.actor_uuid)
WHERE category_type = 5 /*eq: SOURCE = 'PROFILES' */
UNION ALL
SELECT socialProfilesComments.content AS content, socialProfilesComments.creation_date AS created, comment_id AS id, socialProfilesComments.update_date AS last_updated, USERS.EXID 
FROM homepage.BOARD_COMMENTS AS socialProfilesComments
JOIN homepage.BOARD_ENTRIES AS boardEntries ON (socialProfilesComments.entry_id = boardEntries.entry_id)
JOIN homepage.PERSON AS users ON (users.person_id = socialProfilesComments.actor_uuid)
WHERE category_type = 5 /*eq: SOURCE = 'PROFILES' */