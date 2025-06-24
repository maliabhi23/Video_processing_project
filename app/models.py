from pydantic import BaseModel
from typing import List

class SearchQuery(BaseModel):
    vector: List[float]
    top_k: int = 5
