[comment]: # (THEME = black)
[comment]: # (CODE_THEME = monokai)
[comment]: # (controls: true)
[comment]: # (keyboard: true)
[comment]: # (markdown: { smartypants: true })
[comment]: # (hash: false)
[comment]: # (respondToHashChanges: false)
[comment]: # (Other settings are documented at https://revealjs.com/config/)


# Text Analytics
Yannick Hutter | FHGR Chur | 

[comment]: # (!!!)


## Natural Language Processing

* Es wird zwischen `geschriebener und gesprochener Sprache` unterschieden.
* Hauptfokus liegt auf der `geschriebenen Sprache`
* `Natural` bezeichnet die durch `menschliche Interaktion gewachsene Sprache`.

[comment]: # (!!!)


### Wichtige Rollen in NLP
* Bedeutung
* Entstehung von Struktur zwischen Wörtern
* Kann durch das Beherschen der Sprache ein künstliches Bewusstsein geschaffen werden?

[comment]: # (!!!)

### Wie lernen Menschen die Sprache
* Durch Nachahmung und Wiederholung (Behavioristischer Ansatz nach Skinner)
* Durch vorgegebene kognitive Fähigkeiten, festlegen von Kategorien, Vereinheitlichung und Übertragung (nach Comsky) 

[comment]: # (!!!)

### Anwendungsfelder
* Übersetzung - Machine Learning
* Spracherkennung - Speech Recognition
* Auskunftssysteme - Chat Bots
* Automatische Textzusammenfassung
* Textgenerierung und Analyse (Cluster, Stimmungsanalyse, Entity Extraction)

[comment]: # (!!!)

### Syntax
* Sprache ist mehr als eine `ungeordnete` Ansammlung von Wörtern
* Gibt die Struktur von Sätzen vor
* Satz
* Satzteil
* Phrase (besteht aus mindestens einem Wort, meist mehrere)
* Wort

[comment]: # (!!!)

### Wörter
* Sind die **kleinste unabhängige Einheit**.
* Besitzen eigenständige Bedeutung
* Bestehen aus Morphemen (ändert die Bedeutung des Wortes, bspw. Plural)
* Morpheme sind `nicht unabhängig`

[comment]: # (!!!)

### Wortarten (Part of Speech - POS)
* Nomen
* Verben
* Adjektive
* Adverb (beschreibt andere Wörter)
* Pronomen
* Präposition (anhand, dank, trotz, ...)

[comment]: # (!!!)

### Phrasen
* Gruppierung eines oder mehrerer Wörter
* Hauptwort ist meist der "Kopf"

[comment]: # (!!!)

### Noun Phrase (NP) 
* Nomen ist Hauptwort
* Beispiele: "NLP", "the brown fox", "the lazy cat"

[comment]: # (!!!)

### Verbal Phrase (VP) 
* Verb ist Hauptwort

[comment]: # (!!!)

### Adjektiv Phrase (ADJP) 
* Adjektiv ist Hauptwort
* Beschreibt oder qualifiziert Nomen
* Beispiel: "Die sehr schnelle Katze" - "sehr schnelle"

[comment]: # (!!!)

### Adverbial Phrase (ADVP) 
* Adverb ist Hauptwort
* Modifiziert Nomen, Verben oder andere Adverben
* Beispiel: "NLP ist sehr interessant" - "sehr interessant" (Beschreibt das Verb genauer)

[comment]: # (!!!)

### Präpositional Phrase (PP) 
* Präposition ist Hauptwort
* Beschreibt andere Wörter oder Phrasen 
* Beispiel: "Eine Frau steht auf einer Leiter" - "auf einer Leiter" (Präposition "auf")

[comment]: # (!!!)

### Grammatiken
* Wird laufend weiterentwickelt
* Dependenzgrammatik 
* Konstituentengrammatik 

[comment]: # (!!!)


### Dependenzgrammatik 
* Beschreibt Abhängigkeit zwischen Wörtern 
* Eins-zu-eins Beziehung, d.h. ein Wort hängt immer von einem anderen Wort ab
* Hauptwort oder Wurzel Wort hat `keine weiteren Abhängigkeiten im Satz`

[comment]: # (!!!)


### Konstituentengrammatik
* Gehen von `Wort-übergreifenden Strukturen aus`
* Wörter bilden den Kopf von Phrasen
* Zusammensetzung anhand `von Phasenstrukturregeln`
* Erlauben Ableitungsregeln zur `Generierung von gültigen Sätzen`
* Wortordnung und Wortreihenfolge kann zur Klassifikation von Sprachen und Sprachfamilien genutzt werden

[comment]: # (!!!)

## Reguläre Ausdrücke
* Werden genutzt um den Text nach bestimmten `Mustern` zu analysieren oder auch zum Suchen und Ersetzen
* `.` steht für **ein einzelnes (beliebiges) Zeichen**
* `^` steht für den **Anfang eines Strings**
* `$` steht für das **Ende eines Strings**
* `*` steht für **beliebig viele (auch keine) Wiederholungen des Musters vor dem Stern
* `?` steht für *keine oder eine Wiederholung** eines Zeichen/Musters

[comment]: # (!!!)

## Reguläre Ausdrücke
* `+` steht für **eins oder mehrere** Wiederholungen eines Zeichen/Musters
* `[]` steht für eine **alternative Auswahl der in den Klammern aufgeführter Zeichen**
* `[^]` **negiert** die Auswahl 
* `\d` steht für **Dezimalziffern 0-9**
* `\D` steht für **nicht Dezimalziffern**
* `\s` steht für **Whitespace**
* `\S` steht für **nicht Whitespace**

[comment]: # (!!!)

## Reguläre Ausdrücke
* `\w` steht für **alphanumerische 0-9 | a-Z | A-Z | _** Zeichen
* `\W` steht für **nicht alphanumerische** Zeichen

[comment]: # (!!!)
