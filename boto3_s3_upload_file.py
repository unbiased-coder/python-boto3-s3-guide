import boto3_helper

def boto3_s3_upload_file(filename):
    print ('Uploading file: %s to bucket: unbiased-coder-bucket... '%filename, end='')
    session = boto3_helper.init_aws_session()
    s3 = session.resource('s3')
    s3.meta.client.upload_file(filename, 'unbiased-coder-bucket', filename)
    print ('done')

boto3_s3_upload_file('test.txt')
boto3_s3_upload_file('test1.txt')
