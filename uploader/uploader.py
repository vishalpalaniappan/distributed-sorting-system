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

    # If object_name was not specified, use file_name
    if object_name is None:
        object_name = os.path.basename(file_name)
        
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
    try:
        if not os.path.exists(DATA_DIR):
            print(f"Directory {DATA_DIR} does not exist")
            return False
            
        files = os.listdir(DATA_DIR)
    except Exception as e:
        print(f"Error accessing directory {DATA_DIR}: {e}")
        return False

    if len(files) > 0:
        #File oldest file
        file = sorted(files)[0]

        # Upload file
        uploadFile(os.path.join(DATA_DIR, file), BUCKET, file)

        # Remove file
        try:
            os.remove(os.path.join(DATA_DIR, file))
        except Exception as e:
            raise(e)

def main(sleep_time=5):
    '''
        Main Loop
    '''
    try:
        print(f"Starting uploader. Monitoring {DATA_DIR} every {sleep_time} seconds...")
        while True:
            checkFolder()
            time.sleep(sleep_time)
    except KeyboardInterrupt:
        print("Uploader stopped by user")
    except Exception as e:
        print(f"Uploader stopped due to error: {e}")

if __name__ == "__main__":
    main()