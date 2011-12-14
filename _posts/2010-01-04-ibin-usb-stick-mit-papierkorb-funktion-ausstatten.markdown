---
layout: post
title: iBin - USB-Stick mit Papierkorb-Funktion ausstatten
wordpress_id: 483
wordpress_url: http://ganz-sicher.net/blog/?p=483
date: 2010-01-04 22:39:22.000000000 +01:00
category: software
---

<img class="lefticon" title="iBin icon" src="{{site.url}}/wp-content/uploads/iBin-icon.png" alt="" width="48" height="48" />
Der Papierkorb kann oft die letzte Rettung sein, wenn Dateien versehentlich gelöscht wurden: Hier werden die nochmal aufgelistet, bevor sie (fast) unwiderruflich gelöscht werden und können bei Bedarf auch jederzeit wiederhergestellt werden. Wer allerdings häufig mit USB-Geräten (z.B. USB-Sticks oder -Festplatten) zu tun hat, hat eventuell schon die unschöne Erfahrung gemacht, dass die dort gelöschten Dateien <em>nicht</em> wie üblich in den Papierkorb wandern, sondern direkt gelöscht werden. Hat man seine Urlaubsfotos erstmal vom USB-Gerät gelöscht, kann man nur noch versuchen, diese mit Wiederherstellungstools wie <a href="http://www.piriform.com/recuva">Recuva</a> zu retten - was leider nicht immer funktioniert....

<!--more-->
Eine bessere Lösung bietet ein kleines Tool namens <a href="http://www.autohotkey.net/~FirstToyLab/project_iBin_download.htm" target="_blank">iBin</a> an: Einmal auf einem USB-Stick installiert, wird statt dem üblichen Dialogfenster beim Löschen eine andere Meldung vorgeschoben:

<img class="borderimg centered" title="ibin löschen abfrage" src="{{site.url}}/wp-content/uploads/ibin-loeschen-abfrage.png" alt="" width="430" height="147" />

Mit "Dump into iBin" landen die zu löschenden Dateien künftig erstmal im neu erzeugten USB-Papierkorb (Klick auf das iBin Trayicon in der Taskleiste):

<img class="borderimg centered" title="ibin gelöschte dateien" src="{{site.url}}/wp-content/uploads/ibin-geloeschte-dateien.png" alt="" width="463" height="310" />

In den iBin-Optionen (Rechtsklick auf das Trayicon -&gt; 'Custom Options') kann außerdem festgelegt werden, dass der iBin-Papierkorb bei bestimmten Aktionen (beim Programm-Start, bei vollem USB-Laufwerk, nach x Tagen,...) automatisch geleert wird.
<em>Achtung</em>: <a href="http://www.autohotkey.net/~FirstToyLab/project_iBin_download.htm" target="_blank">iBin</a> muss jedes Mal erneut gestartet werden, wenn der USB-Stick angeschlpssen wird!

