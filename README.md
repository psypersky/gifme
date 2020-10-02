# Gifme

## Dev

__Build__
`docker build -f dev.Dockerfile -t gifme-dev .`

__Run locally__
`docker run -it -p 5000:5000 -v $(pwd)/app/:/app gifme-dev`

curl localhost:5000

curl -X POST localhost:5000/ping

curl -X POST localhost:5000/bale

## Prod

__Build__
`docker build -f dev.Dockerfile -t gifme .`

https://flask.palletsprojects.com/en/1.1.x/
https://github.com/Zulko/moviepy