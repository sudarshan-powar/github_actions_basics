import boto3
import datetime

def lambda_handler(event, context):
    s3 = boto3.client('s3')

    # change this to your bucket name
    bucket_name = 'github-actions-tutorial-saayam'

    # content to upload
    content = 'Hello World uploaded from Lambda'
    file_name = f'hello-lambda-{datetime.datetime.utcnow().isoformat()}.txt'

    try:
        s3.put_object(
            Bucket=bucket_name,
            Key=file_name,
            Body=content
        )
        return {
            'statusCode': 200,
            'body': f'File uploaded successfully: {file_name}'
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': f'Error uploading file: {str(e)}'
        }
