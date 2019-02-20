import os
from time import time

import boto3

AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')

BUCKET = 'dojo-skool-10'
S3_IMAGES_DIRECTORY = 'src_images/'


def pull_last_image():
    s3 = boto3.resource('s3',
                        aws_access_key_id=AWS_ACCESS_KEY_ID,
                        aws_secret_access_key=AWS_SECRET_ACCESS_KEY)
    s3_client = boto3.client('s3')

    response = s3_client.list_objects(
        Bucket=BUCKET,
        Prefix=S3_IMAGES_DIRECTORY
    )

    last_image = response['Contents'][-1]['Key']
    image_path = 'images/traffic_{}.jpg'.format(int(time()))
    s3_client.download_file(BUCKET,
                            last_image,
                            image_path)


if __name__ == '__main__':
    pull_last_image()
