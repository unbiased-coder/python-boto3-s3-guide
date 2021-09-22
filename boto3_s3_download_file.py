import boto3_helper

def boto3_s3_download_file(filename):
    print ('Downloading file: %s to bucket: unbiased-coder-bucket... '%filename, end='')
    session = boto3_helper.init_aws_session()
    s3 = session.resource('s3')
    s3.meta.client.download_file('unbiased-coder-bucket', filename, filename + '.new')
    print ('done')
    

boto3_s3_download_file('test.txt')
boto3_s3_download_file('test1.txt')
