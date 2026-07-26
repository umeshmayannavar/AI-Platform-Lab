from ai_platform.embeddings import EmbeddingClient
from ai_platform.rag import RAGService
from ai_platform.retrieval.service import RetrievalService
from ai_platform.vector_store import VectorStore


def main():

    embedding_client = EmbeddingClient()

    vector_store = VectorStore()

    retrieval = RetrievalService(
        embedding_client,
        vector_store,
    )

    rag = RAGService(
        retrieval,
    )

    print("=" * 60)
    print("AI Platform Lab - RAG Chat")
    print("=" * 60)

    while True:

        question = input("\nQuestion (exit to quit): ")

        if question.lower() == "exit":
            break

        print("\nSearching knowledge base...")

        answer = rag.answer(question)

        print("\nAnswer")
        print("-" * 60)
        print(answer)


if __name__ == "__main__":
    main()