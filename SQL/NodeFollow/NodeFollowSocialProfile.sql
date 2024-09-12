SELECT socPFollow.follow_id AS id, USERS.EXID, USERS.PERSON_ID 
FROM HOMEPAGE.NR_FOLLOWS AS socPFollow
JOIN HOMEPAGE.PERSON AS users ON (users.person_id = socPFollow.person_id)
               