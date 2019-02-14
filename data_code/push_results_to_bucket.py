import boto3
import glob
import os


AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')

BUCKET = 'dojo-skool-10'
POLYGRAM = 'pade'
S3_RESULT_IMAGES_DIRECTORY = '{}/result_images'.format(POLYGRAM)
S3_RESULT_REPORTS_DIRECTORY = '{}/result_reports'.format(POLYGRAM)


def pull_last_image():
    s3 = boto3.resource('s3',
                        aws_access_key_id=AWS_ACCESS_KEY_ID,
                        aws_secret_access_key=AWS_SECRET_ACCESS_KEY)

    list_of_images = glob.glob('result_images/*')
    list_of_reports = glob.glob('result_reports/*')
    result_image_path = max(list_of_images, key=os.path.getctime)
    result_report_path = max(list_of_reports, key=os.path.getctime)

    result_image = open(result_image_path, 'rb')
    result_report = open(result_report_path, 'rb')

    result_image_name = result_image_path.split('/')[-1]
    result_report_name = result_report_path.split('/')[-1]

    s3.Bucket(BUCKET).put_object(Key='{}/{}'.format(S3_RESULT_IMAGES_DIRECTORY, result_image_name), Body=result_image)
    s3.Bucket(BUCKET).put_object(Key='{}/{}'.format(S3_RESULT_REPORTS_DIRECTORY, result_report_name), Body=result_report)


if __name__ == '__main__':
    pull_last_image()
