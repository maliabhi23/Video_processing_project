from qdrant_client import QdrantClient
from qdrant_client.http.models import Distance, VectorParams, PointStruct
from app.config import QDRANT_COLLECTION
import uuid

# Connect to in-memory Qdrant (you can also use local Qdrant server with host/port)
client = QdrantClient(":memory:")

def init_collection():
    """Initialize the Qdrant collection if not exists."""
    collections = client.get_collections().collections
    collection_names = [c.name for c in collections]
    if QDRANT_COLLECTION not in collection_names:
        client.recreate_collection(
            collection_name=QDRANT_COLLECTION,
            vectors_config=VectorParams(
                size=512,  # color histogram size (8*8*8 = 512)
                distance=Distance.COSINE
            )
        )

def add_vector(image_path: str, vector: list):
    """Add a vector to the Qdrant collection."""
    point_id = str(uuid.uuid4())  # ✅ generate proper UUID
    client.upsert(
        collection_name=QDRANT_COLLECTION,
        points=[
            PointStruct(
                id=point_id,
                vector=vector,
                payload={"image_path": image_path}
            )
        ]
    )

def search_similar(vector: list, top_k: int = 5):
    """Search similar vectors from Qdrant."""
    hits = client.search(
        collection_name=QDRANT_COLLECTION,
        query_vector=vector,
        limit=top_k
    )
    return hits
