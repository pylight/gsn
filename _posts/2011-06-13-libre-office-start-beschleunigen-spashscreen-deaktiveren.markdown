---
layout: post
title: Libre Office - Start beschleunigen &amp; Spashscreen deaktiveren
wordpress_id: 1376
wordpress_url: https://ganz-sicher.net/blog/?p=1376
date: 2011-06-13 15:57:00.000000000 +02:00
category: kurz-notiert
---
<img class="lefticon" src="{{site.url}}/wp-content/uploads/libre_icon1.png" alt="" width="120" height="24" />

Ich benutze <a href="http://www.libreoffice.org/">LibreOffice</a> (früher OpenOffice) gerne zum Bearbeiten einfacher Texte oder für "Powerpoint" Präsentationen. Unter Archlinux (Gnome 3) habe ich jedoch kürzlich die Erfahrung gemacht, dass der PC nach einiger Zeit komplett einfriert, wenn Libre Office läuft. Nach genauerem Beobachten der Prozessliste stellte sich heraus, dass ein Prozess namens oosplash.bin nahezu 100% meiner Prozessorleistung verbraucht. Es handelt sich dabei wohl im einen Bug, mit dem ich scheinbar <a href="https://bbs.archlinux.org/viewtopic.php?pid=944567">nicht alleine dastehe</a>.

Wie der Prozessname schon erkennen lässt, hängt der Fehler mit dem Spashscreen von LibreOffice zusammen, der beim Start angezeigt wird:
<!--more-->
<img class="borderimg centered" src="https://ganz-sicher.net/blog/wp-content/uploads/LibreOffice_splashscreen.png" alt="" width="250" height="155" />

Da es sich dabei um eine Funktion handelt, die ich sowieso gerne verzichten kann, hab ich diesen einfach deaktiviert. Dazu muss in der Datei <em>/etc/libreoffice/sofficerc</em> die Zeile mit <strong>Logo=1</strong> auf <strong>Logo=0</strong> abgeändert werden:

<img class="borderimg centered" src="https://ganz-sicher.net/blog/wp-content/uploads/Screenshot-Terminal1.png" alt="" width="486" height="295" />

Bei mir führt diese kleine Änderung dazu, dass ich nicht nur deutlich <em>flüssiger</em> mit LibreOffice arbeiten kann, sondern auch der <em>Start des Programms</em> sehr viel zügiger von statten geht. Ein paar weitere Einstellungen um den Start von LibreOffice zu beschleunigen findet man im <a href="http://wiki.ubuntuusers.de/LibreOffice#Start-beschleunigen">Ubuntuusers Wiki</a>:

Unter <span style="font-family: sans-serif; line-height: 21px;"> <em style="padding: 0px; margin: 0px;">"Extras -&gt; Optionen -&gt; LibreOffice.org -&gt; Arbeitsspeicher":</em></span>
<ul>
	<li>den Wert "Verwenden für LibreOffice.org" auf 128 MB zu setzen</li>
	<li>die "Anzahl der Schritte" auf 25 zu reduzieren und</li>
	<li>den Wert von "Speicher pro Objekt" auf 8 MB zu setzen</li>
</ul>
LibreOffice startet damit bei mir annähernd so schnell wie das schlankere <a href="http://www.abisource.com/">AbiWord</a> und das Editieren von Dokumenten macht nochmal deutlich mehr Spaß! ;-)
