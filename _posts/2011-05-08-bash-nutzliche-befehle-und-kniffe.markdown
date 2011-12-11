---
layout: post
title: Bash - Nützliche Befehle und Kniffe
wordpress_id: 1249
wordpress_url: http://ganz-sicher.net/blog/?p=1249
date: 2011-05-08 10:41:00.000000000 +02:00
category: linux-distributionen
---
<img class="lefticon" src="/wp-content/uploads/terminal1.png" alt="" width="48" height="48" />
Nach einigen "Klickbunti"-Themen mal wieder ein kleiner Eintrag zur guten alten Shell ;-). Unter Linux kommt man ja fast nicht drum herum, mit dem Terminal und der Bash (Bourne-again shell) in Berührung zu kommen, deswegen ist man gut beraten, sich entsprechend zu wappnen. ;p
Ein paar pfiffige Befehle, für das produktive Arbeiten mit der Bash, habe ich versucht hier zusammenzustellen...
<!--more-->

Einstieg - Grundbefehle lernen
===============================
Wer gerade erst mit Linux anfängt, sollte sich in jedem Fall einmal die Zeit nehmen, die Grundbefehle für die Shell zu lernen. Dazu gibt es viele gute Zusammenfassungen im Netz, z.B.
<ul>
	<li><a href="http://www.tim-bormann.de/sammlung-konsolen-befehle-linux/">http://www.tim-bormann.de/sammlung-konsolen-befehle-linux/</a></li>
	<li><a href="http://www.helmbold.de/linux/">http://www.helmbold.de/linux/</a></li>
	<li><a href="http://www.admintalk.de/konsolenbefehle.php">http://www.admintalk.de/konsolenbefehle.php</a></li>
	<li><a href="http://www.cyberciti.biz/tips/linux-unix-commands-cheat-sheets.html">http://www.cyberciti.biz/tips/linux-unix-commands-cheat-sheets.html</a></li>
</ul>
Auch mit einem Editor sollte man in der Konsole umgehen können, um Konfigurationsdateien anpassen zu können. Für Einsteiger bietet sich hier <strong><em>nano</em></strong> an, das bei den meisten Distributionen auch bereits vorinstalliert ist, für erfahrene Anwender gibt es jedoch noch sehr viel mächtigere Editoren wie z.B. <strong><em>vim</em></strong>. (siehe Tipps unten)
Außerdem ist es sinnvoll, zu wissen wie die Verzeichnisstruktur unter Linux (Suchmaschine des Vertrauens hilft!) aufgebaut ist, um beispielsweise zu wissen, wo wichtige Dateien zu finden sind.

Die richtigen Befehle finden
============================

Als Anfänger tut man sich natürlich schwer, auf Anhieb die richtigen Befehle zu finden. Aber auch wenn man schon mehr Erfahrung hat, passiert es häufiger, dass man auf neue Befehle stößt. Einige Tipps, wie man sich trotzdem zurechtfindet:
<ul>
	<li>Man-Pages nutzen! mit <strong><em>man befehlxy</em></strong> oder <strong><em>info befehlxy</em></strong> erhält man oft viele Informationen zu einem Befehl und den zugehörigen Flags (zusätzliche Argumente, die mit einem Bindestrich angefügt werden, z.B. <strong><em>ls -la</em></strong>)
Mit <em>/suchwort</em> kann man in Man-Pages auch nach geeigneten Schlüsselwörtern suchen.</li>
	<li>oft bekommt man auch mit <em><strong>befehlxy --help</strong></em> oder -h eine Kurzhilfe angezeigt</li>
	<li><strong><em>apropos suchwortxy</em></strong> - Sucht in den Kurzbeschreibungen der Befehle nach dem Suchwort</li>
	<li><em><strong>whatis befehlxy</strong></em> - gibt die Kurzbeschreibung eines Befehls aus</li>
	<li><strong><em>whereis</em></strong> und <em><strong>which</strong></em> - zeigt den (Haupt)Speicherort eines Programms/Befehls an</li>
	<li><em><strong>ldd /pfad/zu/programm</strong></em> - zeigt Bibliotheks-Abhängigkeiten eines Programmes (Beispiel:<em> ldd /usr/bin/gedit</em>)</li>
</ul>

Pipe benutzen
==============
Das Terminal hat zwar keine grafischen Effekte, dafür jedoch andere Vorteile. Diese liegen unter Anderem bei der einfachen Manipulation der Eingabe- und Ausgabekanäle. Natürlich ist es besonders effektiv, wenn man diese Vorteile gezielt einsetzt.
Grob gesagt gibt es 3 Standardkanäle unter Linux für Eingabe &amp; Ausgabe. Eingabe ("STDIN", meist mit der Nummer 0 gekenntzeichnet), Ausgabe ("STDOUT", Nummer 1) und Fehlerausgabe ("STDERR", Nummer 2). Normalerweise gibt der Benutzer etwas über die "Standardeingabe" (einen Befehl) in das Terminal ein und bekommt eine Ausgabe oder einen Fehler zurückgeliefert.
Das alleine wäre nichts besonders, allerdings lässt sich die Ausgabe auch über sogenannte Pipes - gekenntzeichnet durch einen senkrechten Strich | an den Eingabekanal eines anderen Befehls umleiten. So kann man Befehle unter Linux einfach verketten.

<span style="text-decoration: underline;">Drei kleine Beispiele:</span>

	ls | sort				# gibt den Ordnerinhalt aus uns sortiert die Ausgabe alphabetisch
	cat file.txt | grep apfel		# gibt eine Datei aus und sucht dann nach dem Textausschnitt, der den Begriff "apfel" enthält
	history | less				# listet die zuletzt eingegebenen Befehle auf, mit less kann man komfortable in der Ausgabe scrollen oder suchen

Neben der "Pipe" gibt es auch noch andere Möglichkeiten, die Ausgabe umzuleiten. Zum Beispiel kann man mit dem Zeichen &gt; auch Ausgaben in Dateien weiterleiten, wenn diese nicht direkt auf dem Bildschirm erscheinen sollen. So kann man z.B. auch Fehler in einer extra Datei sammeln, indem man die oben genannte Nummer der Fehlerausgabe benutzt:
<blockquote>CMD  2 &gt; errors.txt</blockquote>

*Bang*-Operator: !
==================
Der oben angesprochene <em>history</em>-Befehl zeigt vor jedem früheren Befehl eine Nummer an. Mit einem Ausrufezeichen und einer passenden Nummer kann man den Befehl so auch später erneut aufrufen und erspart sich unnötige Tipparbeit:
<blockquote>$ history | more
10  2011-04-20 10:37:42 sudo pacman -Syu
11  2011-04-20 11:04:06 ls
12  2011-04-20 11:04:18 cd tmp/
13  2011-04-20 11:04:19 ls
14  2011-04-20 09:44:04 cd .config/autostart/
15  2011-04-20 09:44:05 ls
$ !12
cd tmp/</blockquote>
Auch kann man die letzen Eingaben relativ ansprechen, z.B.
<blockquote>!-3      # fuehrt den drittletzten Befehl aus</blockquote>
Speziell für den letzten Befehl gibt es das Kürzel <strong>!!</strong>, was z.B. besonders hilfreich ist, wenn man mal wieder vergessen hat, einen Systembefehl mit Rootrechten zu starten:
<blockquote>$ pacman -Syu
error: you cannot perform this operation unless you are root.
$ sudo !!
sudo pacman -Syu
Password:</blockquote>
<div>Mit dem !-Befehl lassen sich noch andere nützliche Dinge anstellen, z.B.</div>
<blockquote>mkdir newdir
cd !!:1       # erstes Argument vom letzten befehl, wechselt in das neu erstelle Verzeichnis (alternativ "cd !$")</blockquote>
<blockquote>!ssh  :p     # letzten befehl zeigen, der ssh enthielt (ohne :p wird der Befehl direkt ausgeführt)</blockquote>
&nbsp;

Dateiverwaltung
===============
<table>
<tbody>
<tr>
<td>ls -la</td>
<td># gesamten Ordnerinhalt auflisten, sollte den meisten bekannt sein ;)</td>
</tr>
<tr>
<td>cd -</td>
<td># zurück zum vorherigen Verzeichnis, vergleichbar mit dem Zürück-Button in Dateimanagern</td>
</tr>
<tr>
<td>rm -Rf ordner</td>
<td># löscht einen ordner komplett (rekursiv) &amp; ohne nervige Fehler wie bei rmdir</td>
</tr>
<tr>
<td>mkdir -p ~/neue/ordner/anlegen</td>
<td># mit -p können direkt mehrere Unterordner in einem Schritt erstellt werden</td>
</tr>
<tr>
<td>du / -h | more bzw. df -h</td>
<td># zeigt Festplattenspeichernutzung bzw. freien Speicherplatz (-h --&gt; human readable)</td>
</tr>
<tr>
<td>tar cf dir.tar dir/</td>
<td>Tar-Archiv aus Verzeichnis dir erstellen. (tar czf für tar.gz und cjf für tar.bz2)</td>
</tr>
<tr>
<td>tar xvzf file.tar.gz</td>
<td>gzip tar Datei extrahieren (Dateiendung .tgz oder .tar.gz)</td>
</tr>
<tr>
<td>tar xvjf file.tar.bz2</td>
<td>bzip2 tar Datei extrahieren (Dateiendung .tbz oder .tar.bz2)</td>
</tr>
</tbody>
</table>
&nbsp;

Wildcards
==========
Wildcards (erkennbar z.B. an dem Sternchen: *) werden verwendet, wenn bestimmte Buchstaben nicht klar festgelegt werden sollen. Mit ihnen ist es möglich, verschiedene Dateien auf einmal zu behandeln.
Beispiele:
<table>
<tbody>
<tr>
<td>mv *.jpg ./Bilder</td>
<td># alle jpg-Dateien in den Unterordner Bilder kopieren</td>
</tr>
<tr>
<td>find -name *notizen*</td>
<td># sucht nach einer Datei im aktuellen verzeichnis mit dem Begriff notizen im Namen, siehe auch: <a href="http://www.go2linux.org/usages-examples-of-find-command">http://www.go2linux.org/usages-examples-of-find-command</a></td>
</tr>
<tr>
<td>cp filename{,.bak}</td>
<td># Datei filename einfach backupen</td>
</tr>
</tbody>
</table>
Das Zeichen * steht für 0 bis beliebig viele Zeichen. Für nur ein beliebiges Zeichen, sollte ? verwendet werden. Natürlich ist es auch möglich, nur bestimmte Buchstaben zuzulassen.
Siehe dazu z.B. <a href="http://www.tuxfiles.org/linuxhelp/wildcards.html">http://www.tuxfiles.org/linuxhelp/wildcards.html</a>.

Bash-Scripts und Automatisierung
=================================
Ein riesiger Vorteil beim Benutzen der Bash ist die Möglichkeit, mehrere Befehle mit Scripts zu automatisieren. Das verkleinern von vielen Bildern oder ein regelmäßig erstelltes Backup sind so sehr bequem möglich. Natürlich erhöht es auch die Produktivität stark, wenn man solche Scripts an den richtigen Stellen einsetzt. Zudem ist es für Jeden, der schonmal mit dem Terminal gearbeitet hat und bereits einige Befehle kennt, kein großer Schritt mehr, Shell-Scripting zu lernen.
Gute Anlaufstellen sind beispielsweise:
<ul>
	<li><a href="http://selflinux.org/selflinux/html/shellprogrammierung.html">http://selflinux.org/selflinux/html/shellprogrammierung.html</a> - deutsche Einführung in die Shellprogrammierung</li>
	<li><a href="http://tldp.org/LDP/abs/html/index.html">http://tldp.org/LDP/abs/html/index.html</a> - umfangreiche Referenz zum Thema Bash-Scripting (englisch)</li>
</ul>
Neben den Scripts gibt es auch noch andere Möglichkeiten, bei häufig benötigten Aktionen Zeit zu sparen. Befehle in der Datei <strong>.bashrc</strong> im Homeverzeichnis werden beispielsweise immer beim Starten der Shell ausgeführt. Hier bietet es sich an, für längere Befehle alias-Namen festzulegen. Beispiel:
<blockquote>alias la='ls -lahg --color=auto --group-directories-first'</blockquote>
Nun muss statt dem langen Befehl in den Anführungszeichen immer nur la eingegeben werden.
Weitere nette Anregungen für die .bashrc findet man z.B. im <a href="https://bbs.archlinux.org/viewtopic.php?id=50235">Archlinux Forum</a> oder im <a href="http://ubuntuforums.org/showthread.php?t=679762">Ubuntu Forum</a>.


vim - Befehle für den Texteditor
=================================
vim ist ein sehr umfangreicher Texteditor für die Konsole, der durch eine angepasste Konfigurationsdatei sowie etliche Plugins noch erheblich erweitert werden kann. Da bei Linux öfter mal vorkommen kann, dass man Konfigurationsdateien anpassen muss, hier ein kurzer Überblick.
Zum Einstieg ist es wichtig zu wissen, dass es im Wesentlichen 2 Modi gibt: einen Befehls-/Kommandomodus (in dem vim auch startet) zur Eingabe von Befehlen und einen Eingabemodus zur Textbearbeitung. Mit der <strong>Taste i</strong> wird standardmäßig in den Eingabemodus gewechselt, die <strong>Taste ESC </strong>bringt einen zurück in den Befehlsmodus.

<strong>Ein paar nützliche Befehle:</strong>
<table>
<tbody>
<tr>
<td>:q</td>
<td>vim beenden</td>
</tr>
<tr>
<td>:q</td>
<td>Verlassen erzwingen (bei Änderungen ohne Speichern)</td>
</tr>
<tr>
<td>:w</td>
<td>Änderungen in Datei schreiben</td>
</tr>
<tr>
<td>:wq oder :x</td>
<td>Speichern und Verlassen kombinieren</td>
</tr>
<tr>
<td>/suche</td>
<td>nach dem string "suche" im dokument suchen</td>
</tr>
<tr>
<td>:/s/foo/bar</td>
<td>nach foo suchen und mit bar ersetzen (erstes Ergebnis)</td>
</tr>
<tr>
<td>:%s/foo/bar</td>
<td>im Dokument nach foo suchen und mit bar ersetzen (alle Ergebnisse)</td>
</tr>
<tr>
<td>n</td>
<td>Weitersuchen (nächstes Ergebnis)</td>
</tr>
<tr>
<td>u</td>
<td>vorige Schritte rückgängig machen</td>
</tr>
<tr>
<td>b oder w</td>
<td>ein Wort vor oder weiter springen</td>
</tr>
<tr>
<td>D</td>
<td>vom Cursor bis zum Ende der Zeile alles ausschneiden</td>
</tr>
<tr>
<td>p</td>
<td>Text aus Zwischenablage einfügen</td>
</tr>
<tr>
<td>v</td>
<td>Text markieren (erneutes v beendet Markieren)</td>
</tr>
<tr>
<td>y</td>
<td>Text kopieren</td>
</tr>
<tr>
<td>dd</td>
<td>aktuelle Zeile löschen</td>
</tr>
<tr>
<td>G</td>
<td>zum Ende des Dokumentes springen</td>
</tr>
<tr>
<td>gg</td>
<td>ganz zum Anfang eines Dokuments springen</td>
</tr>
</tbody>
</table>
&nbsp;

Speicherprobleme lösen
======================

<em>Für die aktuelle Datei fehlen die nötigen Schreibrechte:</em>
<blockquote>:shell     # wechseln in die Shell, ohne vim zu beenden
chmod u+w filename.txt     # gibt dem aktuellen benutzer schreibrechte
exit     # kehrt zu vim zurück
:w!     # Dateiänderungen speichern</blockquote>
<em>Für die Aktuelle Datei fehlen die Rootrechte (Konfigurationsdateien usw.):</em>
<blockquote>:w !sudo tee %</blockquote>
(tee schreibt standardausgabe in eine datei, in diesem Fall die aktuelle (%), alternativ kann nach dem tee befehl natürlich auch ein anderer Befehl angegeben werden)

<em>Weiterführendes zu vim:</em>
<ul>
	<li><a href="http://marketplace.tutsplus.com/item/venturing-into-vim-4part-video-series/131400">http://marketplace.tutsplus.com/item/venturing-into-vim-4part-video-series/131400</a></li>
	<li><a href="http://net.tutsplus.com/sessions/vim-essential-plugins/">http://net.tutsplus.com/sessions/vim-essential-plugins/</a> - Vorstellung einiger Plugins</li>
	<li><a href="http://net.tutsplus.com/articles/web-roundups/25-vim-tutorials-screencasts-and-resources/">http://net.tutsplus.com/articles/web-roundups/25-vim-tutorials-screencasts-and-resources/</a><a href="http://www-user.tu-chemnitz.de/~hot/VIM/VIM/vikurz.html"><span style="color: #000000;">
</span>http://www-user.tu-chemnitz.de/~hot/VIM/VIM/vikurz.html</a></li>
	<li><a href="http://www.oualline.com/vim-cook.html">http://www.oualline.com/vim-cook.html</a></li>
	<li>Suchmaschine des Vertrauens ;)</li>
</ul>


Nützliche Tastenkombinationen (u.A. Gnome-Terminal)
========================================================
<ul>
	<li><span style="font-size: 14px; font-weight: normal;"><strong>Strg + A</strong> oder <strong>Strg + E</strong> - an das Anfang oder Ende einer Eingabe springen</span></li>
	<li><span style="font-size: 14px; font-weight: normal;"><strong>Strg + Shift + T</strong> - neuen Tab mit  eigenem Terminal anlegen</span></li>
	<li><span style="font-size: 14px; font-weight: normal;"><strong>Strg + R &lt;suchwort&gt;</strong> - History/letzte Eingaben nach einem Befehl durchsuchen</span></li>
	<li><span style="font-size: 14px; font-weight: normal;"><strong>Tab</strong> - versucht einen Befehl zu vervollständigen - hier empfhiehlt es sich auch, bash-completion installiert zu haben, was dieses Feature noch erweitert</span></li>
	<li><span style="font-size: 14px; font-weight: normal;"><strong>Strg + D</strong> - Eingabe von aktuellem Befehl beenden ("End-of-File", schließt die Standardeingabe - und damit häufig auch das Programm)</span></li>
	<li><span style="font-size: 14px; font-weight: normal;"><strong>Strg + C</strong> - Laufendes Kommando abbrechen (sendet das Signal "SIGINTR" am das Programm)</span></li>
	<li><span style="font-size: 14px; font-weight: normal;"><strong>F11</strong> - Vollbild</span></li>
	<li><span style="font-size: 14px;"><strong>Strg + Z</strong><span style="font-weight: normal;"> - gerade im Terminal aktiven Prozess schlafen legen (es wird eine Nummer angezeigt (z.B. [1]) über die der Prozess wieder im aktuellen Terminal: </span><strong style="font-weight: normal;">fg %1</strong><span style="font-weight: normal;"> oder im Hintergrund: </span><strong style="font-weight: normal;">bg %1</strong><span style="font-weight: normal;"> fortgesetzt werden kann)</span></span></li>
	<li><span style="font-size: 14px; font-weight: normal;"><strong>CMD &amp;</strong> - oeffnet einen Befehl nicht im Terminal sondern im Hintergrund, sodass man im Terminal weiterarbeiten kann. Bei Erfolg wird die ProcessID des neuen Prozesses angezeigt.</span></li>
	<li><span style="font-size: 14px; font-weight: normal;"><strong>Strg+U</strong> / <strong>Strg +W</strong> - gesamten Text nach/vor dem Curor löschen
</span></li>
	<li><span style="font-size: 14px; font-weight: normal;"><strong>Alt + F / Alt + B</strong> - ein Wort in der Eingabe vor / zurueck springen
</span></li>
</ul>


Fehlerbehandlung
================
Viele Fehler, die einem bei der Shell-Benutzung über den Weg laufen, sind die Ursache ähnlicher Fehlerquellen und deswegen oft einfach lösbar. Generell empfiehlt es sich (sofern im Terminal keine Fehlermeldung aufgetaucht ist), einmal in den Logfiles (i.d.R. zu finden im Verzeichnis /log), z.B. in Kombination mit dem <em>grep</em>-Befehl nachzusehen. Für ehemalige Windows-Nutzer ist wahrscheinlich das Rechtesystem erst einmal ungewohnt:

Rechteverwaltung
=================
<blockquote>chmod u+rwx file   # dem benutzer Lese (r) Schreib (w) und Ausführungsrechte (x) für die Datei file geben</blockquote>
<blockquote>chown und chgrp # Besitzer und Gruppe einer Datei festlegen</blockquote>
<blockquote>su user  # als benutzer user anmelden. su ohne Parameter gibt dauerhafte Rootrechte</blockquote>

Programme "killen"
==================
Programme kann man auf verschiedene Weise zum Beenden zwingen:
<blockquote>pkill -f programm     # versucht "programm" zu beenden</blockquote>
Falls mehrere Instanzen eines Programmes laufen, lassen sich auch alle aufeinmal beenden mit:
<blockquote>killall programm</blockquote>
Erweiterte Kontrolle über das gewünschte Signal, das zum Beenden gesendet wird bekomt man mit dem kill-Befehl. (siehe man kill) Hier muss allerdings auch erst z.B. mittels  ps -ax | grep programm nach der richtigen Processid gesucht werden, Beispiel:
<blockquote>kill -9 ID</blockquote>

Andere (System)tools und Weitere Quellen
==========================================
Um den Artikel möglichst allgemeingültig zu halten, habe ich mich bemüht, hier nur die "Standardbefehle" zu erwähnen. Natütlich gibt es noch etliche gute Bash-Tools, die die Produktivität nochmal verbessern. Statt der normalen Systemüberwachung <em>top</em> benutze ich z.B. <strong>htop</strong>, welches mehr Funktionen bietet. Für Systemtools gibt es bereits einen guten Blogartikel, welchen ich hier gerne verlinke: <a href="http://www.cyberciti.biz/tips/top-linux-monitoring-tools.html">http://www.cyberciti.biz/tips/top-linux-monitoring-tools.html</a>.

Weitere Querverweise
====================
<ul>
	<li><a href="http://www.commandlinefu.com/">http://www.commandlinefu.com/</a> - Website, auf der interessante Bashbefehle gesammelt werden</li>
	<li><a href="http://presentations.codeinthehole.com/confoo2011/">http://presentations.codeinthehole.com/confoo2011/</a> - 60 Folien lange &amp; interessante Präsentation zum Thema "commandlineflue for web developers"</li>
	<li><a href="http://linux.101hacks.com/">http://linux.101hacks.com/</a> - Anwendungsbespiele bekannter Befehle</li>
</ul>
Ich hoffe die Tipps in diesem Artikel kann dem Einen oder Anderen die Arbeit in der Bash erleichtern. ;) Wie immer freue ich mich über Kommentare:
Gibt es noch Befehle oder Tricks, die ihr weiterempfehlen könnt oder für erwähnenswert haltet?

<a href="http://www.helmbold.de/linux/"></a>
