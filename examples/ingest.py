from ai_platform.loader import load_document
from ai_platform.chunking import chunk_text


document = load_document("documents/sample.md")

chunks = chunk_text(document.content)

print(f"Document: {document.path}")
print(f"Chunks: {len(chunks)}")

print()

for chunk in chunks:
    print("-" * 60)
    print(f"Chunk {chunk.id}")
    print("-" * 60)
    print(chunk.text)
    print()