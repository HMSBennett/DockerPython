# DockerPython

docker ps -a

docker images

docker build -t myapp:latest .

docker build -t alternative:latest --build-arg PYTHON_VERSION=2.7 .

docker ps -a

docker images

docker run -d -p 9000:9000 --name 3.6 myapp:latest

docker stop 3.6

docker rm 3.6

docker run -d -p 9000:9000 --name 2.7 alternative:latest
