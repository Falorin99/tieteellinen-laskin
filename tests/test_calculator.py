"""Ensimmäiset yksikkötestit lausekkeiden käsittelylle."""

import pytest
from calculator import tokenize, to_postfix, calculate


def test_tokenize_basic_expression():
    assert tokenize("2+3") == ["2", "+", "3"]


def test_tokenize_multidigit_numbers():
    assert tokenize("12+35*4") == ["12", "+", "35", "*", "4"]


def test_tokenize_spaces_and_parentheses():
    assert tokenize("(12 + 3) * 4") == [
        "(", "12", "+", "3", ")", "*", "4"
    ]


def test_tokenize_rejects_unknown_character():
    with pytest.raises(ValueError):
        tokenize("2+a")


def test_postfix_respects_precedence():
    assert to_postfix(tokenize("2+3*4")) == [
        "2", "3", "4", "*", "+"
    ]


def test_postfix_handles_parentheses():
    assert to_postfix(tokenize("(2+3)*4")) == [
        "2", "3", "+", "4", "*"
    ]


def test_postfix_rejects_unmatched_parenthesis():
    with pytest.raises(ValueError):
        to_postfix(tokenize("(2+3"))


def test_calculate_basic_expression():
    assert calculate("2+3*4") == 14


def test_calculate_decimal_numbers():
    assert calculate("2.5+3.5") == pytest.approx(6.0)


def test_calculate_negative_number():
    assert calculate("-5+3") == -2


def test_calculate_negative_in_parentheses():
    assert calculate("2*(-3)") == -6


def test_calculate_subtract_negative():
    assert calculate("10-(-5)") == 15


def test_calculate_negative_expression():
    assert calculate("-(2+3)") == -5


def test_calculate_division_by_zero():
    with pytest.raises(ZeroDivisionError):
        calculate("10/0")


def test_calculate_invalid_decimal():
    with pytest.raises(ValueError):
        calculate("2.5.3+1")


def test_calculate_incomplete_expression():
    with pytest.raises(ValueError):
        calculate("2+")


def test_calculate_missing_operator():
    with pytest.raises(ValueError):
        calculate("2(3+4)")

