Flask Hello World + Deploy to Elastic Cloud Service (ECS)
===============

1. Build docker image locally:
```
docker build - t flask-hello-world:latest . 
```

2. Run docker container locally:
```
docker run -d -p 5000:5000 flask-hello-world -name do
```
