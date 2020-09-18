# Gifme


`docker build -f dev.Dockerfile -t gifme-dev .`

`docker run -it -p 5000:5000 -v $(pwd)/app/:/app gifme-dev`

## Prod

`docker build -f dev.Dockerfile -t gifme .`

https://flask.palletsprojects.com/en/1.1.x/
https://github.com/Zulko/moviepy