from ai_platform.embeddings import EmbeddingClient
from ai_platform.retrieval.service import RetrievalService
from ai_platform.vector_store import VectorStore


embedding_client = EmbeddingClient()

vector_store = VectorStore()

retriever = RetrievalService(
    embedding_client,
    vector_store,
)

question = input("Question: ")

matches = retriever.retrieve(question)

print()

print("=" * 60)
print("Top Matches")
print("=" * 60)

for index, match in enumerate(matches, start=1):

    print()

    print(f"Match #{index}")
    print(f"Score : {match['score']:.2f}")
    print(f"Source: {match['source']}")

    print()

    print(match["text"])