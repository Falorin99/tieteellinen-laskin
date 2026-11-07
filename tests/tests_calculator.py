"""Ensimmäiset yksikkötestit lausekkeiden käsittelylle."""

import pytest

from calculator import tokenize, to_postfix


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
