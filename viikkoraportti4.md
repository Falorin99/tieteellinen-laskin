# Viikkoraportti 4

## Mitä olen tehnyt tällä viikolla?

Tällä viikolla olen keskittynyt laskimen algoritmisen ytimen kehittämiseen sekä projektin valmisteluun vertaisarviointia varten.

Olen jatkanut Shunting-yard-algoritmin kehittämistä ja laajentanut laskimen toimintaa postfix-muotoisten lausekkeiden evaluointiin. Laskimen algoritminen ydin pystyy käsittelemään peruslaskutoimituksia ja huomioimaan operaattoreiden prioriteetit sekä sulut.

Lisäksi olen suunnitellut desimaalilukujen, negatiivisten lukujen, muuttujien ja potenssilaskujen käsittelyä.

Olen myös perehtynyt toteutusdokumentin, testausdokumentin ja käyttöohjeen sisältöön sekä valmistellut niiden ensimmäisiä versioita.

## Miten ohjelma on edistynyt?

Ohjelman algoritminen rakenne on selkeytynyt huomattavasti projektin alkuvaiheeseen verrattuna. Lausekkeiden käsittely on jaettu kolmeen päävaiheeseen: tokenisointiin, postfix-muotoon muuntamiseen ja evaluointiin.

Tällainen rakenne helpottaa yksittäisten algoritmien kehittämistä, testaamista ja mahdollisten virheiden löytämistä.

Projektissa on käytössä Poetry sekä GitHub Actions automaattista testausta ja testikattavuuden mittaamista varten.

## Mitä olen oppinut?

Olen oppinut ymmärtämään paremmin pinorakenteen hyödyntämistä matemaattisten lausekkeiden käsittelyssä.

Erityisesti operaattoreiden prioriteettien ja operandien järjestyksen merkitys on tullut selkeämmäksi. Esimerkiksi vähennys- ja jakolaskuissa operandien järjestyksellä on suuri merkitys lopputuloksen kannalta.

Olen myös perehtynyt unaarisen miinusoperaattorin ja tavallisen vähennyslaskun väliseen eroon sekä siihen, miten muuttujia voidaan käsitellä osana matemaattisia lausekkeita.

Testauksen osalta olen ymmärtänyt paremmin, ettei korkea testikattavuus yksinään takaa ohjelman virheettömyyttä.

## Mikä jäi epäselväksi tai tuotti vaikeuksia?

Haastavimpia asioita ovat olleet negatiivisten lukujen käsittely yhdessä muiden operaattoreiden kanssa sekä erilaisten virheellisten matemaattisten lausekkeiden tunnistaminen.


## Mitä teen seuraavaksi?

Seuraavalla viikolla tavoitteena on:

- Viimeistellä laskimen algoritminen ydin.
- Kehittää muuttujien tallentamista ja käyttämistä lausekkeissa.
- Toteuttaa määrittelydokumentin mukaisia tieteellisiä laskutoimituksia.
- Kehittää käyttöliittymää ja virhetilanteiden käsittelyä.
- Laajentaa yksikkötestausta ja täydentävää testausta.
- Tarkistaa koodin laatu Pylintin avulla.
- Täydentää projektin dokumentaatiota.
- Huomioida vertaisarvioinnista saatava palaute.

Tämän viikon aikajana:
Ti 17.11. Algoritmien kehittäminen ja postfix-lausekkeiden evaluointi, 4 tuntia
To 19.11 Operaattoreiden, muuttujien ja virhetilanteiden käsittelyn suunnittelu, 4 tuntia 
La 21.11. Testauksen ja dokumentaation kehittäminen sekä vertaisarviointiin valmistautuminen, 3 tuntia
