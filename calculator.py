

"""Matemaattisten lausekkeiden käsittely ja laskeminen."""

import re


PRECEDENCE = {
    "+": 1,
    "-": 1,
    "*": 2,
    "/": 2,
    "NEG": 3
}


def is_number(token: str) -> bool:
    """Tarkistaa, onko token kokonaisluku tai desimaaliluku.

    Args:
        token: Tarkistettava merkkijono.

    Returns:
        True, jos token on kelvollinen luku.
    """
    return re.fullmatch(r"(?:[0-9]+(?:\.[0-9]*)?|\.[0-9]+)", token) is not None


def tokenize(expression: str) -> list[str]:
    """Jakaa lausekkeen lukuihin, operaattoreihin ja sulkuihin.

    Args:
        expression: Käyttäjän kirjoittama matemaattinen lauseke.

    Returns:
        Lista lausekkeen tokeneista merkkijonoina.

    Raises:
        ValueError: Jos syöte sisältää virheellisen merkin tai luvun.
    """
    tokens = []
    index = 0

    while index < len(expression):
        char = expression[index]

        if char.isspace():
            index += 1
            continue

        if char in "0123456789.":
            start = index

            while (
                index < len(expression)
                and expression[index] in "0123456789."
            ):
                index += 1

            number = expression[start:index]

            if not is_number(number):
                raise ValueError(f"Virheellinen luku: {number}")

            tokens.append(number)
            continue

        if char in "+-*/()":
            tokens.append(char)
        else:
            raise ValueError(f"Tuntematon merkki: {char}")

        index += 1

    return tokens


def to_postfix(tokens: list[str]) -> list[str]:
    """Muuntaa tokenit postfix-muotoon Shunting-yard-algoritmilla.

    Args:
        tokens: Luvut, operaattorit ja sulut tokeneina.

    Returns:
        Postfix-järjestyksessä oleva tokenlista.

    Raises:
        ValueError: Jos lausekkeen rakenne on virheellinen.
    """
    output = []
    operators = []
    expect_operand = True

    for token in tokens:
        if is_number(token):
            if not expect_operand:
                raise ValueError("Operaattori puuttuu")

            output.append(token)
            expect_operand = False

        elif token in "+-*/" and len(token) == 1:
            # Miinus voi olla myös unaarinen operaattori.
            if expect_operand:
                if token == "-":
                    operators.append("NEG")
                    continue

                raise ValueError("Virheellinen operaattori")

            while (
                operators
                and operators[-1] in PRECEDENCE
                and PRECEDENCE[operators[-1]] >= PRECEDENCE[token]
            ):
                output.append(operators.pop())

            operators.append(token)
            expect_operand = True

        elif token == "(":
            if not expect_operand:
                raise ValueError("Operaattori puuttuu")

            operators.append(token)

        elif token == ")":
            if expect_operand:
                raise ValueError("Virheellinen sulkulauseke")

            while operators and operators[-1] != "(":
                output.append(operators.pop())

            if not operators:
                raise ValueError("Sulkeva sulku ilman avaavaa sulkua")

            operators.pop()
            expect_operand = False

        else:
            raise ValueError(f"Tuntematon token: {token}")

    if expect_operand:
        raise ValueError("Keskeneräinen lauseke")

    while operators:
        operator = operators.pop()

        if operator == "(":
            raise ValueError("Avaava sulku ilman sulkevaa sulkua")

        output.append(operator)

    return output


def evaluate_postfix(tokens: list[str]) -> float:
    """Laskee postfix-muodossa olevan lausekkeen arvon.

    Args:
        tokens: Postfix-muodossa oleva tokenlista.

    Returns:
        Matemaattisen lausekkeen arvo.

    Raises:
        ValueError: Jos lauseke on virheellinen.
        ZeroDivisionError: Jos jakaja on nolla.
    """
    stack = []

    for token in tokens:
        if is_number(token):
            stack.append(float(token))

        elif token == "NEG":
            if not stack:
                raise ValueError("Virheellinen lauseke")

            stack.append(-stack.pop())

        elif token in PRECEDENCE:
            if len(stack) < 2:
                raise ValueError("Virheellinen lauseke")

            right = stack.pop()
            left = stack.pop()

            if token == "+":
                result = left + right
            elif token == "-":
                result = left - right
            elif token == "*":
                result = left * right
            else:
                result = left / right

            stack.append(result)

        else:
            raise ValueError(f"Tuntematon token: {token}")

    if len(stack) != 1:
        raise ValueError("Virheellinen lauseke")

    return stack[0]


def calculate(expression: str) -> float:
    """Laskee matemaattisen lausekkeen arvon.

    Args:
        expression: Käyttäjän kirjoittama matemaattinen lauseke.

    Returns:
        Lausekkeen laskettu arvo.
    """
    tokens = tokenize(expression)
    postfix = to_postfix(tokens)

    return evaluate_postfix(postfix)


