Toteutan harjoitustyön Python-ohjelmointikielellä. Pythonin lisäksi minulla on kokemusta Java-, C-ohjelmointikielistä, joilla voin tarvittaessa tehdä vertaisarviointeja osaamiseni puitteissa.

Dokumentaatio kirjoitetaan suomeksi.

Opinto-ohjelmani on tietojenkäsittelytieteen kandidaattiohjelma (TKT).

Harjoitustyön aiheena on tieteellisen laskimen toteuttaminen Pythonilla.

Ohjelman tarkoituksena on käsitellä käyttäjän syöttämiä matemaattisia lausekkeita ja laskea niiden tulokset oikeassa laskujärjestyksessä. Laskin tukee peruslaskutoimituksia, sulkulausekkeita, potenssilaskuja sekä valittuja matemaattisia funktioita.

Ohjelma ei käytä Pythonin valmista eval()-funktiota lausekkeiden laskemiseen, vaan lausekkeiden käsittely toteutetaan itse.

Harjoitustyön keskeisenä algoritmina käytetään Shunting-yard-algoritmia, jonka avulla matemaattinen lauseke muunnetaan infiksimuodosta postfix-muotoon eli käänteiseen puolalaiseen notaatioon.

Postfix-muotoisen lausekkeen laskeminen toteutetaan pinoa hyödyntävällä algoritmilla.

Keskeiset tietorakenteet ovat:

Pino (stack), jota käytetään operaattoreiden ja laskennan välitulosten käsittelyyn.

Lista, johon tallennetaan lausekkeen osat ja muunnettu lauseke.

Lisäksi toteutetaan matemaattisen lausekkeen jäsentely tokeneiksi sekä virheellisten syötteiden tunnistaminen.

Harjoitustyön ydin on matemaattisten lausekkeiden jäsentäminen ja laskeminen itse toteutetuilla algoritmeilla.

Suurin osa kehitystyöstä keskittyy Shunting-yard-algoritmin toteuttamiseen, postfix-lausekkeiden laskemiseen sekä laskujärjestyksen ja sulkujen oikeaan käsittelyyn.

Käyttöliittymä toteutetaan yksinkertaisena komentorivisovelluksena, jotta työssä voidaan keskittyä algoritmien toteuttamiseen.
