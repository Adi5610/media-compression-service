from datetime import timezone, datetime
from uuid import UUID, uuid4

from media_compression_service.shared.models import UploadResult
from media_compression_service.shared.enums import ImageStatus
from media_compression_service.upload_api.repositories.image_repository import ImageRepository
from media_compression_service.upload_api.repositories.s3_repository import S3Repository


def _genrate_s3_key(image_id: UUID, file_name: str) -> str:

    now = datetime.now(timezone.utc)
    extension = file_name.rsplit('.', 1)[-1]


    return (f"original/"
              f"{now:%y/%m/%d}/"
              f"{image_id}.{extension}"
              )

class UploadService:

    def __init__(self, s3_repository: S3Repository, image_repository: ImageRepository):
        self.s3_repository = s3_repository
        self.image_repository = image_repository

    async def upload_image(self, file_name: str, content_type: str, size:int) -> UploadResult:


        # generate iumage id
        image_id = uuid4()

        # generate original key for s3
        s3_key = _genrate_s3_key(image_id, file_name)

        #generate presigned upload url
        upload_url = self.s3_repository.generate_upload_url(
            s3_key=s3_key,
            content_type=content_type,
        )

        #insert data into dynamodb
        self.image_repository.create(
            image_id=image_id,
            status=ImageStatus.UPLOADING,
            original_key=s3_key,
            original_filename=file_name,
            content_type=content_type,
            declared_size=size,

        )

        return UploadResult(image_id=image_id,
                            status=ImageStatus.UPLOADING,
                            original_key=s3_key,
                            upload_url=upload_url)