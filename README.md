# Gifme

A slack bot

## Features

### Server

**health**   
`POST /health/ping - slack-auth - Slack /ping`   
`GET /health/check - public`  

**auth**  
`POST /auth/slack/pin - slack-auth - Slack /login`  
`POST /auth/cli/login - public`  

**image**  
`POST /image/slack/cmd - slack-auth - Slack /gifme`  
`  Slack /gifme ls`  
`  Slack /gifme <bucket> ls`  
`  Slack /gifme <bucket> <image-name>`  
`POST image/cli/bucket/upload - user-auth`  

### CLI

Install script

`TODO: script to install cli`

```sh
gifme login
    pin: 2736
successfully logged in to Gifme Bot

gifme image upload <bucket-name> <image-name> <filename>
gifme image delete <bucket-name> <image-name>
```

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