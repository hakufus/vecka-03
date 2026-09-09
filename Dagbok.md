7 sept
Idag har jag gjort python uppgifterna och börjat på norviks större nätverk. alla datorerna får ip men dom kan ej pinga varandra. Tränat på github i terminalen via visual studio.

8 sept
Idag har jag kört veckan python script. jag har sett till att datorerna kan pinga varandra och börjat med att lägga in uppgifterna i github. Tagit screenshot på mitt norvik nätverk
innan det flyter på som vanligt.
Jag förstår hur man räknar och läser på subnet och hur man lånar en för att det blir mindre addresser på ett nät. Jag har förstått det men använder verktyg till detta som räknar själv.

9 sept.
Vad är skillnaden mellan running-config och startup-config? 
Skillnaden mellan running-config och startup-config handlar om var i routerns eller switchens minne konfigurationen sparas och vad som händer vid avbrott omstart.
Running config är den som kör just nu på switchen/routen men om du ändrar något så sparas inte dina andringar.
Startup-config är det inställningen som körs vid varje uppstart. Den läser in från filen på routen/switchen.

Vilket lager arbetar en switch på, och vilket arbetar en router på?
En switch jobbar på layer 2 och router jobbar på layer 3

Din dator vill nå en server i ett annat land. Vilken MAC-adress
frågar den efter, och varför?
Din dator använder mac-adressen inom det lokala nätverket för att kommunicera inom nätverket. Utanför gatewayen är det din ip adress som körs.

Sätt nu masken 255.255.255.0 på datorn i stället, men behåll adressen. Når
den fortfarande gatewayen? Varför?
Vi antar att datorn ligger inom det första intervallet i det delade nätverkets ipnummer. datorn kan göra en arp och få svar från gatewayen då den ligger inom samma nätverk. 255.255.255 är nätverket och .0 är host. så det går att skicka signalen till gateway.

Ta bort gatewayen på datorn. Når den fortfarande servern i samma nät? Når
den internet? Den när fortfarande servern men den kan  ej gå ut på internet.

Idag är det kontrollfrågor och räkna subnet
