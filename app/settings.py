from environs import Env

env = Env()

aws_access_key_id = env('AWS_ACCESS_KEY_ID')
aws_secret_access_key=env('AWS_SECRET_ACCESS_KEY')
aws_default_region=env('AWS_DEFAULT_REGION')
aws_s3_bucket=env('AWS_S3_BUCKET')
