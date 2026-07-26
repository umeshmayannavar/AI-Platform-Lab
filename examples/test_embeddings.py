from ai_platform.embeddings import EmbeddingClient

client = EmbeddingClient()

vector = client.embed("Kubernetes is awesome")

print()

print("=" * 60)
print("Embedding Test")
print("=" * 60)

print(f"Dimensions : {len(vector)}")

print(f"First Value: {vector[0]:.6f}")