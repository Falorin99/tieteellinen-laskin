
"""Matemaattisten lausekkeiden käsittelyn ensimmäiset algoritmit."""

PRECEDENCE = {"+": 1, "-": 1, "*": 2, "/": 2}


def tokenize(expression: str) -> list[str]:
    """Jakaa lausekkeen kokonaislukuihin, operaattoreihin ja sulkuihin.

    Args:
        expression: Käyttäjän kirjoittama matemaattinen lauseke.

    Returns:
        Lista lausekkeen tokeneista merkkijonoina.

    Raises:
        ValueError: Jos lausekkeessa on tuntematon merkki.
    """
    tokens = []
    number = ""

    for char in expression:
        if char.isdigit():
            number += char
            continue

        if number:
            tokens.append(number)
            number = ""

        if char.isspace():
            continue
        if char in "+-*/()":
            tokens.append(char)
        else:
            raise ValueError(f"Tuntematon merkki: {char}")

    if number:
        tokens.append(number)

    return tokens


def to_postfix(tokens: list[str]) -> list[str]:
    """Muuntaa tokenit postfix-muotoon Shunting-yard-algoritmilla.

    Args:
        tokens: Kokonaisluvut, binäärioperaattorit ja sulut tokeneina.

    Returns:
        Postfix-järjestyksessä oleva tokenlista.

    Raises:
        ValueError: Jos sulut eivät täsmää tai token on tuntematon.
    """
    output = []
    operators = []

    for token in tokens:
        if token.isdigit():
            output.append(token)
        elif token in PRECEDENCE:
            while (
                operators
                and operators[-1] in PRECEDENCE
                and PRECEDENCE[operators[-1]] >= PRECEDENCE[token]
            ):
                output.append(operators.pop())
            operators.append(token)
        elif token == "(":
            operators.append(token)
        elif token == ")":
            while operators and operators[-1] != "(":
                output.append(operators.pop())
            if not operators:
                raise ValueError("Sulkeva sulku ilman avaavaa sulkua")
            operators.pop()
        else:
            raise ValueError(f"Tuntematon token: {token}")

    while operators:
        operator = operators.pop()
        if operator == "(":
            raise ValueError("Avaava sulku ilman sulkevaa sulkua")
        output.append(operator)

    return output
