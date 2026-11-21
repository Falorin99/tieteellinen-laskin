# Käyttöohje

## Vaatimukset

- Python 3.10 tai uudempi
- Poetry

## Asennus

Lataa projekti GitHub-repositoriosta.

Siirry projektin juurihakemistoon ja asenna tarvittavat riippuvuudet komennolla:

`poetry install`

## Ohjelman käynnistäminen

`poetry run python main.py`

## Laskimen käyttäminen

Laskimen algoritminen ydin käsittelee matemaattisia lausekkeita sekä huomioi operaattoreiden prioriteetit ja sulut.

Esimerkkejä:

| Lauseke | Odotettu tulos |
|---|---:|
| 2+3 | 5 |
| 10-4 | 6 |
| 5*6 | 30 |
| 10/4 | 2.5 |
| 2+3*4 | 14 |
| (2+3)*4 | 20 |

## Kehitteillä olevat ominaisuudet

Käyttöohjetta täydennetään muuttujien, desimaalilukujen, negatiivisten lukujen ja tieteellisten laskutoimitusten käyttöesimerkeillä toteutuksen valmistuttua.

Käyttöliittymän toiminta tarkistetaan ennen vertaisarviointia.

## Testaus

Yksikkötestit voidaan suorittaa komennolla:

`poetry run pytest`
