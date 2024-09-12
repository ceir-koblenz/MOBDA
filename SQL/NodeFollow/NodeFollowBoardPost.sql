SELECT boardPFollow.uuid AS id, boardPFollow.created AS created, USERS.exid, BOARDPFOLLOW.TOPICID 
FROM FORUM.DF_SUBSCRIPTION AS boardPFollow
JOIN FORUM.df_memberprofile AS users ON (users.memberid = boardPFollow.createdby)