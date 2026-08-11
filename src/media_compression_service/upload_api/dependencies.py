import os
from typing import Annotated

from fastapi import Depends

from media_compression_service.shared.settings import settings
from media_compression_service.upload_api.repositories.s3_repository import S3Repository
from media_compression_service.upload_api.services.upload_service import UploadService



def get_s3_repository() -> S3Repository:
    return S3Repository(
        bucket_name=settings.s3_bucket_name,
        region=settings.aws_region,
        upload_url_expiration=settings.upload_url_expiration,
    )

def get_upload_service(s3_repository: S3Repository = Depends(get_s3_repository)) -> UploadService:
    return UploadService(s3_repository)

# uploadServiceDep is obj of type UploadService which depends on get_upload_service
uploadServiceDep = Annotated[UploadService, Depends(get_upload_service)]