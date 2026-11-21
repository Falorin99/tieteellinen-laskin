# Tieteellinen laskin

Algoritmit ja tekoäly -kurssin harjoitustyö.

## Projektin kuvaus

Projektin tavoitteena on toteuttaa Pythonilla tieteellinen laskin.

Laskimen algoritminen ydin perustuu Shunting-yard-algoritmiin ja postfix-lausekkeiden evaluointiin.

## Toiminnallisuus

- Matemaattisten lausekkeiden tokenisointi.
- Peruslaskutoimitukset.
- Operaattoreiden prioriteettien huomioiminen.
- Sulkulausekkeiden käsittely.
- Postfix-lausekkeiden evaluointi.

Kehitteillä ovat muuttujien käsittely, desimaaliluvut, negatiiviset luvut ja määrittelydokumentin mukaiset tieteelliset laskutoimitukset.

## Asennus

`poetry install`

## Ohjelman käynnistäminen

`poetry run python main.py`

## Testaus

`poetry run pytest`

## Testikattavuus

`poetry run coverage run --branch -m pytest`

`poetry run coverage report -m`

## Pylint

`poetry run pylint calculator.py main.py`

## Dokumentaatio

- [Määrittelydokumentti](dokumentaatio/maarittelydokumentti.md)
- [Toteutusdokumentti](dokumentaatio/toteutusdokumentti.md)
- [Testausdokumentti](dokumentaatio/testausdokumentti.md)
- [Käyttöohje](dokumentaatio/kayttoohje.md)

## Viikkoraportit

- [Viikkoraportti 1](dokumentaatio/viikkoraportti1.md)
- [Viikkoraportti 2](dokumentaatio/viikkoraportti2.md)
- [Viikkoraportti 3](dokumentaatio/viikkoraportti3.md)
- [Viikkoraportti 4](dokumentaatio/viikkoraportti4.md)

## Teknologiat

- Python
- Poetry
- Pytest
- Coverage
- Pylint
- GitHub Actions
