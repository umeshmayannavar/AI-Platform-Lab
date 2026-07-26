from ai_platform.chunking import chunk_text
from ai_platform.embeddings import EmbeddingClient
from ai_platform.loader import load_document
from ai_platform.vector_store import VectorStore


document = load_document("documents/sample.md")

chunks = chunk_text(
    document.content,
    source=document.path,
)

embedding_client = EmbeddingClient()

vector_store = VectorStore()

print("Creating embeddings...")

first_embedding = embedding_client.embed(
    chunks[0].text
)

vector_store.create_collection(
    len(first_embedding)
)

for chunk in chunks:

    embedding = embedding_client.embed(
        chunk.text
    )

    vector_store.upsert(
        chunk,
        embedding,
    )

print()

print("=" * 60)
print("Document Indexed Successfully")
print("=" * 60)

print(f"Document : {document.path}")
print(f"Chunks   : {len(chunks)}")