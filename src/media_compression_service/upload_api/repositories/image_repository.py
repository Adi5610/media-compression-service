from datetime import datetime, timezone
from uuid import UUID

import boto3

from media_compression_service.shared.enums import ImageStatus


class ImageRepository:

    def __init__(self, table_nam: str, region: str):

        dynamodb = boto3.resource('dynamodb', region_name=region)

        self.table = dynamodb.Table(table_nam)

    def create(self,
               image_id: UUID,
               status: ImageStatus,
               original_key : str,
               original_filename: str,
               content_type: str,
               declared_size: int,
               )-> None:

        now = datetime.now(timezone.utc).isoformat()

        self.table.put_item(
            Item={
                'image_id': str(image_id),
                'status': str(status.value),
                'original_filename': original_filename,
                'original_key': original_key,
                'compressed_key': None,
                'content_type': content_type,
                'declared_size': declared_size,
                'compressed_size': None,
                'retry_count': 0,
                'last_error': None,
                'created_at': now,
                'updated_at': now,
                'completed_at': None,
            }
        )

