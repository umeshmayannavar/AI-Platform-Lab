from openai import OpenAI


class EmbeddingService:
    def __init__(self):
        self.client = OpenAI(
            base_url="http://localhost:4000",
            api_key="ai-platform-lab",
        )

    def embed(self, text: str):
        response = self.client.embeddings.create(
            model="embedding",
            input=text,
        )

        return response.data[0].embedding