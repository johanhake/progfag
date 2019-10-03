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

Et python-skript trenger en kommandotolk for å kunne kjøres. Hvis man har installert python på datamaskinen kan man kjøre skriptet gjennom å bruke kommandotolken `python` forran filnavnet til skriptet (`mitt-program.py`). 

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
En oppskrift med operasjoner som utfør en oppgave.

### Beskrivelse
En algoritme er en beskrivelse av et antall [operasjoner](#operasjon) som tilsammens utfør en oppgave. Oppgaven kan være en matematisk oppgave som å beregne et gjennomsnitt eller å finne typetallet (største tallet i en tallmengde). Oppgaven kan også være noe værdagslig som å velge den beste oppskriften i en samling med oppskrifter. En algoritme kan være noe konkret som noen linjer med kode som tilsammens utfør oppgaven eller en abstrakt beskrivelse av hvilke operasjoner som skal utføres og i hvilken rekkefølge de skal gjøres.  

Mange internettbedrifter bruker algoritmer når de skal presentere varer eller artikler til deg. For eksempel bruker strømmetjenester som Netflix og Spotify slike når de skal presentere filmer eller musikk de mener passer deg. Disse algoritmene baserer seg på at bedriftene husker hva du har valgt tidligere og hva andre personer som likner deg (samme alder, kjønn, bosted) har valgt.

#### Eksempel: gjennomsnitt
* Lag en list-variabel `alle_tall` hvor du samler alle tall du vill beregne gjennomsnittet på.
* Summer alle tallene i `alle_tall` og lagre resultatet i variabelen `sum`.
* Divider verdien i `sum` med antallet tall i `alle_tall` og lagre verdien i variabelen `gjennomsnitt`

```python
alle_tall = [4, 5, 3, 5, 6, 4, 3, 5]
sum = 0
for tall in alle_tall:
    sum += tall
gjennomsnitt = sum/len(alle_tall)
```

## Operasjon
En enkelt ting en datamaskin skal gjøre.

### Beskrivelse
En operasjon forteller datamaskinen at den skal gjøre noe. Et [program](#program) er mange operasjoner som er satt sammen etter hverandre. Alle operasjoner i et program bruker eller endrer på [verdier](#verdi) og flere operasjoner kan settes sammen til [uttrykk](#uttrykk).

Det finnes fem ulike typer av operasjoner:

1. Bearbeider verdier (*process* eng.)
2. Lagre verdier eller operasjoner 
3. Hente inn verdier (inndata), input
4. Vise verdier (utdata), output
5. Kontrollere et program 

#### Bearbeide verdier
Når du bearbeider en eller flere verdier gjør datamaskinene noe med verdiene. To ulike måter å bearbeide verdier på er å enten bruke en [operator](#operator) for eksempel `5 + 6` eller å sende verdiene som [argumenter](#argument) til en [funksjon](#funksjon) for eksempel `gjennomsnitt([3, 6, 8])`. 

#### Lagre verdi eller operasjon
Verdier lagres i [variabler](#variabel) og operasjoner lagres i [funksjoner](#funksjon). Verdien eller operasjonene blir da lagret i [arbeidsminnet](#arbeidsminne) og kan brukes seinere i programmet. 

Når en verdi skal lagres i en variabel bruker man en [tilordningsoperatorer](#tilordningsoperator) (`=`).

```python
alder = 9
navn = "Marie"
```
Her lagres to ulike verdier: `9, "Marie"`, til variablene: `alder, navn`. 

#### Hente en verdi, input
En datamaskin hadde vært ganske verdiløs hvis den ikke kunne hente verdier enten fra en bruker eller fra et eller annet sted for eksempel en avstandsensor på en bil. 

```python
navn = input("Hva heter du?")
```
Her brukes funksjonen `input` til å spør brukeren om å skrive inn sitt navn. Programmet stopper da opp og venter på at brukeren skal skrive inn sitt navn. 

#### Vise en verdi, output
En verdi kan vises til en bruker for eksempel ved at den vises på skjermen, eller skrives til en fil. 

```python
print("Jeg er 13 år!")
```
Her sendes verdien `"Jeg er 13 år!"` til funksjonen `print` som så viser den på skjermen.    

#### Kontrollere et program
Vanligvis utføres operasjonene i et program fra toppen av tekstfilen og nedover. En operasjon som kontrollerer et [program](#program) kan endre på denne flyten og det finnes ulike måter å kontrollere denne flyten på:

1. if-setninger: Utfører ulike deler av et program avhengig av verdien til en betingelse
2. løkker: Utfører 

## Uttrykk
En eller flere operasjoner som er satt sammen

### Beskrivelse
Et uttrykk består av en eller flere [operasjoner](#operasjon) som er satt sammen. Som oftest resulterer et uttrykk i en verdi.

```python
navn = "Petter"
setning = "Jeg heter " + navn + " og jeg er " + 16 + " år." 
```

Her er to linjer som begge tilordner to variabler to verdier som begge er resultater av to uttrykk. Den første linjen består vare av et uttrykk som resulterer i verdien: `"Petter"`. Den andre linjen består av et uttrykk som resulterer i verdien `"Jeg heter Petter og jeg er 16 år."`.

## Operator
Enkle tegn som bearbeider en eller to verdier

### Beskrivelse
Den enkleste måten å bearbeide en eller to verdier er å bruke en operator. FORTSETT!

## Variabel
Er et navngitt sted i arbeidsminnet som lagrer verdier.

### Beskrivelse
En variabel er et navngitt sted i arbeidsminnet som lagrer en eller flere [verdier](#verdi) i et program. Navnet til variabelen brukes så i [uttrykk](#uttrykk) for å representere verdien til variabelen.

Du bestemmer selv hva navnet til en variabel skal være, men [syntaksen](#syntaks) til programmeringsspråket legger begrensninger på hva et [variabelnavn](#variabelnavn) kan være. Når man lager en variabel for første gangen sier man at man [definerer](#definere) den og man kan ikke bruke en variabel før den er definert. Navnet til en variabel brukes når du:

1. [definerer](#definerer) variablen
2. bruker verdien til variablen
3. endrer verdien til variablen. 

Disse tre måtene kan illustreres med følgende eksempel:
```python
lån = 500000.
rente_prosent = 0.05
rente = lån*rente_prosent
lån = lån + rente
```
Her defineres første tre variabler: `lån`, `rente_prosent` og `rente`. På tredje raden brukes variabelen `lån` og `rente_prosent` i et [uttrykk](#uttrykk) for å regne ut hva renten skal være. På siste raden endres så verdien til variabelen `lån` at renten legges til det første lånet. 

#### Variabel i matematikken
Ordet variabel brukes også i algebra i matematikken. Da betegner det ofte en ukjent tallverdi, f. eks. *x, y*. Innen programmering har en variabel *alltid* en verdi og representerer altså ikke noe ukjent. 

## Variabelnavn
Navnet til en variabel.

### Beskrivelse
En [variabel](#variabel) har altid et navn. [Syntaksen](#syntaks) til et programmeringsspråk legger noen krav til navnet. 

For Python gjelder disse kravene til et variabelnavn 
 
1. kan innholde bokstaver, siffer og understrek. 
2. kan IKKE innholde mellomrom ` `, bindestrek `-` eller punktum `.`: Bruk heller `_` mellom ord i variabelnavnet.
3. kan IKKE starte med en siffer.
4. må være unikt. Flere variabler kan altså ikke ha samme navn. 

### Tips til variabelnavn
Bruk variabelnavn som beskriver hva verdien til variabelen skal brukes til. For eksempel er navn som `a`, `b` oftest dårlige navn, mens `lån`, `navn` eller `poengsum` er bra navn. 

## Funksjonsnavn
Navnet til en funksjon

### Beskrivelse
En funksjon har som oftest et navn. [Syntaksen](#syntaks) til et programmeringsspråk legger noen krav til navnet. Disse krav er de samme som for [variabelnavn](#variabelnavn).

### Tips til funksjonsnavn
Bruk funksjonsnavn som beskriver hva funksjonen skal gjøre. Ettersom en funksjon utfører noe er det altid lurt å bruke et verb som første ord i navnet. For eksempel er `beregn_nytt_lån` eller `hent_resultater` gode navn til to funksjoner.   

### Beskrivelse
En [funksjon](#funksjon) har nesten altid et navn. Funksjonsnavnet brukes når du 

1. [definerer](#definerer) funksjonen
2. [kaller funksjonen](#kalle-funksjon)


## Verdi
En representasjon av en eller flere størrelser

### Beskrivelse
En verdi representerer en størrelse som kan manipuleres av et program. Verdier er ofte det man til daglig kaller data. En datamaskin er altså en maskin som bruker verdier! Verdier har ulike [datatyper](#datatype) som beskriver hva verdien kan brukes til:

Eksempler på datatyper er:
* tall: `2, -5, 0.45, 1e-3`
* tekst: `"A", "Jeg heter Lise."` 
* boolean: `True, False`
* liste: `[5, 3, 8], ["ost", 2, "melk", 5]` 

## Datatype
Beskriver hva en verdi kan brukes til

### Beskrivelse
Alle verdier har en datatype som beskriver hva den kan brukes til. De vanligste datatypene er:
* [tall](#tall): Brukes i all matematikk, se for eksempel [aritmetiske operatorer](#aritmetisk operator).
* tekst eller [strenger](#streng): Brukes til å formidle tekst til en bruker.
* [boolean](#boolean): Brukes til å beskrive om noe er *sant* (`True`) eller *falskt* (`False`).
* [lister](#liste): Brukes å samle verdier i en ordnet rekkefølge.
* [assosiative lister](#assosiativ liste). Brukes til å samle verdier som er assosiert med en [nøkkel](#nøkkel) som er en tekst-streng. 

## Liste
En samling av verdier som er ordnet i en rekkefølge 

### Beskrivelse
En liste (*array* eng.) brukes når du har mange verdier som hører sammen. Verdiene i en liste kalles [elementer](#element) og er ordnet i en rekkefølge. Verdien til hvert element hentes ut fra listen gjennom å bruke nummeret i rekkefølgen elementet har i listen. Dette nummeret kalles for [indeksen](#indeks) til elementet. Du kan lagre listen i en [variabel](#variabel) slik at du kan bruke verdiene seinere i et program. 

```python
# Konkuranse
deltagere = ["Rebecca", "Erik", "Salma", "Amanda"]
deltager = deltagere[2]
deltagere[1] = "Svein"
```
`deltagere` er en list-variabel med fire elementer. Hvert element representerer navnene til deltagerne i en konkuranse. `deltager` er en variabel som har det *tredje* (ikke det andre!) elementet fra listen. Til slutt endres verdien til det andre elementet til `"Svein"`. Deltager `"Erik"` er altså byttet ut med `"Svein"`.

#### Element
Verdiene i en liste kalles for elementer.

#### Indeks
En indeks brukes når man skal hente ut eller endre på elementene i en liste. Indeksen betegner nummeret til verdien i listen. Det første elementet har indeksen `0`, det andre har indeksen `1` og så videre. På rad to over brukes indeksen `2` til å hente ut verdien til det tredje elementet i listen `deltager`. På rad tre over brukes indeksen `1` til å endre det andre elementet i listen til verdien `"Svein"`.

## Definere
Operasjon som lager en variabel eller funksjon.

### Beskrivelse
For å kunne bruke en [variabel](#variabel) eller [funksjon](#funksjon) må de først defineres. Når en variabel defineres knyttes et [variabelnavn](#variabelnavn) til en verdi som lagres i [arbeidsminnet](#arbeidsminne). Når en funksjon defineres knyttes et [funksjonsnavn](#funksjonsnavn) 
Enkelt sagt betyr det å lagre en verdi å si ifra at vi skal ha en variabel eller funksjon med et spesifikt navn. Navnet brukes så i programmet for å representere enten verdien til variabelen eller alle operasjonen til funksjonen.  

I tilegg til å få et navn må en variabel også få en verdi når den defineres. En funksjon må også få et set med operasjoner som skal utføres hver gang man kaller eller kjører funksjonen. I noen [programmeringsspråk](#programmeringsspråk) kan man si ifra at man skal bruke en variabel uten å gi den en verdi. Da heter det å *deklarere* en variabel. 

## Løkke
Operasjoner som repeteres flere ganger.

### Beskrivelse


## Funksjon
Operasjoner som lagres til et navn.

### Beskrivelse
En funksjon brukes til å lagre et sett med operasjoner til et navn. Operasjonene som lagres i en funksjon må utføre en spesifikk oppgave slik at man bruker funksjonens navn istedenfor alle operasjonene når programmet skal utføre oppgaven. Når funksjonen brukes heter det at man [kaller funksjonen](#kalle-funksjon). Når en funksjon blir kallet blir alle operasjonene til funksjonen utført og slik blir også oppgaven til funksjonen utført. 

En funksjon likner på en variabel med at den har et navn og noe blir lagret til navnet, men en funksjon lagrer operasjoner hvor en variabel bare lagrer verdier.

### Eksempel



## Kalle funksjon
Utføre operasjoner knyttet til en funksjon

### Beskrivelse

## Argument
Verdier man sender til en funksjon når man kaller den

## Tilordne
Når man gir eller endrer en verdi til en variabel

