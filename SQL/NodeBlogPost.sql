SELECT blogposts.id AS id, blogposts.hitcount AS Views, blogposts.pubtime AS created, BLOGPOSTS.title AS title, 
blogposts.updatetime AS last_updated, BLOGPOSTS.userid, BLOGPOSTS.TEXT AS content, blogposts.WEBSITEID, r.EXTID 
FROM  blogs.weblogentry AS blogposts JOIN blogs.ROLLERUSER r ON BLOGPOSTS.USERID = r.ID 

