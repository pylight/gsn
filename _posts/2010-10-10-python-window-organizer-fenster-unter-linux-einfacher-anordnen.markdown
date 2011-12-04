---
layout: post
title: Python Window Organizer - Fenster unter Linux einfacher anordnen
wordpress_id: 747
wordpress_url: http://ganz-sicher.net/blog/?p=747
date: 2010-10-10 12:08:37.000000000 +02:00
---
Eines der großen Vorteile beim Arbeiten unter Windows 7 war für mich immer, dass man einzelne Fenster schnell und unkompliziert per Tastenkombinationen anordnen kann, um etwas mehr Übersicht auf den Bildschirm zu bringen. Ein Feature, das ich mir auch unter Gnome/Linux immer gewünscht habe, auch wenn ich dort i.d.R. auf mehreren Desktops arbeite und damit dem Problem etwas aus dem Weg gehen konnte.

Genau diese Funktion liefert mir nun PyWO (Python Window Organizer), ein kleines Tool, mit dem man seine Fenster auf mehrere Wege positionieren kann.

<!--more-->Es funktioniert mit Compiz, Metacity (Gnome), KDE, XFCE, E16, OpenBox und FVWM. Zum ausführen, muss <em>python-xlib </em>installiert sein, unter Ubuntu beispielsweise installierbar mit dem Befehl:
<blockquote><span style="font-family: 'Courier New,courier';">sudo apt-get install python-xlib</span></blockquote>
Die aktuelle version von PyWO bekommt ihr <a title="Pywo" href="http://code.google.com/p/pywo/downloads/list" target="_blank">hier</a>.

Eine anschaulichere Demonstration der Funktionsweise von PyWO, gibt's im folgenden Video:

<object classid="clsid:d27cdb6e-ae6d-11cf-96b8-444553540000" width="640" height="385" codebase="http://download.macromedia.com/pub/shockwave/cabs/flash/swflash.cab#version=6,0,40,0"><param name="allowFullScreen" value="true" /><param name="allowscriptaccess" value="always" /><param name="src" value="http://www.youtube.com/v/VZkbrS0lFkw?fs=1&amp;hl=en_US" /><param name="allowfullscreen" value="true" /><embed type="application/x-shockwave-flash" width="640" height="385" src="http://www.youtube.com/v/VZkbrS0lFkw?fs=1&amp;hl=en_US" allowscriptaccess="always" allowfullscreen="true"></embed></object>
<div class="infobox">

<em>Zum Schluss noch einige nützliche Tastenkombinationen:</em>

<strong>Alt-Ctrl-Shift-Q</strong> - PyWO beenden
<strong>Alt-Ctrl-Shift-R</strong> - Konfigurationsdatei neu laden
<strong>Alt-Ctrl-Shift-I</strong> - Debuginformationen über den windows manager und das aktuelle Fenster ausgeben

<strong>Alt- Numblock_Teilen</strong> - Fenster wechseln (Position des Fensters ändern, anderes fenster anklicken um dieses mit aktuellem zu Tauschen)
<strong>Alt- Numblock_1-9</strong> - Fenster im bestimmte Richtung bewegen
<strong>Shift- Numblock_1-9</strong> - Fenster in bestimmte Richtung vergrößern
<strong>Alt-Shift-KP_1-9</strong> - (bei überlappenden Fenstern) -&gt; Fenster verkleinern
<strong>Alt-Ctrl-KP_1-9</strong> - Fenster zu vordefinierter Position bewegen
<strong>Ctrl_KP_1-9</strong> - ausrichten und Größe anpassen (Raster), variable Länge
<strong>Ctrl-Shift_KP_1-9</strong> - ausrichten und Größe anpassen (Raster), variable Höhe

</div>
Mehr über die Konfiguration des Tools, erfährt man im <a title="Wiki" href="http://code.google.com/p/pywo/wiki/PywoConfiguration" target="_blank">PyWO wiki</a>.

(<a title="WebUpd8" href="http://www.webupd8.org/2010/10/pywo-python-window-organizer-easily.html" target="_blank">via</a>)
