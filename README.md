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

Når dette er færdigt (tager ca: `antal adresser x 2 sekunder`) findes den bedste sti mellem alle adresserne (via 2-OPT TSP).

Til sidst printes den endelige liste.

# Example
![](example.gif)
