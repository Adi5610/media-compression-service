
from media_compression_service.shared.enums import ImageStatus
from uuid import UUID
from pydantic import BaseModel, Field

ImageID = UUID

class CreateImageRequest(BaseModel):
    filename: str = Field(min_length=1)
    content_type: str
    size: int = Field(gt=0)

class UploadImageResponse(BaseModel):
    upload_url: str
    image_id: ImageID
    status: ImageStatus