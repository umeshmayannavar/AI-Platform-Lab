from ai_platform.indexer import Indexer


def main():

    indexer = Indexer()

    indexer.index_directory(
        "documents"
    )


if __name__ == "__main__":
    main()