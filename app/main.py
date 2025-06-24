from fastapi import FastAPI, UploadFile, File
from app.video_utils import extract_frames
from app.feature_extraction import compute_feature_vector
from app.vector_db import init_collection, add_vector
from app.models import SearchQuery
from app.retrieval import get_similar_frames

app = FastAPI()

@app.on_event("startup")
def startup():
    init_collection()

# http://localhost:8000/upload_video
@app.post("/upload_video")
async def upload_video(file: UploadFile = File(...)):
    path = f"temp_{file.filename}"
    with open(path, "wb") as f:
        f.write(await file.read())
    
    frames = extract_frames(path)
    for frame_path in frames:
        vec = compute_feature_vector(frame_path)
        add_vector(frame_path, vec)
    return {"extracted": frames}

from app.feature_extraction import compute_feature_vector

vector = compute_feature_vector("output/frame_0.jpg")
print(len(vector))  # Should print 512


@app.post("/search_similar")
async def search_similar(query: SearchQuery):
    return get_similar_frames(query.vector, query.top_k)
