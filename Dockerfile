FROM python:3.12.0-alpine

WORKDIR /parser

COPY . /parser/

RUN pip install -r requirements.txt

# You have to prodvide API value, if there are no .env file
# ENV API=value

CMD sh -c "gunicorn -k uvicorn.workers.UvicornWorker --workers 4 --bind 0.0.0.0:80 main:app"
