# run mysql
docker run --rm -e MYSQL_ROOT_PASSWORD=1235 -e MYSQL_USER=ubuntu -e MYSQL_PASSWORD=1234 -p 3306:3306 --name mysql -d mysql
sleep 3

# run flask
docker run --rm -p 5000:5000 -e MYSQL_HOST=mysql -e MYSQL_USER=ubuntu -e MYSQL_PASSWORD=1234 --link mysql --name flask -d flask
sleep 3

# run nginx
docker run --rm -p 8080:80 -v $(pwd):/etc/nginx/conf.d/ -v $(pwd):/usr/share/nginx/html/ --link flask -d nginx
