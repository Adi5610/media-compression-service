from fastapi import UploadFile
from uuid import UUID, uuid4

from media_compression_service.shared.models import UploadResult
from media_compression_service.shared.enums import ImageStatus
from media_compression_service.upload_api.repositories.s3_repository import S3Repository


class UploadService:

    def __init__(self, s3_repository: S3Repository):
        self.s3_repository = s3_repository

    async def upload_image(self, file_name: str, content_type: str) -> UploadResult:

        image_id = uuid4()
        s3_key, upload_url = self.s3_repository.generate_upload_url(
            image_id=image_id,
            filename=file_name,
            content_type=content_type,
        )

        return UploadResult(image_id=image_id,
                            status=ImageStatus.UPLOADING,
                            original_key=s3_key,
                            upload_url=upload_url)