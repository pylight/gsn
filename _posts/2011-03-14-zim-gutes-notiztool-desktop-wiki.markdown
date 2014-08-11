---
layout: post
title: Zim - gutes Notiztool / Desktop-Wiki
wordpress_id: 1109
wordpress_url: http://ganz-sicher.net/blog/?p=1109
date: 2011-03-14 23:26:32.000000000 +01:00
category: software
---
<img class="lefticon" title="zim_icon" src="{{site.url}}/wp-content/uploads/zim_icon.png" alt="" width="48" height="48" />

Nachdem mir das Notizprogramm <a href="http://projects.gnome.org/tomboy/">tomboy</a> (evtl. auch als <a href="http://live.gnome.org/Gnote">Gnote</a> bekannt, wenn man kein mono einsetzen möchte) kürzlich alle meine Notizen nach dem Syncronisieren nicht mehr zeigen wollte und ich sie dann unständlich aus den <em>.notes</em>-Dateien raussuchen musste, war ich so begeistert, dass ich mich umbedingt nach mal nach einer Alternative umschauen wollte.
<!--more-->

Gefunden habe ich <a title="Zim Homepage" href="http://zim-wiki.org/">Zim</a>. Zim soll eigentlich ein Desktop-Wiki sein, eignet sich aber für meine Begriffe auch hervorragend für die eigenen Notizen, da man die Wiki-Syntax nicht zwingend verwenden muss. Das Programm ist sehr übersichtlich, man findet sich spontan zurecht. Verfügbar ist es für Linux und Windows, über Umwege wohl auch für Mac (<a href="http://zim-wiki.org/manual/FAQ.html">siehe FAQ</a>). Ich syncronisiere die Notizen mit <a href="http://www.dropbox.com/">Dropbox</a> (beim ersten Start von Zim habe ich als Speicherort einen Ordner innerhalb von Dropbox angegeben) und hatte damit bisher keine Probleme. Zim basiert auf Python und hat deswegen ein <a title="Zim - Hinweise zur Installation" href="http://zim-wiki.org/install.html">paar Abhängigkeiten</a>.

Da es sich ja um ein Desktop-Wiki und nicht primär ein Notiztool handelt, gibt es auch eine gute Exportfunktion, um beispielsweise HTML-Dateien erstellen zu lassen. Alternativ lässt sich das Wiki auch "live" per Webserver zugänglich machen. Eine sehr nützliche Sache, war für mich jedoch nicht so relevant.

Entscheidende Vorteile für mich gegenüber Tomboy:
==================================================
<ul>
	<li>besser lesbare "Notizseiten", die man auch mal schnell mit einem anderen Texteditor wie gedit anpassen kann. tomboy hat dagegen unheimlich viele Formatierungsangaben, es werden pro Notizzettel teilweise sehr viele Dateien angelegt</li>
	<li>bessere Übersichtlichkeit, alles direkt auf einen Blick und klarere Struktur dank der Möglichkeit der Erstellung von Unterseiten</li>
	<li>Einfügen von Bildern, andere Dateien können direkt verlinkt/angehängt werden</li>
	<li>einige weitere Funktionen dank Plugins (z.B. Latex-Unterstützung ;) )</li>
</ul>

<a href="{{site.url}}/wp-content/uploads/zim_screenshot.png"><img class="borderimg centered" title="zim_screenshot" src="{{site.url}}/wp-content/uploads/zim_screenshot.png" alt="" width="460" height="255" /></a>

<a href="{{site.url}}/wp-content/uploads/zim_ordner.png"><img class="borderimg centered" title="zim_ordner" src="{{site.url}}/wp-content/uploads/zim_ordner.png" alt="" width="650" height="270" /></a>


Was noch fehlt
===============
Schön wäre jetzt noch das direkte Einfügen per Drag und Drop (Bilder, Links &amp; Text) aus dem Browser, ähnlich wie das z.B. bei Nevernote (inoffizieller Client für Evernote) möglich ist. Außerdem würde ich mir die Möglichkeit wünschen, das Programm minimiert (wie tomboy) zu starten. Vielleicht kommt sowas ja noch in Zukunft.. :)

<div class="infobox"><span style="text-decoration: underline;"><strong>Zim Homepage/Wiki</strong></span>: <a href="http://zim-wiki.org/" class="homelink">http://zim-wiki.org/</a> (übrigens auch mit <em>Zim</em> geschrieben ;) )</div>

***Update:*** Kleiner Tipp: Zim kann auch minimiert mit Trayicon gestartet werden (ähnlich wie Tomboy) dazu einfach folgenden Befehl benutzen:

> zim --plugin trayicon
