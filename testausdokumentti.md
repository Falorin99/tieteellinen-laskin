# Testausdokumentti

## Yksikkötestaus

Projektissa käytetään pytest-kirjastoa yksikkötestien suorittamiseen. Testit sijaitsevat tests/test_calculator.py-tiedostossa.

Testauksen tarkoituksena on varmistaa laskimen algoritmien oikeellisuus.

## Testatut ominaisuudet

Projektin ensimmäisessä testausvaiheessa on testattu:

- Matemaattisten lausekkeiden tokenisointi.
- Kokonaislukujen käsittely.
- Välilyöntien käsittely.
- Operaattoreiden prioriteetit.
- Sulkulausekkeiden käsittely.
- Virheellisten merkkien tunnistaminen.
- Virheellisten sulkulausekkeiden tunnistaminen.

## Testisyötteet

| Lauseke | Odotettu postfix-muoto |
|---|---|
| 2+3 | 2 3 + |
| 2+3*4 | 2 3 4 * + |
| (2+3)*4 | 2 3 + 4 * |
| 12+35*4 | 12 35 4 * + |

## Testikattavuus

Kolmannen viikon automaattisessa testauksessa saatiin seuraavat tulokset:

| Mittari | Tulos |
|---|---:|
| Yksikkötestien määrä | 7 |
| Läpäistyt testit | 7 |
| Epäonnistuneet testit | 0 |
| Testikattavuus | 91 % |
| Koodilauseet | 44 |
| Suorittamatta jääneet koodilauseet | 3 |
| Haarautumiset | 32 |
| Osittain katetut haarautumiskohdat | 4 |

Testikattavuuden mittauksessa huomioitiin myös ohjelman haarautumiset.

Tulokset koskevat projektin aikaisempaa versiota, ja testikattavuus mitataan uudelleen uusien ominaisuuksien toteuttamisen jälkeen.

## Automaattinen testaus

GitHub Actions suorittaa yksikkötestit automaattisesti repositorioon tehtävien muutosten yhteydessä.

Riippuvuuksien hallintaan käytetään Poetrya ja testikattavuuden mittaamiseen coverage-työkalua.

## Täydentävä testaus

Yksikkötestauksen lisäksi suunnitteilla on integraatio- ja suorituskykytestausta.

Tarkoituksena on testata:

- Pitkiä matemaattisia lausekkeita.
- Sisäkkäisiä sulkulausekkeita.
- Desimaalilukuja ja negatiivisia lukuja.
- Muuttujien käsittelyä.
- Virheellisiä syötteitä.
- Nollalla jakamista.

Suorituskykytestauksessa voidaan käyttää esimerkiksi 100, 1000 ja 10000 yhteenlaskettavaa lukua.

## Testien suorittaminen

Riippuvuuksien asentaminen:

`poetry install`

Yksikkötestien suorittaminen:

`poetry run pytest`

Testikattavuuden mittaaminen:

`poetry run coverage run --branch -m pytest`

Testikattavuusraportin näyttäminen:

`poetry run coverage report -m`
