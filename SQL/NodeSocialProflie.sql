SELECT USER.CREATION_DATE AS created, USER.displayname AS title, USER.person_id AS id, USER.last_update AS last_updated, USER.exid
FROM HOMEPAGE.PERSON AS USER 
WHERE USER.member_type = 0 
