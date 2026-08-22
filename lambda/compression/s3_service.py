import boto3


class S3Service:
    def __init__(self):
        self.client = boto3.client('s3')

    def download(self, bucket: str, key: str) -> bytes:
        response = self.client.get_object(
            Bucket=bucket,
            Key=key
        )
        return response['Body'].read()

    def upload(self, bucket: str, key: str, body: bytes, content_type: str) -> None:

        self.client.put_object(
            Body=body,
            Bucket=bucket,
            Key=key,
            ContentType=content_type,
        )

