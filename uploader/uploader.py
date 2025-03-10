import os
import boto3
import time
from botocore.exceptions import ClientError

DATA_DIR = "../compressed_data"
BUCKET = "sample-log-json-bucket"

def uploadFile(file_name, bucket, object_name=None):
    '''
        Uploads the given file with the given name to the bucket.
    '''
    s3_client = boto3.client('s3')
    try:
        s3_client.upload_file(file_name, bucket, object_name)
        print("Successfuly uploaded file:", file_name)
    except ClientError as e:
        print("Failed to uploaded file:", file_name)
        raise(e)

def checkFolder():
    '''
        Check folder to see if there are files to upload.
    '''
    files = os.listdir(DATA_DIR)

    if len(files) > 0:
        file = sorted(files)[0]
        path = os.path.join(DATA_DIR, file)
        uploadFile(path, BUCKET, file)

        try:
            os.remove(path)
        except Exception as e:
            raise(e)

def main():
    '''
        Main Loop
    '''
    while True:
        checkFolder()
        time.sleep(5)

if __name__ == "__main__":
    main()