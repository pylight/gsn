---
layout: post
title: Gimp 2.7 mit Single-Window-Modus
wordpress_id: 1011
wordpress_url: http://ganz-sicher.net/blog/?p=1011
date: 2011-03-08 19:20:12.000000000 +01:00
---
<img style="float: left;" src="http://ganz-sicher.net/blog/wp-content/uploads/gimp.png" alt="" width="32" height="32" />Ich mag das kostenlose Bildbearbeitungsprogramm <a href="http://www.gimp.org/">Gimp</a>. Was ich nicht mag, sind die 3 unabhängigen Fenster, die es mitbringt. Gerade wenn man viele andere Fenster offen hat, verliert man da schonmal leicht den Überblick. Erst jetzt habe ich mitbekommen, dass sich das ab der neuen Version ändern lässt. :)

<!--more-->
<div class="infobox"><strong>Hinweis</strong>: Auf der <a href="http://www.gimp.org/downloads">Gimp-Website</a><span> wird heißt es:
<em>GIMP 2.7.1 is a snapshot of current development towards GIMP 2.8.</em>
Es handelt sich also nicht um eine Stable-Version! </span></div>
<h3>Gimp 2.7 einrichten</h3>
Unter Ubuntu oder Debian lässt sich Gimp 2.7 mit den folgenden Befehlen installieren:

<strong>Neue Paketquelle hinzufügen:</strong>
<code>sudo sh -c "echo 'deb http://ppa.launchpad.net/matthaeus123/mrw-gimp-svn/ubuntu karmic main' &gt;&gt; /etc/apt/sources.list"</code>

<strong>pgp key hinzufügen:</strong>
<pre style="font-family: sans-serif; padding-top: 0px; padding-right: 13px; padding-bottom: 0.1em; padding-left: 0px; text-align: left; font-size: 1em; font-style: normal; font-weight: normal; max-height: 35em; min-height: 2em; overflow-x: auto; overflow-y: auto; width: 651px; border-color: #222222; margin: 0px;"><code>sudo apt-key adv --recv-keys --keyserver keyserver.ubuntu.com 405A15CB</code></pre>
<pre style="font-family: sans-serif; padding-top: 0px; padding-right: 13px; padding-bottom: 0.1em; padding-left: 0px; text-align: left; font-size: 1em; font-style: normal; font-weight: normal; max-height: 35em; min-height: 2em; overflow-x: auto; overflow-y: auto; width: 651px; border-color: #222222; margin: 0px;"><strong><span style="font-family: Georgia, 'Times New Roman', 'Bitstream Charter', Times, serif; line-height: 19px; white-space: normal;">Paketquellen aktualisieren und updaten:</span></strong></pre>
<pre style="font-family: sans-serif; padding-top: 0px; padding-right: 13px; padding-bottom: 0.1em; padding-left: 0px; text-align: left; font-size: 1em; font-style: normal; font-weight: normal; max-height: 35em; min-height: 2em; overflow-x: auto; overflow-y: auto; width: 651px; border-color: #222222; margin: 0px;"><code style="font-family: monospace; font-size: 1em; font-style: normal; font-weight: normal; border-color: #222222;">sudo apt-get update &amp;&amp; sudo apt-get upgrade</code></pre>
Unter dem Menüpunkt Windows (Fenster) -&gt; Single-window-mode kann die neue Funktion dann aktiviert werden. Das Ergebnis:

<center><a href="http://ganz-sicher.net/blog/wp-content/uploads/gimp_single_window.png"><img class="boderimg" src="http://ganz-sicher.net/blog/wp-content/uploads/gimp_single_window.png" alt="" width="595" height="455" /></a></center>
<img style="display: block; margin-left: auto; margin-right: auto;" src="http://ganz-sicher.net/blog/wp-content/uploads/gimp_version_2-7.png" alt="" width="600" height="350" />

&nbsp;

(Leider muss der Modus bei jedem Start neu aktiviert werden. Dieser Bug soll jedoch angeblich in Version 2.8 behoben sein.)
Alternativ könnte übrigens auch <a href="http://code.google.com/p/gimpbox/">Gimpbox</a> (eine Modifikation von Gimp) verwendet werden: <a href="http://www.omgubuntu.co.uk/2010/09/gimpbox-gives-stable-versions-of-the-gimp-single-window-mode/">GimpBox Anleitung bei Omgubuntu</a>.
