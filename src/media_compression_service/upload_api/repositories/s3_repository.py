from uuid import UUID

import boto3
from pydantic import BaseModel


class S3Repository:

    def __init__(self, bucket_name: str, region: str, upload_url_expiration: int = 900):
        self.bucket_name = bucket_name
        self.region = region
        self.upload_url_expiration = upload_url_expiration

        self.client = boto3.client('s3', region_name=region)

    def generate_upload_url(self, s3_key: str, content_type: str) -> str:

        """

        generates upload url for given image_id, filename and content_type

        """

        upload_url = self.client.generate_presigned_url(
            ClientMethod="put_object",
            Params={
                "Bucket": self.bucket_name,
                "Key": s3_key,
                "ContentType": content_type,
            },
            ExpiresIn=self.upload_url_expiration,
        )

        return upload_url



