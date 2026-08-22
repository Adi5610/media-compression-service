from PIL import Image
from io import BytesIO

class ImageProcessor:

    def compress(self, imageBytes: bytes) -> bytes:
        with Image.open(BytesIO(imageBytes)) as image:

            output = BytesIO()

            image.save(output,
                       format='WEBP',
                       quality=80,
                       optimize=True,)

        return output.getvalue()
