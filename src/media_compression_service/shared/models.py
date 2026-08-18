from uuid import UUID
from dataclasses import dataclass

from media_compression_service.shared.enums import ImageStatus

@dataclass
class UploadResult:
    image_id: UUID
    status: ImageStatus
    original_key: str
    upload_url: str