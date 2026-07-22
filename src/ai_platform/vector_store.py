from uuid import uuid4

from qdrant_client import QdrantClient
from qdrant_client.models import (
    Distance,
    PointStruct,
    VectorParams,
)

from ai_platform.types import Chunk


class VectorStore:
    """
    Wrapper around Qdrant operations.
    """

    def __init__(
        self,
        host: str = "localhost",
        port: int = 6333,
        collection_name: str = "documents",
    ):

        self.collection_name = collection_name

        self.client = QdrantClient(
            host=host,
            port=port,
        )

    def create_collection(
        self,
        vector_size: int,
    ):

        collections = self.client.get_collections().collections

        existing = {
            collection.name
            for collection in collections
        }

        if self.collection_name in existing:
            print(
                f"✓ Collection '{self.collection_name}' already exists"
            )
            return

        self.client.create_collection(
            collection_name=self.collection_name,
            vectors_config=VectorParams(
                size=vector_size,
                distance=Distance.COSINE,
            ),
        )

        print(
            f"✓ Created collection '{self.collection_name}'"
        )

    def upsert(
        self,
        chunk: Chunk,
        embedding: list[float],
    ):

        self.client.upsert(
            collection_name=self.collection_name,
            points=[
                PointStruct(
                    id=str(uuid4()),
                    vector=embedding,
                    payload={
                        "text": chunk.text,
                        "source": str(chunk.source),
                        "chunk_id": chunk.id,
                    },
                )
            ],
        )

    def search(
        self,
        embedding: list[float],
        limit: int = 3,
    ) -> list[dict]:
        """
        Perform semantic similarity search.
        """

        results = self.client.query_points(
            collection_name=self.collection_name,
            query=embedding,
            limit=limit,
        )

        matches = []

        for point in results.points:

            matches.append(
                {
                    "score": point.score,
                    "text": point.payload["text"],
                    "source": point.payload["source"],
                    "chunk_id": point.payload["chunk_id"],
                }
            )

        return matches