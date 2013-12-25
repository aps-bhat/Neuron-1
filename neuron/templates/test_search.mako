<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>test_search</title>
</head>
<body>
<%
import pymongo
import gridfs
conn=pymongo.Connection()
db=conn.mydb
fs=gridfs.GRIDFS(db)
image=fs.get(ObjectId("52b32b02b00489b318d6e098")).read()
%>
<im
</body>
</html>
