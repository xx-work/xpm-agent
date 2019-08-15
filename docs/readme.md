# 修改成熟后 将sdk放到当前目录下编译。


"""
docker run -itd -p 27017:27017 --name mongo-server  \
-e MONGO_INITDB_ROOT_USERNAME=admin007 \
-e MONGO_INITDB_ROOT_PASSWORD=myadmin@816 \
--restart=always \
mongo:3.6
"