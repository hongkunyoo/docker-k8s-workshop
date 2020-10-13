start-db:
        docker run --rm -e MYSQL_ROOT_PASSWORD=1234 -e MYSQL_USER=ubuntu -e MYSQL_PASSWORD=1234 -p 3306:3306 --name mysql -d mysql

stop-db:
        docker stop mysql

build-app:
        docker build . -t app

start-app:
        docker run --rm -e MYSQL_HOST=172.17.0.1 -e MYSQL_USER=ubuntu -e MYSQL_PASSWORD=1234 -p 5000:5000 --name app -d app

stop-app:
        docker stop app
