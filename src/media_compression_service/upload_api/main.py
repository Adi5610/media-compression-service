from fastapi import FastAPI

app = FastAPI(
    title="Image Compression Service",
    version="1.0.0",
)


@app.get("/health")
def health():
    return {"status": "healthy"}