"""Demo of using pre-signed URLs to download file from S3."""

import boto3
import os
import requests
from datetime import datetime

if __name__ == "__main__":

    s3 = boto3.client(
        's3',
        endpoint_url="https://cog.sanger.ac.uk",  # customizable by env vars
    )

    bucket_name = "bcl-uploader-damian.ziobro"
    file_path = "/home/damian/bcl/bcl_folder.zip"  # 1kB
    file_path = "/home/damian/bcl/bcl_folder_large.zip"  # 100 MB

    file_name = os.path.basename(file_path)

    print(f"Uploading file: '{file_name}' to bucket: '{bucket_name}'")
    start = datetime.now()
    s3.upload_file(file_path, bucket_name, file_name)
    print(f"Uploading finished in: {datetime.now() - start}")

    print("Generating pre-signed URL...")
    url = s3.generate_presigned_url(
        ClientMethod='get_object',
        Params={
            'Bucket': bucket_name,
            'Key': file_name
        }
    )
    print(f"pre-signed url: {url}")

    print(f"Downloading {file_name} from bucket: {bucket_name}...")
    start = datetime.now()

    response = requests.get(url, stream=True)
    output_file = "/tmp/bcl_folder.zip"
    with open(output_file, "wb") as file:
        for chunk in response.iter_content(chunk_size=1024):
            file.write(chunk)

    print(f"Dowloading finished in: {datetime.now() - start}")
    print(f"File downloaded from S3 and saved in: {output_file}")
