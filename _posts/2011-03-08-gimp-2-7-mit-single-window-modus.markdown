---
layout: post
title: Gimp 2.7 mit Single-Window-Modus
wordpress_id: 1011
wordpress_url: http://ganz-sicher.net/blog/?p=1011
date: 2011-03-08 19:20:12.000000000 +01:00
category: software
---
<img class="lefticon" src="{{site.baseurl}}/wp-content/uploads/gimp.png" alt="" width="32" height="32" />
Ich mag das kostenlose Bildbearbeitungsprogramm <a href="http://www.gimp.org/">Gimp</a>. Was ich nicht mag, sind die 3 unabhängigen Fenster, die es mitbringt. Gerade wenn man viele andere Fenster offen hat, verliert man da schonmal leicht den Überblick. Erst jetzt habe ich mitbekommen, dass sich das ab der neuen Version ändern lässt. :)

<!--more-->
<div class="infobox"><strong>Hinweis</strong>: Auf der <a href="http://www.gimp.org/downloads">Gimp-Website</a> wird heißt es:
<em>GIMP 2.7.1 is a snapshot of current development towards GIMP 2.8.</em>
Es handelt sich also nicht um eine Stable-Version!</div>

Gimp 2.7 einrichten
====================
Unter Ubuntu oder Debian lässt sich Gimp 2.7 mit den folgenden Befehlen installieren:

Neue Paketquelle hinzufügen:

	sudo sh -c "echo 'deb http://ppa.launchpad.net/matthaeus123/mrw-gimp-svn/ubuntu karmic main' &gt;&gt; /etc/apt/sources.list"

pgp key hinzufügen:

	sudo apt-key adv --recv-keys --keyserver keyserver.ubuntu.com 405A15CB

Paketquellen aktualisieren und updaten:

	sudo apt-get update &amp;&amp; sudo apt-get upgrade
	
Unter dem Menüpunkt Windows (Fenster) -&gt; Single-window-mode kann die neue Funktion dann aktiviert werden. Das Ergebnis:

<img class="borderimg centered" src="{{site.baseurl}}/wp-content/uploads/gimp_single_window.png" alt="" width="595" height="455" />

<img class="borderimg centered" src="{{site.baseurl}}/wp-content/uploads/gimp_version_2-7.png" alt="" width="600" height="350" />

(Leider muss der Modus bei jedem Start neu aktiviert werden. Dieser Bug soll jedoch angeblich in Version 2.8 behoben sein.)
Alternativ könnte übrigens auch <a href="http://code.google.com/p/gimpbox/">Gimpbox</a> (eine Modifikation von Gimp) verwendet werden: <a href="http://www.omgubuntu.co.uk/2010/09/gimpbox-gives-stable-versions-of-the-gimp-single-window-mode/">GimpBox Anleitung bei Omgubuntu</a>.
