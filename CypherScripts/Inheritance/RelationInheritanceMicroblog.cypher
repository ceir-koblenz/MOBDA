MATCH (coc:Container_Concept)
MATCH (mbc:Microblog_Concept)
WITH [coc, mbc] AS ConMBC
UNWIND ConMBC as conMBC
MATCH (mb:Microblog)
MERGE (mb)-[rmb:is_a]->(conMBC)