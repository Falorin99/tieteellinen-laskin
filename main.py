from calculator import tokenize, to_postfix


def main() -> None:
    """Lukee lausekkeita ja näyttää niiden tokenit sekä postfix-muodon."""
    print("Tieteellinen laskin")
    print("Kirjoita 'exit' lopettaaksesi.")

    while True:
        expression = input("Lauseke: ").strip()

        if expression.lower() == "exit":
            break
        if not expression:
            print("Anna matemaattinen lauseke.")
            continue

        try:
            tokens = tokenize(expression)
            postfix = to_postfix(tokens)
            print("Tokenit:", tokens)
            print("Postfix:", " ".join(postfix))
        except ValueError as error:
            print("Error:", error)


if __name__ == "__main__":
    main()
