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
`docker run -it -p 5000:5000 -v $(pwd):/gifme gifme-dev`

curl localhost:5000

curl -X POST localhost:5000/health/ping

curl localhost:5000/health/check

curl -X POST localhost:5000/image/gifme?some=argument

## Prod

__Build__
`docker build -f dev.Dockerfile -t gifme .`

## Test

docker run -it -p 5000:5000 -v $(pwd):/gifme gifme-dev python3 -m unittest discover test

docker run -it -p 5000:5000 -v $(pwd):/gifme gifme-dev python3 -m unittest test/example.py

## Other

docker run -it -p 5000:5000 -v $(pwd):/gifme gifme-dev sh
