import uvicorn
from fastapi import FastAPI
from media_compression_service.upload_api.routes import router

app = FastAPI(
    title="Image Compression Service",
    version="1.0.0",
)

app.include_router(router)

@app.get("/health")
def health():
    return {"status": "healthy"}

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)