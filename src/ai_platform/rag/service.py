"""
Retrieval-Augmented Generation (RAG) service.
"""

from ai_platform.llm import chat
from ai_platform.rag.context import ContextBuilder
from ai_platform.retrieval.service import RetrievalService


class RAGService:
    """
    End-to-end Retrieval-Augmented Generation service.
    """

    def __init__(
        self,
        retrieval_service: RetrievalService,
        context_builder: ContextBuilder,
    ):
        self.retrieval_service = retrieval_service
        self.context_builder = context_builder

    def answer(
        self,
        question: str,
    ) -> str:
        """
        Answer a question using retrieved context.
        """

        print("1. Retrieving documents...")

        matches = self.retrieval_service.retrieve(
            question,
        )

        print(f"2. Retrieved {len(matches)} chunks")

        print("3. Building prompt...")

        prompt = self.context_builder.build(
            question,
            matches,
        )

        print("4. Calling LLM...")

        response = chat(prompt)

        print("5. LLM finished")

        return response