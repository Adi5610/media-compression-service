from image_processor import ImageProcessor
from s3_service import S3Service
import boto3

s3 = boto3.client('s3')

processor = ImageProcessor()
s3_service = S3Service()

def _genrate_compressed_key(original_key: str) -> str:

    return original_key.replace('original/', 'compressed/', 1).rsplit('.', 1)[0] + ".webp"


def handler(event, context):

    detail = event['detail']

    # get bucket and event name form details (event)
    bucket = detail['bucket']['name']
    key = detail['object']['key']

    # fetch image bytes from s3
    image_bytes = s3_service.download(bucket, key)

    # compress image using
    compressed_bytes = processor.compress(image_bytes)

    # only if image is successfully compressed
    if len(compressed_bytes) < len(image_bytes):


        compressed_key = _genrate_compressed_key(key)

        # upload coimpressed image to S3
        s3_service.upload(bucket, compressed_key, compressed_bytes, 'image/webp')

    else:
        compressed_key = None


    return {
        "statusCode": 200,
        "body": {
            "original_key": key,
            "Original_size": len(image_bytes),
            "Compressed_key": compressed_key,
            "Compressed_size": len(compressed_bytes),

        }
    }