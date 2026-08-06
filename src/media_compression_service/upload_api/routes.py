from fastapi import APIRouter, UploadFile, File

from media_compression_service.upload_api.schemas import UploadImageResponse
from media_compression_service.upload_api.services.upload_service import UploadService

router = APIRouter(prefix="/images", tags=["Images"])

upload_service = UploadService()

# Response model : 1. Validates the response 2. Filters extra fields 3. Generates API documentation
@router.post("", response_model=UploadImageResponse)
async def upload_image(image: UploadFile = File(...)):

    message = await upload_service.upload_image(image)
    return UploadImageResponse(message=message)

