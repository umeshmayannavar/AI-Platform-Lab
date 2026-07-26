"""
Retrieval-Augmented Generation service.
"""

from ai_platform.llm import chat
from ai_platform.rag.context import ContextBuilder
from ai_platform.retrieval.service import RetrievalService


class RAGService:
    """
    End-to-end RAG orchestration.
    """

    def __init__(
        self,
        retrieval_service: RetrievalService,
    ):
        self.retrieval_service = retrieval_service
        self.context_builder = ContextBuilder()

    def answer(
        self,
        question: str,
    ) -> str:

        matches = self.retrieval_service.retrieve(
            question
        )

        prompt = self.context_builder.build(
            question,
            matches,
        )

        return chat(prompt)