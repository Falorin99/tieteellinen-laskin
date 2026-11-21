# Toteutusdokumentti

## Ohjelman yleisrakenne

Harjoitustyössä toteutetaan Pythonilla tieteellinen laskin. Ohjelman tarkoituksena on käsitellä matemaattisia lausekkeita ja laskea niiden arvoja.

Ohjelman algoritminen ydin on erotettu käyttöliittymästä.

- calculator.py sisältää laskimen algoritmit.
- main.py sisältää tekstipohjaisen käyttöliittymän.
- tests/test_calculator.py sisältää yksikkötestit.
- pyproject.toml sisältää projektin asetukset ja riippuvuudet.

## Käytetyt algoritmit

### Tokenisointi

Tokenisoinnissa matemaattinen lauseke jaetaan lukuihin, operaattoreihin ja sulkuihin.

Esimerkiksi lauseke `2+3*4` jaetaan tokeneihin `2`, `+`, `3`, `*` ja `4`.

### Shunting-yard-algoritmi

Shunting-yard-algoritmi muuntaa matemaattisen lausekkeen postfix-muotoon huomioiden operaattoreiden prioriteetit ja sulut.

Esimerkiksi lauseke `2+3*4` muunnetaan muotoon `2 3 4 * +`.

### Postfix-lausekkeiden evaluointi

Postfix-lausekkeiden evaluoinnissa käytetään pinoa. Luvut lisätään pinoon, ja operaattorin kohdalla pinosta poistetaan tarvittavat operandit.

Laskutoimituksen tulos lisätään takaisin pinoon. Lopuksi pinossa on lausekkeen laskettu arvo.

## Tietorakenteet

Ohjelmassa käytetään Pythonin listoja tokenien ja laskennan välitulosten tallentamiseen sekä pinojen toteuttamiseen.

Muuttujien tallentamiseen on suunniteltu käytettäväksi Pythonin sanakirjaa.

## Aika- ja tilavaativuus

Shunting-yard-algoritmin aikavaativuus on O(n), missä n on tokenien lukumäärä.

Postfix-lausekkeiden evaluoinnin aikavaativuus on peruslaskutoimituksilla O(n), kun yksittäisten laskutoimitusten oletetaan vievän vakioaika.

Molempien algoritmien tilavaativuus on O(n).

## Puutteet ja jatkokehitys

Projektin kehitys on vielä kesken. Seuraavaksi kehitetään muuttujien käsittelyä, tieteellisiä laskutoimituksia ja virheellisten syötteiden käsittelyä sekä laajennetaan testausta.

## Laajojen kielimallien käyttö

Projektin yhteydessä on käytetty ChatGPT:tä algoritmien opiskeluun, toteutuksen suunnitteluun, teknisten ongelmien ratkaisemiseen ja dokumentaation luonnosteluun. ChatGPT:ltä on saatu myös ohjelmakoodi- ja testiesimerkkejä.

Käytetyt mallit ja tekoälyn tuottaman materiaalin hyödyntäminen täsmennetään toteutuksen edetessä.

## Lähteet*

-

*Lista muuttuu ajan myötä
