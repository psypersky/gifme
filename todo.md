# TODO

- [x] Setup python in docker
- [x] flask for development
- [x] read about decorators
- [x] volume binded to localhost for code restart on change
- [x] install & configure aws cli
- [x] create ecr repository and push gifme image
- [x] Setup ELB
- [x] Setup ECS cluster, task definition, service
- [x] check everything works
- [x] create and deploy ping endpoint
- [x] how to create a slash commands slack bot?
- [x] create /ping slash command in slack
- [x] create /bale endpoint and test image attachments
- [x] get some britney pictures
- [x] find out the most Flasky way to structure a Flask project
- [x] redefine the api
- [x] new foldering/blueprint structure
- [x] create cluster, task definition, service and deploy with aws cli
- [x] Add example unit tests
- [x] enable logs in ECS
- [x] check what Slack sends to gifme
- [x] set docker environment variables using an .env file
- [x] code first version of ls slash command
- [x] deploy
- [ ] find out how to use patch.object correctly
- [ ] give api s3 access
- [ ] ad a json logger
- [ ] set up a load balancer to have an static ip :/ $$, there seems to be no other way for ECS w fargate
- [ ] implement gifme command using S3 with some random gifs without auth
- [ ] cloudwatch logs
- [ ] use pipenv to run commands https://pipenv-fork.readthedocs.io/en/latest/
- [ ] read about flask contexts https://testdriven.io/blog/flask-contexts/
- [ ] ECS CLI V2
- [ ] setup production env
https://aws.amazon.com/blogs/containers/announcing-the-amazon-ecs-cli-v2/
https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-cli-tutorial-fargate.html

- [ ] Use cloud formation
https://github.com/aws-samples/ecs-refarch-cloudformation

- [ ] https://packaging.python.org/guides/installing-stand-alone-command-line-tools/

Check later

Flask production - https://vsupalov.com/flask-web-server-in-production/ 
Greenlets vs threads - https://stackoverflow.com/questions/15556718/greenlet-vs-threads
Async Flask - https://pgjones.gitlab.io/quart/index.html
JSON web tokens vuln - https://auth0.com/blog/critical-vulnerabilities-in-json-web-token-libraries/

https://flask.palletsprojects.com/en/1.1.x/
https://github.com/Zulko/moviepy

Testing
https://chromium.googlesource.com/external/github.com/google/oauth2client/+/master/tests/contrib/test_flask_util.py
https://gist.github.com/papaeye/5656071
https://docs.github.com/en/free-pro-team@latest/github/searching-for-information-on-github/searching-code
https://www.programcreek.com/python/example/63694/mock.patch.object
http://www.ines-panker.com/2020/06/01/python-mock.html

https://palletsprojects.com/
https://dev.mikamai.com/2016/12/07/elastic-ip-address-eip-and-ecs-ec2-container/
https://medium.com/galvanize/static-ip-applications-on-aws-ecs-c7d411421d4f