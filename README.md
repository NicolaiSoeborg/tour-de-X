# tour-de-X
Nem planlægning af Tour-de-X

Åben `app.py` i din ynglings editor og ændre:

```
DTU bygning 101, lyngby
Bagsværd Station
Lautrupvang 15, 2750 Ballerup
Nørreport Station
Rævehøjvej 36, 2800 Kongens Lyngby
```

til listen af addresser på turen.

Sørg for at du har de rigtige python pakker installeret (`pip3 install -r requirements.txt`) og kør `python3 app.py`.

Et Google Chrome browser vil åbne og hente offentlig transport tider fra Google Maps. Husk at krydse fingre for at det virker!

Når dette er færdigt (tager ca: `(antal adresser)^2 x 2 sekunder`) findes den bedste sti mellem alle adresserne (via 2-OPT TSP).

Til sidst printes den endelige liste.


## Antagelser

 * Programmet bruger Google Maps til at finde den hurtigste rute mellem to adresser **HER OG NU**, dvs hvis du kører programmet om natten vil det finde natbusser/tog, men dette er næppe optimalt hvis din Tour-de-X foregår om dagen (og vice versa).

 * Der bliver ikke brugt en officiel Google API, så der er en chance for at Google blokkere dig eller giver dig en CAPTCHA.  Du burde egentlig bare kunne klare CAPTCHA i browser vinduet og så skulle programmet gerne fortsætte, men det er skrevet meget hurtigt og er ret ustabilt, så det virker nok ikke i praksis.

 * Programmet bruger en uhyre dårlig måde at regne "google tid" (fx `1 t 45 min`) om til minutter (i.e. `1*60+45` fra forrige eksempel).  Det har virket i mine test, men burde laves om.  Jeg modtager gerne Pull Requests :-)


# Example
![](example.gif)
