import boto3_helper

def boto3_s3_delete_files():
    session = boto3_helper.init_aws_session()
    s3 = session.resource('s3')
    bucket = s3.Bucket(name="unbiased-coder-bucket")
    print("Deleting all files in bucket")
    bucket.objects.all().delete()

boto3_s3_delete_files()
