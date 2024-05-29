# Finals projekts

**Katrs punkts - 0,5 balle**

## Prezentācija
 - Analīze - problēmas apraksts, kāpēc problēma tika uzskatīta par aktuālo, kam tas noderētu, aprakstīti eksistējoši lidzīgi risinājumi
 - Specifikācija - aprakstītas funkcionālas un nefunkcionālas prasības
 - Iterācijas - sadalīt prasības uz vismaz diviem izstrādes posmiem
 - Izmantoti resursi - dokumentācija, linki
 - Risinājuma demonstrācija (var arī ekrānšaviņi)

## Izstrāde
 - Kods atbilst izvirzītam prasībam
 - Ir ievaddatu validācija (pārbaude ka tika ierakstīti korrekti dati)
 - Mainīgie rakstīti snake_case, bez saisinājumiem
 - Ir komentāri pirms if, for, while kosntrukcijam
 - Kods atbilst izvirzītam prasībam
 - Izmaiņas saglabātas Github repozitorijā
 - Izmaiņas saglabātas vairākas iterācijās (vairāki commit)
 - Izmantoti saraksti vai vārdnīcas vai klases
 - Izmantota jebkura bibliotēka (modulis uzinstalēts ar PIP un izmantots kodā) 
 - Izmantoti JSON faili vai SQLite datubāze datu glabāšanai

## Testēšana

 - 2 happy path
 - 4 use-cases
 - 4 edge-cases
 	Happy path
1.	Testa gadījums Valūtas maiņas kurss ir 1,0831. Konvertējot 10 EUR uz USD. Rezultātam jābūt 10,83 USD. 
2.	Testa gadījums Valūtas maiņas kurss ir 7,82. Konvertējot 15 EUR uz CNY. Rezultātam jābūt 117,3 CNY. 
	Use-cases 
1.	Testa gadījums Valūtas maiņas kurss ir 0,86. Konvertējot 987 EUR uz GBP. Rezultātam jābūt 848,82 GBP. 
2.	Testa gadījums Valūtas maiņas kurss ir 90,41. Konvertējot 197 USD uz INR. Rezultātam jābūt 16450,40 INR. 
3.	Testa gadījums  Valūtas maiņas kurss ir 0.99. Konvertējot 23435 EUR uz CHF. Rezultātam jābūt 23178.98 CHF. 
4.	Testa gadījums  Valūtas maiņas kurss ir 106.34. Konvertējot 9234 GBP uz INR. Rezultātam jābūt 981921.96INR. 
	Edge-cases
1.	Testa gadījums Valūtas maiņas kurss ir 1,0831. Konvertējot 0 EUR uz USD. Rezultātam jābūt 0 USD. 
2.	Testa gadījums Valūtas maiņas kurss ir 1,0831. Konvertējot -10 EUR uz USD. Sistēmai jāatgriež kļūdas ziņojums, norādot, ka summai jābūt lielākai par nulli. 
3.	Testa gadījums Valūtas maiņas kurss ir 1,0831. Konvertējot 10 EUR uz neatbalstītu valūtu  XYZ. Sistēmai jāatgriež kļūdas ziņojums, norādot, ka valūta nav atbalstīta. 
4.	Testa gadījums Valūtas maiņas kurss ir 1,0831. Nepareizs valūtas pāra formāts  sFh/Daw. Sistēmai jāatgriež kļūdas ziņojums, norādot, ka pareizais formāts ir “EUR/USD”.

