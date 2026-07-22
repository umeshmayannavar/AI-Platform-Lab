from ai_platform.retriever import Retriever


def test_retriever_creation():

    retriever = Retriever()

    assert retriever is not None