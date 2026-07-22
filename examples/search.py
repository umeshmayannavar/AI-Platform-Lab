from ai_platform.retriever import Retriever


def main():

    retriever = Retriever()

    query = input(
        "Search Query: "
    )

    print()

    results = retriever.retrieve(query)

    print("=" * 60)

    print("Top Matches")

    print("=" * 60)

    for index, result in enumerate(results, start=1):

        print()

        print(f"Match #{index}")

        print(f"Score : {result['score']:.4f}")

        print(f"Source: {result['source']}")

        print()

        print(result["text"])

        print("-" * 60)


if __name__ == "__main__":
    main()