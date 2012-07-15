---
layout: post
title: Let's play Jeopardy! (Open Source, C++/Qt-basiert)
date: 2012-07-15 00:15
category: linux-distributionen
---
<img src="{{site.url}}/images/blog/icon.png" class="lefticon" alt="" />
Es wird Zeit, dass ich mal ein wenig "Werbung" mache - für ein Spiel, dass ein Freund/Kommilitone von mir geschrieben hat und dass uns schon so einige Abende vor dem Beamer versüßt hat! =) Es handelt sich um eine Spiel-Umsetzung der bekannten ["Jeopardy!" Quiz Show](http://de.wikipedia.org/wiki/Jeopardy!). Die Software ist natürlich Open Source und durch die Benutzung des Qt-Frameworks auch auf Linux, Mac und Windows lauffähig. (Unter Windows sollte es *rein theoretisch* laufen, bisher hat sich noch niemand gefunden, der das auch zweifelsfrei beweisen wollte...)
<!--more-->
Jeopardy - Das Spielprinzip
============================
Für alle die das Spiel/die Show nicht kennen, es ist schnell erklärt: Es gibt ein Spielfeld mit einer Reihe von festgelegten Kategorien (üblicherweise 4-6), zu denen jeweils 5 Fragen vorhanden sind. Diese Fragen sind aufsteigend in der Schwierigkeit & dem damit verbundenen Punkte-/Geldwert, den man bei Beantwortung der Frage erhält. Antworten darf derjenige, der zuerst seinen Buzzer (bzw. seine Taste auf der Tastatur) drückt. Bei einer richtigen Antwort darf derjenige die nächste Frage auswählen (Kategorie und Punktewert), falsche Antworten geben Punkteabzug und es darf wieder Jeder Antworten, bis die Musik abgelaufen ist. Eventuell ist das Spiel auch bekannt von "[Hacker Jeopardy](https://www.google.de/search?hl=de&site=&source=hp&q=hacker+jeopardy)" vom CCC-Kongress oder durch [Watson](http://www.youtube.com/watch?v=WFR3lOm_xhE), den Super-Computer der das Spiel besser beherrscht als seine menschlichen Kontrahenten.
Das Spiel macht natürlich mit mehreren Leuten am meisten Spaß - und im Idealfall lernt man sogar noch etwas beim Spielen. ;]

Download
========
Das Spiel findet ihr (zusammen mit der zugehörigen Dokumentation im Wiki) auf Github:
[https://github.com/chlange/jeopardy](https://github.com/chlange/jeopardy)
Dort kann es als Git-Version oder [Zip-Archiv](https://github.com/chlange/jeopardy/tags) geladen werden. Das Spiel hat mittlerweile einen stabilen Status erreicht und wurde auch auf einer [Konferenz in Paris](http://www.youtube.com/watch?v=y6qF6n3erRY) schon erfolgreich getestet. Falls ihr trotzdem Probleme oder Fragen haben solltet, dürft ihr euch gerne hier im Kommentarbereich oder auf Github melden.

Installation
=============
Wenn ihr das Spiel per git laden wollt, wären die Befehle also:

	apt-get install git                               # optional: git installieren falls nicht vorhanden
	git clone git://github.com/chlange/jeopardy.git   # das Projekt herunterladen
	cd jeopardy                                       # in das Spielverzeichnis wechseln
	
Zum Übersetzen des Quellcodes benötigt ihr g++ und qtcreator, z.B. unter Ubuntu/Linux Mint installierbar per:

	apt-get install qtcreator g++
	
Ihr könnt das Project dann über das Terminal übersetzen mit:

	qmake
	make
	
*(bei Moc-fehlermeldungen eventuell die removeMocErrors.sh ausführen und die beiden letzten Schritte wiederholen)*

Und die grafische Oberfläche starten mit:

	./jeopardy

Alternativ könnt ihr das Projekt auch mit dem grafischen *qtcreator* übersetzen, indem ihr *qtcreator* startet und das Projekt über die Datei jeopardy.pro ladet.


Jeopardy-Runden bauen
======================
Da das Spiel vom Inhalt (d.h. den ausgedachten Fragen und Kategorien) lebt, muss natürlich zunächst eine Person eine Spiel-Runde erstellen. Diese Runden werden in Roundfiles gespeichert, die Schreibweise für diese Dateien ist recht einfach gehalten und wird in einer [Beispieldatei](https://github.com/chlange/jeopardy/blob/master/answers/1.jrf) näher erläutert. Eingebunden werden können Texte, Bilder, Videos und Sounds. Die Person, die die Fragen erstellt, entscheidet üblicherweise auch als GameMaster, ob die Antworten richtig oder falsch waren. Um die Erstellung und Verwaltung der Runden noch einfacher zu machen, habe ich auch ein kleines Webtool erstellt, das unter [https://github.com/pylight/jeopardy-tools](https://github.com/pylight/jeopardy-tools) zu finden ist (Demo: [http://pylight.github.com/jeopardy-tools/](http://pylight.github.com/jeopardy-tools/)). Anregungen für eigene Fragen findet man z.B. bei [Jeopardy Labs](http://jeopardylabs.com/browse/).

Ansonsten kann ich nur viel Vergnügen beim Spielen wünschen. Anregungen zur Verbesserung des Spiels gebe ich selbstverständlich immer gerne weiter!

