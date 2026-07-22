from ai_platform.chunking import chunk_text
from ai_platform.embeddings import EmbeddingService
from ai_platform.loader import load_documents
from ai_platform.vector_store import VectorStore


class Indexer:
    """
    Index documents into Qdrant.
    """

    def __init__(self):

        self.embedding_service = EmbeddingService()
        self.vector_store = VectorStore()

    def index_directory(self, directory: str):

        documents = load_documents(directory)

        print(f"Loaded {len(documents)} documents")

        initialized = False

        total_chunks = 0

        for document in documents:

            chunks = chunk_text(
                document.content,
                document.path,
            )

            total_chunks += len(chunks)

            for chunk in chunks:

                embedding = self.embedding_service.embed(
                    chunk.text
                )

                if not initialized:

                    self.vector_store.create_collection(
                        len(embedding)
                    )

                    initialized = True

                self.vector_store.upsert(
                    chunk,
                    embedding,
                )

        print(f"Indexed {total_chunks} chunks")