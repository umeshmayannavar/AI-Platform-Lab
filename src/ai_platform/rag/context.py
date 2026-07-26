"""
Prompt construction utilities for Retrieval-Augmented Generation.
"""


class ContextBuilder:
    """
    Converts retrieved chunks into an LLM prompt.
    """

    def build(
        self,
        question: str,
        matches: list[dict],
    ) -> str:

        if not matches:
            context = "No relevant context found."
        else:
            context = "\n\n".join(
                [
                    f"[Document {i}]\n{match['text']}"
                    for i, match in enumerate(matches, start=1)
                ]
            )

        return f"""You are an AI assistant answering questions about the indexed documents.

Instructions:
- Answer ONLY using the provided context.
- If the answer is not present in the context, say:
  "I don't know based on the indexed documents."
- Do not make up facts.

Context
=======

{context}

Question
========

{question}

Answer
======"""