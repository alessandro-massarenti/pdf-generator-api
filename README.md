# pdf-generator-api
A pdf generator api written using Fastapi

## starting the service

```
#builds the image
docker build -t pdf-generator .

#starts the container
docker run --name pdff -p 80:80 pdf-generator
```
