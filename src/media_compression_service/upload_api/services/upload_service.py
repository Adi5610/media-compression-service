from fastapi import UploadFile


class UploadService:

    async def upload_image(self, image: UploadFile) -> str:
        return "image uploaded successfully"