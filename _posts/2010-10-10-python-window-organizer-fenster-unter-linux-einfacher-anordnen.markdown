---
layout: post
title: Python Window Organizer - Fenster unter Linux einfacher anordnen
wordpress_id: 747
wordpress_url: https://ganz-sicher.net/blog/?p=747
date: 2010-10-10 12:08:37.000000000 +02:00
category: software
---
Eines der großen Vorteile beim Arbeiten unter Windows 7 war für mich immer, dass man einzelne Fenster schnell und unkompliziert per Tastenkombinationen anordnen kann, um etwas mehr Übersicht auf den Bildschirm zu bringen. Ein Feature, das ich mir auch unter Gnome/Linux immer gewünscht habe, auch wenn ich dort i.d.R. auf mehreren Desktops arbeite und damit dem Problem etwas aus dem Weg gehen konnte.

Genau diese Funktion liefert mir nun PyWO (Python Window Organizer), ein kleines Tool, mit dem man seine Fenster auf mehrere Wege positionieren kann.

<!--more-->
Es funktioniert mit Compiz, Metacity (Gnome), KDE, XFCE, E16, OpenBox und FVWM. Zum ausführen, muss <em>python-xlib </em>installiert sein, unter Ubuntu beispielsweise installierbar mit dem Befehl:
<blockquote><span style="font-family: 'Courier New,courier';">sudo apt-get install python-xlib</span></blockquote>

<div class="infobox">Die aktuelle version von PyWO bekommt ihr <a title="Pywo" class="scriptlink" href="http://code.google.com/p/pywo/downloads/list" target="_blank">hier</a>.</div>

Eine anschaulichere Demonstration der Funktionsweise von PyWO, gibt's im folgenden Video:

<iframe width="560" height="315" src="https://www.youtube.com/embed/VZkbrS0lFkw" frameborder="0" allowfullscreen></iframe>


Zum Schluss noch einige nützliche Tastenkombinationen:
======================================================

* Alt-Ctrl-Shift-Q - PyWO beenden
* Alt-Ctrl-Shift-R - Konfigurationsdatei neu laden
* Alt-Ctrl-Shift-I - Debuginformationen über den windows manager und das aktuelle Fenster ausgeben
* Alt- Numblock_Teilen - Fenster wechseln (Position des Fensters ändern, anderes fenster anklicken um dieses mit aktuellem zu Tauschen)
* Alt- Numblock_1-9 - Fenster im bestimmte Richtung bewegen
* Shift- Numblock_1-9 - Fenster in bestimmte Richtung vergrößern
* Alt-Shift-KP_1-9 - (bei überlappenden Fenstern) -&gt; Fenster verkleinern
* Alt-Ctrl-KP_1-9 - Fenster zu vordefinierter Position bewegen
* Ctrl_KP_1-9 - ausrichten und Größe anpassen (Raster), variable Länge
* Ctrl-Shift_KP_1-9 - ausrichten und Größe anpassen (Raster), variable Höhe

Mehr über die Konfiguration des Tools, erfährt man im <a title="Wiki" href="http://code.google.com/p/pywo/wiki/PywoConfiguration" target="_blank">PyWO wiki</a>.

(<a title="WebUpd8" href="http://www.webupd8.org/2010/10/pywo-python-window-organizer-easily.html" target="_blank">via</a>)
