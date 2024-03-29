# TJ DOMAIN WHOIS


> **To build and run with Docker**

```
git clone https://github.com/lilpunkrocket/domain-whois.git
Docker build -t image_name
```
_If you have .env file_
```
Docker run [-d] -p {your host port}:80 image_name
```
_Else_
```
Docker run [-d] -e API={your own value} -p {your host port}:80 image_name
```

_To view logs from Docker container_
```
docker exec -it parser sh -c "tail -f logs/[access.log|error.log]"
```
***
> **To run with uvicorn**

```
git clone https://github.com/lilpunkrocket/domain-whois.git
pip install -r requirements.txt
echo "API={your own value}" > .env
uvicorn main:app
```
