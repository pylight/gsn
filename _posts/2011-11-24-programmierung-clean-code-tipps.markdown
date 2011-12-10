---
layout: post
title: Programmierung - Clean Code Tipps
wordpress_id: 1683
wordpress_url: http://ganz-sicher.net/blog/?p=1683
date: 2011-11-24 16:00:50.000000000 +01:00
---
<img class="lefticon" title="unclean_code" src="/wp-content/uploads/unclean_code.png" alt="" width="48" height="48" />
Da ich letztlich zum Thema "Clean Code" &amp; sauberer Programmierung einen Vortrag gehört habe, werde ich im Folgenden für mich und alle, die das sonst noch interessiert, die wichtigsten Punkte davon zusammenfassen. Ergänzungen oder Anmerkungen sind natürlich erlaubt/-wünscht. Ich habe die Überschriften zum Teil auf englisch belassen, weil man damit einfach einiges kürzer und konkreter ausdrücken kann. Ich hoffe, das stellt für Niemanden ein Problem dar. Falls doch: <a href="http://dict.leo.org/">leo</a> hilft!
<!--more-->

Weshalb ist "Clean Code" wichtig? (Intention)
==============================================
Saubere Programmierung ist vor allem dann wichtig, wenn mehrere Leute eine Software entwickeln oder diese über einen längeren Zeitraum benutzt und eventuell erweitert werden muss. Wer von vornherein Wert auf guten Programmierstil legt, wird später sehr viel effizienter Änderungen vornehmen können und spart sich damit auch eine Menge Zeit und Ärger.
Das Ziel eines Programmierer sollte stets sein, dass andere Menschen den eigenen Code auch verstehen, denn:

> Any fool can write code that a computer can understand. Good programmers write code that humans can understand.” 
>
> [Martin Fowler](http://de.wikipedia.org/wiki/Martin_Fowler)


Generelles (General)
======================
<a href="http://www.xkcd.com/844/"><img class="righticon" src="/wp-content/uploads/good_code.png" alt="" width="325" height="445" /></a>

Trust the code
----------------
> answer = 6 + 36;
...wird der Variable *answer* immer den Wert 42 zuweisen. Es hat also keinen Sinn, danach eine Fallunterscheidung (if...else..) nach dem Wert dieser Variable zu machen. Das war nun ein recht überspitztes Beispiel, dennoch sieht man immer wieder im Code anderer Leute, dass dort Fälle behandelt werden, die tatsächlich nie auftreten können. Das ist schlechter Programmierstil, denn es bläht den Programmcode unnötig auf.
Kritisches Nachdenken ist natürlich erlaubt und richtig. Die Grundfunktionen der bekannten Programmiersprachen sind aber von ausreichend vielen Leuten vor euch getestet worden und sollten daher das tun, was sie versprechen.

Write Bad Code (then clean it)
------------------------------
Eine der wichtigsten Regeln: Niemand kann auf Anhieb guten Code schreiben! Beim Schreiben von Code entsteht während des Denkprozesses zwangsläufig ein unproduktiver bis schlechter Codestil. Wichtig ist, dies zu erkennen und danach den Code zu säubern. Code der regelmäßig benutzt wird, muss auch regelmäßig maintained (gewartet) werden!

Use Version Control Systems
-----------------------------
Wir sind im 21. Jahrhundert, also benutze gefälligst <a href="http://de.wikipedia.org/wiki/Versionsverwaltung">Versionsverwaltungssysteme</a> (auch bekannt unter dem Begriff "VCS")! Damit ersparst du dir einen Haufen Ärger, wenn du alten Code wieder benutzen möchtest. Außerdem erleichtert dies erheblich die Arbeit im Team. Ich empfehle <a href="http://stefanimhoff.de/notiz/einstieg-in-git-als-versionskontrollsystem/">Git</a>, das gerade sehr im Kommen ist, als <em>Codelager</em> im Internet bietet sich dazu <a href="https://github.com/">Github</a> an.

(No) Voodo-Code
---------------
Voodo Code ist Programmcode, der nicht dem eigentlichen Programmziel dient, sondern irgendetwas anderes tut (beispielsweise eine Ausgabe anderer Daten macht). Selbstverständlich sollte so etwas vermieden werden, die zentrale Frage sollte immer sein: "Bringt mich das der Lösung meines Problems näher?".

Bugfixing - Don't write redundant code
---------------------------------------
Häufiges Szenario: Eine Funktion ist fertig geschrieben und macht auch das, was sie soll. Fast perfekt, aber da ist noch dieser eine Fall, in dem das irgendwie so gar nicht richtig funktionieren will...
Schlechter Programmierstil wäre nun, am Ende der Funktion auf diesen Fehler zu prüfen und das Verhalten der Funktion dann zu "überschreiben". Die Funktion tut ja irgendwie doch noch nicht so ganz was sie soll, also muss sie wohl nochmal komplett angepasst werden.


Namenskonventionen (Naming)
===========================
One word per concept - Keep the lexicon consistent
--------------------------------------------------
Vor der Umsetzung sollte man sich (vor allem wenn man nicht alleine Programmiert) auf ein System festlegen, nach dem man seine Namen vergibt (beispielsweise Unterstrich nach jedem Wort in Funktionen, <a href="http://de.wikipedia.org/wiki/Camel_Case">Camel Case</a>). Ich persönlich bevorzuge hier die CamelCase-Schreibweise, das ist aber hauptsächlich eine Geschmacksfrage. Wichtig ist nur, dass man innerhalb seines Projekt konsistent bei der Namensvergabe bleibt. Mehrere Begriffe für eine Sache zu verwenden ist ziemlich böse (z.B. setRating() und getBewertung()).

Reveal intention / Searchable Variables
----------------------------------------
Der Name (eine Funktion, Variable, Klasse,...) sollte immer unmissverständlich ausdrücken, welches Ziel damit verfolgt wird. Namen, die z.B. nur aus einem Buchstaben bestehen sind (mal abgesehen von der Laufvariable i, die in kleineren Schleifen wohl Sinn macht) unleserlich. Vor allem aber sind ungenaue Funktionen schlecht, wenn man nach ihnen im Programmcode suchen will.

Long names aren’t bad
----------------------
Früher - in den guten alten Zeiten - waren lange Funktionsnamen mal ein Problem aufgrund des sehr begrenzten Speichers. Heutzutage muss man auf solche Dinge keine Rücksicht mehr nehmen, aktuelle Programmiersprachen können auch mit längeren Namen umgehen. Wenn es übersichtlicher ist, sollte man sich also nicht scheuen, beispielsweise längere Funktionsnamen zu verwenden. Andere, die den Code später lesen, werden froh sein, wenn sie dann leichter nach diesen Namen suchen können, ohne sich irgendwelche Abkürzungen merken zu müssen.


Funktionen (Functions)
======================
Dry - <span style="text-decoration: underline;">D</span>on't <span style="text-decoration: underline;">r</span>epeat <span style="text-decoration: underline;">y</span>ourself
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Wiederholungen sind böse! Genau um dies zu vermeiden gibt es Funktionen.

Do one thing - and do it well
-----------------------------
Funktionen sollten stets eine Abstraktionsebene umfassen. Oder in verständlich: Eine Funktion sollte genau eine Sache machen - und die sollte sie möglichst gut/effizient machen. Funktionen die mehrere Dinge machen sollten vermieden werden, denn das macht den Code schwerer verständlich und erhöht den <a href="http://commadot.com/wtf-per-minute/">Fluchfaktor</a> im Fehlerfall. Also: Wenn möglich, andere Funktionalität immer auslagern!

Zero arguments – the ideal amount
---------------------------------
Mit Funktionsargumenten ist es ein wenig wie mit Benutzer-Eingabefeldern auf Websites. Werte, die weitgehend frei gewählt werden können, sind immer ein potentielles Sicherheitsrisiko und erhöhen die Fehleranfälligkeit.
Das Ziel sollte sein, möglichst wenige Argumente an Funkionen zu übergeben. Will man nur konkrete Befehle an mehreren Stellen ausführen, müssen auch keine Argumente an die Funktion übergeben werden. Wenige Argumente halten die Komplexität der Funktion gering und erhöhen damit die Lesbarkeit.

Flag arguments are bad / Have no side effects - side effects are lies
---------------------------------------------------------------------
Häufig will man Programmcode auslagern, da man an mehreren Stellen ähnlichen Code benutzt. Der Code ist aber nicht exakt gleich, also übergibt man ein <em>"<a href="http://de.wikipedia.org/wiki/Flag_%28Informatik%29">Flag</a>-Argument"</em>, sodass die Funktion je nach Argument ein wenig anders funktioniert. In einem solchen Fall ist es häufig besser, zwei Funktionen zu erstellen, damit man immer auf den ersten Blick weiß, was die betreffende Funktion <em>genau</em> macht.
Ein noch schlimmerer Fehler sind sogenannte "side effects". Damit sind Aktionen gemeint, die zwar von der Funktion ausgeführt werden, aber nichts mit dem eigentlichen Namen oder Beschreibung der Funktion zu tun haben (z.B. das Schreiben in eine andere Datei). Das kann natürlich fatal sein, wenn man einen Fehler sucht, und ihn an dieser Stelle überhaupt nicht erwartet. Wie schon oben geschrieben: Eine Funktion sollte stets nur <span style="text-decoration: underline;">eine</span> Sache tun.

Extract error handling
-----------------------
Fehlerbehandlung ist ohne Frage wichtig. Allerdings gehört es nicht zum eigentlichen Programmcode/der Funktionalität der Software und oft erhöht es die Lesbarkeit, wenn man dies in eigene Funktionen ausgelagert werden.

Return correct &amp; only once
--------------------------------
Am Ende einer Funktion steht meist ein "return ..". Ein return sollte auch nur in Fehlerfällen und einmal am Ende der Funktion aufgerufen werden, um keine Missverständnisse aufkommen zu lassen.
Vor dem return-Befehl sollten zudem in vielen Fällen noch "Verwaltungsbefehle" ausführt werden, z.B. das Freigeben von vorher reserviertem Speicherplatz. Auch hier hilft es, wenn return nicht unnötig aufgerufen wird, denn sowas vergist man leicht an einer Stelle und erzeugt damit Speicherlecks.

Group similar functionality
---------------------------
Zusammenhängende Funktionen sollten auch optisch nebeneinander im Code angeordnert werden, das verhindert auch unnötiges Scrollen beim Bearbeiten. ;)


Kommentare (Comments)
=====================
Comment to clarify and as less as possible!
---------------------------------------------
Oft wird einem bei Einsteigerkursen zur Programmierung beigebracht, möglichst viel Code zu kommentieren. Kommentare sind aber nicht immer sinnvoll. Ihr Zweck ist es, Dinge zu erklären oder klarzustellen. Der Code selbst sollte so verständlich geschrieben sein, dass nur wenige Kommentare benötigt werden. Umgedreht: Wenn du zu viel kommentieren/klarstellen musst, ist dein Code wohl noch nicht gut genug geschrieben!

Trash Comments
----------------
Oft kommentiert man alten Code aus und lässt ihn stehen, weil man ihn eventuell später noch gebrauchen könnte. Schlechter Programmierstil, denn dafür gibt es Versionsverwaltungssysteme (siehe oben). Auch sollte man unnötige Informationen in Kommentaren weglassen - beispielsweise eine History der Änderungen. (auch das können <a href="http://de.wikipedia.org/wiki/Versionsverwaltung">VCS</a>)

Don't comment bad code - rewrite it!
-------------------------------------
Schlecht: <code>/* This is bad, I know -,- */</code>


Wie fange ich an? / How to begin with good code?
================================================
Am Anfang steht die Idee eines Projekts - wie kann ich das jetzt in (guten) Code umsetzen? Wie fängt man am besten an?

Start with Comments
--------------------
Wenn man mit einem leeren Projekt beginnt, ist es oft schwer, die ersten Zeilen (sinnvollen) Code zu schreiben. Ich gehe meist so vor, dass ich zunächst alle wichtigen Schritte, die ich machen muss in Kommtaren aufschreibe. Damit habe ich schon ein Grundgerüst, dass ich "nur noch" mit Code füllen muss und kann meist effektiver programmieren.

TDD - Test driven development
------------------------------
Eine andere (und etwas ausgefeiltere) Taktik zur effektiven Programmierung nennt sich "Test driven development". Im Groben schreibt man hier zunächst einen Test für eine funktion, der am anfang noch fehlschlägt. Danach programmiert man so lange, bis dieser Test funkioniert und schreibt danach seinen nächsten Test. Der Vorteil ist, das man mit diesem System immer klare Ziele vor Augen hat.

Weiterführendes
===============
<a href="http://www.amazon.de/Clean-Code-Handbook-Software-Craftsmanship/dp/0132350882/ref=sr_1_1?ie=UTF8&amp;qid=1322142781&amp;sr=8-1">
<img class="lefticon" src="/wp-content/uploads/clean-code-cover.jpg" alt="" width="100" height="133" /></a>
Der Vortrag "Clean Code", den ich zu diesem Thema gesehen habe, war von dem Buch <a href="http://www.amazon.de/Clean-Code-Handbook-Software-Craftsmanship/dp/0132350882/ref=sr_1_1?ie=UTF8&amp;qid=1322142781&amp;sr=8-1">Clean Code</a> von Robert C. Martin inspiriert. Ich selbst habe erst die ersten Seiten des Buchs gelesen, wollte es hier aber für Interessierte nicht unerwähnt lassen.

Wie stet's mit euch? Haltet ihr sauberen Code für wichtig? An welche Prinzipen haltet ihr euch beim Programmieren und kennt ihr noch weitere gute Tipps um effektiver Code zu schreiben?
