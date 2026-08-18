from fastapi import APIRouter, UploadFile, File, Depends, HTTPException

from media_compression_service.upload_api.dependencies import uploadServiceDep
from media_compression_service.upload_api.schemas import UploadImageResponse, ImageID, CreateImageRequest

router = APIRouter(prefix="/api/v1/images", tags=["Images"])

# Response model : 1. Validates the response 2. Filters extra fields 3. Generates API documentation
@router.post("",
             status_code=201,
             response_model=UploadImageResponse)
async def upload_image(request: CreateImageRequest,
                       service: uploadServiceDep):

    result = await service.upload_image(
        file_name=request.filename,
        content_type=request.content_type,
        size=request.size,
    )
    return UploadImageResponse(
        image_id=result.image_id,
        upload_url=result.upload_url,
        status=result.status,
    )

