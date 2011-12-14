---
layout: post
title: Perfect Privacy-Tool für den NetworkManager - P^2 VPN Config Tool
wordpress_id: 1447
wordpress_url: http://ganz-sicher.net/blog/?p=1447
date: 2011-08-30 22:30:25.000000000 +02:00
category: programmierung-scripting
---
Nachdem ich mir die sehr <a href="http://www.dgsiegel.net/news/2011_06_16-gnome_screencasts">schönen Gtk3 Tutorial-Videos</a> im <a href="http://www.dgsiegel.net/">Blog von Daniel g. Siegel</a> angesehen habe, habe ich kürzlich mein erstes kleines GUI-Tool mit <a href="http://www.python.org/">Python</a> und <a href="http://www.pygtk.org/">Gtk</a> geschrieben. Da ich regelmäßig den Dienst <a href="http://perfect-privacy.com/">Perfect Privacy</a> nutze, mit dem man ohne Logging surfen kann und zudem viele verschiedene VPN-Server aus unterschiedlichen Ländern zur Verfügung hat, handelt es sich um ein Tool, mit dem man die Perfect-Privacy-Server schneller wechseln kann.
<!--more-->

Weshalb Perfect Privacy?
========================
In Zeiten von unbegründeten Abmahnungen im Internet, speichersüchtigen Werbeanbietern und gehackten Websites samt Datenbank-Leaks, halte ich es für wichtig und richtig, dass jeder Nutzer selbst ein wenig auf seine eigene Sicherheit und Anonymität im Netz achtet. Perfect Privacy ist zwar unter den VPN-Anbietern vergleichsweise teuer, bietet dafür jedoch dafür auch eine große Auswahl an Servern (siehe <a href="https://blog.perfect-privacy.com/server-status/">Server Status Seite</a>), was gerade dann sehr nützlich ist, wenn einzelne Webdienste nur in bestimmten Ländern verfügbar sind (z.B. <a href="http://www.pandora.com/">Pandora</a> in den USA, <a href="http://www.youtube.com/">YouTube</a>-Videos oder <a href="http://www.wilmaa.com/">Wilmaa</a> in der Schweiz). Zudem ist der VPN-Dienst von PP vergleichsweise schnell.
Eine Übersicht solcher Dienste gibt es übrigens z.B. im <a href="http://forum.piratenpartei.de/viewtopic.php?t=992">Forum der Piratenpartei</a>. (wenn dagegen kostenfreie Webproxys ausreichen, findet man bei <a href="http://www.anontux.com/">http://www.anontux.com/</a> eine Übersicht)

P^2 Config Tool - Mein erstes Gtk-Programm
==========================================
Das Ändern der Einstellungen des Gnome <a href="http://live.gnome.org/NetworkManager/SystemSettings">NetworkManagers</a> ist recht umständlich, daher habe ich ein kleines Tool erstellt, mit dem die Server von PP schneller gewechselt werden können und danach eine neue Verbindung zu einem anderen VPN-Server aufgebaut werden kann. Hier 2 Screenshots davon:

<img class="borderimg centered" src="{{site.url}}/wp-content/uploads/1.jpg" alt="" width="486" height="268" />

<img class="borderimg centered" src="{{site.url}}/wp-content/uploads/2.jpg" alt="" width="448" height="1058" />

Eine aktuelle Version sowie weitere Infos zum Tool gibt es auf <a href="https://github.com/pylight/P-2-Config-Tool">GitHub</a>. Über Verwesserungsvorschläge sowie Kommentare dazu (im Blog oder auf GitHub) freue ich mich immer.


Gnome 3 / Gnome Shell Networkmanager: "VPN-Icon-Workaround"
============================================================
Unter Gnome 3 ist der Networkmanager leider noch nicht ganz ausgereift was die VPN-Unterstützung angeht. So wird beispielsweise kein anderes Icon angezeigt, wenn die VPN-Verbindung aktiv ist. Unter Gnome 2 war dies anders, aber mit einem kleinen Trick in Form einer Gnome Shell-Erweiterung kann man die alte Funktionsweise des Networkmanagers wieder erhalten: Durch das löschen des Network-Icons vom Gnome 3 Panel wird der Networkmanager aus dem Fallback-Modus benutzt. Dieser funktioniert wie in früheren Gnome-Versionen:

<img class="borderimg centered" src="{{site.url}}/wp-content/uploads/2.png" alt="" width="269" height="133" />

Hier der Code für die extension.js-Datei:

	const Panel = imports.ui.panel;
	function main() {
		let i = Panel.STANDARD_TRAY_ICON_ORDER.indexOf('network');
		
		if (i == 0) 
		{
			Panel.STANDARD_TRAY_ICON_ORDER.splice(i,1);
		}
		
		delete Panel.STANDARD_TRAY_ICON_
		SHELL_IMPLEMENTATION['network'];
	}

