SELECT  tags.id AS id, tags.name AS label, tags.time AS created, tags.entryid, USERS.extid
FROM blogs.ROLLER_WEBLOGENTRYTAG  AS tags
JOIN blogs.ROLLERUSER AS users ON (users.id = tags.userid)
