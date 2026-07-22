from ai_platform.embeddings import EmbeddingService

service = EmbeddingService()

embedding = service.embed(
    "Kubernetes is a container orchestration platform."
)

print(f"Dimension: {len(embedding)}")
print(embedding[:10])