from app.vector_db import search_similar

def get_similar_frames(vector: list, top_k: int = 5):
    results = search_similar(vector, top_k)
    return [
        {"image_path": hit.payload['image_path'], "score": hit.score}
        for hit in results
    ]
