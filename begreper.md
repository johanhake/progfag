---
  export_on_save:
    html: true
---

# Begreper

## Program
Et set med operasjoner som får en datamaskin til å utføre noe.

### Beskrivelse
Et program eller en app (applikasjon) er et set med [operasjoner](#operasjon) som får en datamaskin til å utføre noe. Når dette skjer sier man ofte at man *kjører* programmet. Hvis vi bruker en mobiltelefon eller en datamaskin kjører vi nesten altid et eller annet program, f eks sms-appen til telefonen eller Microsoft Word på datamaskinen. Et program lages ved at man [programmerer](#programmere) eller koder det og det kjøres ved at man laster programmet inn i [arbeidsminne](#arbeidsminnet) til mobiltelefonen eller datamaskinen.

## Arbeidsminne
Er et sted i datamaskinen hvor programmer lagres.

### Beskrivelse
Når et program kjøres lastes det inn i arbeidsminnet til en datamaskin. Er programmet komplisert, har mange [operasjoner](#operasjon), tar det også større plass i arbeidsminnet.

Arbeidsminnet til en datamaskin kalles også for RAM (Random Access Memory).

## Programmere
Å lage et program 

### Beskrivelse
Når du lager et [program](#program) sier vi at du programmerer eller koder programmet. Da setter du sammen [operasjoner](#operasjon) som får datamaskinen til å gjøre det du vill den skal gjøre. Operasjonene kan enten skrives i en tesktfil, [tekstprogrammering](#teksprogrammering) eller settes sammen grafiskt gjennom blokker, [blokkprogrammering](#blokkprogrammering). Blokkprogrammering kan være enklere å bruke når du skal lære deg programmering og tekstprogrammering brukes gjerne for mer komplekse programmer. Uanset om du velger tekst eller blokk-programmering må du velge et eller annet [programmeringsspråk](#programmeringsspråk) som du koder i.

## Tekstprogrammering
Programmering hvor operasjoner skrives i tekstfiler.

### Beskrivelse
I tekstprogrammering består [operasjoner](#operasjon) av instruksjoner satt sammen av ord og tall. Operasjonene utføres så linje for linje i en rekkefølge som går fra toppen av filen mot bunnen og i hver linje utføres de fra høyre mot venstre. *ILLUSTRASJON* Tekstfilene kan så enten *kjøres* direkte gjennom en [kommandotolk](#kommandotolk) (*interpreter* eng.) og filene kalles da for et *skript*, eller kan filene gjøres om til egne program gjennom å [kompilere](#kompilere) de. Vi kommer bare lage skript når vi bruker tekstprogrammering. Alle apper som installeres på en datamaskin er eksempler på kompilerte program. 

Tekstprogrammering må følge fastlagde regler som bestemmes av hvilket [programmeringsspråk](#programmeringspråk) du koder i. Reglene kalles for [syntaksen](#syntaks) til programmeringsspråket. 

## Kompilere
Lage et kjørbart program av en tekstfil.

### Beskrivelse
En type av tekstprogammering 

## Blokkprogrammering
Programmering hvor operasjonene settes sammen grafisk gjennom ulike blokker.

### Beskrivelse
I blokkprogrammering består [operasjoner](#operasjon) av blokker som settes sammen grafisk i et eget program. Det er oftest lettest å komme igang å programmere gjennom å bruke blokkprogrammering da betydningen til operasjonene mange ganger lett kan visualiseres gjennom utseendet til de ulike blokkene. 

## Syntaks
Regler for hvordan operasjoner skrives innen tekstprogrammering.

### Beskrivelse
Ved [tekstprogrammering](#tekstprogrammering) skriver man alle operasjoner med bokstaver og tegn. Syntaksen til et tekst-programmeringsspråk er regler som bestemmer hvordan bokstavene kan skrives. På samme måte som syntaksen til skriftlig norsk bestemmer hvordan norsk kan skrives, f. eks. en setning starter med stor bokstav og slutter med et punkt, bestemmer syntaksen til tekstprogrammering hvordan operasjoner kan skrives i en tekstfil.

### Eksempel
Syntaksen for å tildele to variabler hver sin verdi og å lage en kommentar er forskjellige for ulike programmeringsspråk. Her viser vi hvordan det ser ut for Python og JavaScript. Vi ser at det er flere ting som er likt men også noen ting som skiller de to språkene.

#### Python
```python
# Alder og høyde til en person
alder = 9
høyde = 1.34
```

#### JavaScript
```javascript
// Alder og høyde til en person
let alder = 9;
let høyde = 1.34;
```

## Kommandotolk
Et program som kjører et skript.

### Beskrivelse
Noen filer som lages ved [tekstprogrammering](#tekstprogrammering) trenger et eget program, kommandotolk, for å kunne kjøres. Tekstfilene med programmet kalles da for skript. 

### Eksempel
Et python-skript trenger en kommandotolk for å kunne kjøres. Hvis man har installert python på datamaskinen kan man kjøre et python-skript gjennom å bruke kommandotolken python forran filnavnet til skriptet. 
```bash
> python mitt-program.py
```

## Programmeringsspråk
Et språk som beskriver hvordan operasjoner settes sammen i et program.

### Beskrivelse
Når man [programmerer](#programmere) må man velge et programmeringsspråk man skal bruke for å sette sammen de ulike [operasjonene](#operasjon). Det finnes mange ulike programmeringsspråk som kan brukes til enten [tekstprogrammering](#tekstprogrammering) eller [blokkprogrammering](#blokkprogrammering). De finnes aller flest tekst-programmeringsspråk i verden da disse er enklere å bruke når man skal lage større program.

#### Eksempler på tekst-programmeringsspråk som trenger en kommandotolk
* Python - brukes mye for å regne med matematikk
* JavaScript - brukes til å styre en nettside

#### Eksempler på tekst-programmeringsspråk som må kompileres
* C - brukes til å programmere kjernen til Android
* C++ - brukes til å programmere Windows

#### Eksempler på blokk-programmeringsspråk
* Scratch - brukes til å programmere enkle spill
* Blokkuino - brukes til å styre en arduino

## Algoritme
Beskrivelse av 

### Beskrivelse

## Operasjon
En enkelt ting en datamaskin skal gjøre.

### Beskrivelse
En operasjon forteller datamaskinen at den skal gjøre noe. Et [program](#program) er mange operasjoner som er satt sammen etter hverandre. En operasjon kan være enkel, f eks å legge sammen to tall eller å kaste en terning (gjennom å kjøre en funksjon). Operasjonen kan også være sammensatt for eksempel å regne ut et gjennomsnitt av flere tall.

### Eksempel
Eksempler på operasjoner som kan skrives på en rad
```python
# Legger sammen to tall og lagrer resultatet i en variabel
resultat = 5+7

# Viser resultatet fra en terningskast 
print(terning());

# Regner ut gjennomsnittet til 5 ulike verdier
gjennomsnitt = (14+16+9+18+14)/5
```

## Variabel
Er et navngitt sted i arbeidsminnet som holder spesifikke verdier.

### Beskrivelse
En variabel er et navngitt sted i arbeidsminnet som holder på en eller flere verdier i et program. Navnet til variablen anvendes til enten å bruke verdien til variablen eller å endre verdien til den. 

En variabel brukes i et program istedenfor en konkret verdi. Istedenfor å bruke verdien, for eksempel 2 for antallet desiliter melk du har til en porsjon havregrøt kan du bruke en variabel for denne verdien:
```python
havregryn = 1
melk = 2
```

Bruke antall porsjoner... FORTS!

Du bestemmer selv hva navnet til en variabel skal være, men [syntaksen](#syntaks) til programmeringsspråket begrenser ofte hvordan navnet kan skrives, for eksempel kan man ikke ha mellomrom eller bindestrek i et [variabelnavn](#variabelnavn) i noen tekst-programmeringsspråk. Hvert variabelnavn må også være unikt, man kan altså ikke ha flere variabler med samme navn. 

Når man lager en variabel for første gangen sier man at man [definerer](#definere) den. Man kan ikke bruke en variabel før den er definert.  

Ordet variabel brukes også innen algebran i matematikken, men da oftest til å betegne en ukjent tallverdi, f. eks. *x, y*. Innen programmering har en variabel *alltid* en verdi og representerer altså ikke noe ukjent. Men en variabel brukes gjerne innen programmering når man vil

## Variabelnavn
Navnet til en variabel.

### Beskrivelse
En variabel har altid et navn FORTS! 
og det er det navnet du bruker for å representerer 
Det er noen regler FORTS!


## Definere
Operasjon som lager en variabel eller funksjon.

### Beskrivelse
For å kunne bruke en [variabel](#variabel) eller [funksjon](#funksjon) må de først defineres. Enkelt sagt betyr det å si ifra at vi skal ha en variabel eller funksjon med et spesifikt navn. Navnet brukes så i programmet for å representere enten verdien til variabelen eller alle operasjonen til funksjonen.  

I tilegg til å få et navn må en variabel også få en verdi når den defineres. En funksjon må også få et set med operasjoner som skal utføres hver gang man kaller eller kjører funksjonen. I noen [programmeringsspråk](#programmeringsspråk) kan man si ifra at man skal bruke en variabel uten å gi den en verdi. Da heter det å *deklarere* en variabel. 

## Løkke
Operasjoner som repeteres flere ganger.

### Beskrivelse

## Funksjon
Operasjoner som lagres til et navn.

### Beskrivelse
En funksjon brukes til å lagre et sett med operasjoner til et navn. Operasjonene som lagres i en funksjon må utføre en spesifikk oppgave slik at man bruker funksjonens navn istedenfor alle operasjonene når programmet skal utføre oppgaven. Når funksjonen brukes heter det at man [kaller](#kalle) funksjonen. Når en funksjon blir kallet blir alle operasjonene til funksjonen utført og slik blir også oppgaven til funksjonen utført. En funksjon likner på en variabel med at den har et navn og noe blir lagret til navnet, men en funksjon lagrer operasjoner hvor en variabel bare lagrer verdier.

### Eksempel


## Kalle
Utføre operasjoner knyttet til en funksjon

### Beskrivelse


## Argument
Verdier man kan gi til en funksjon når man kaller den

## Tilordne
Når man gir en verdi til en variabel

