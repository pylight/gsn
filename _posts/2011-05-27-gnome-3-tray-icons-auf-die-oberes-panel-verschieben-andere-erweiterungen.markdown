---
layout: post
title: Gnome 3 - Tray Icons auf oberes Panel verschieben + andere Erweiterungen
wordpress_id: 1312
wordpress_url: http://ganz-sicher.net/blog/?p=1312
date: 2011-05-27 09:41:30.000000000 +02:00
category: linux-distributionen
---
Das <a href="http://www.youtube.com/watch?v=lepXx1kDelo">neue Benachrichtigungssystem</a> von Gnome 3 ist schön, allerdings stört mich, dass die Nachrichten sich mit den Programm-Trayicons der Programme in der "Notification Area" rechts unten vermischen. Mitlerweile habe ich eine Möglichkeit gefunden, einzelne Trayicons - wie noch bei Gnome 2 - auf die obere Leiste zu verschieben.

<!--more-->
Trayicons verschieben
=====================
<a href="/wp-content/uploads/Tray-Topbar.jpg"><img class="borderimg centered" title="Tray Topbar" src="/wp-content/uploads/Tray-Topbar.jpg" alt="" width="700" height="405" /></a>

Um die Tray-Icons von einzelnen Programmen auf die obere Leiste zu verschieben, kann man sich eine kleine Gnome Shell-Erweiterung erstellen. Wie schonmal angemerkt, basiert die Oberfläche von Gnome 3 zum Großteil auf Javascript und die Möglichkeiten der Erweiterung sind daher sehr vielfältig. Erstellen kann man neue Erweiterungen sehr einfach mit dem gnome-shell-extension-tool:
	
	gnome-shell-extension-tool --create-extension

Dort kann dann ein beliebiger Name und eine Beschreibung eingegeben, sowie eine eindeutige Extension-ID vergeben werden. Danach öffnet sich direkt ein Editor mit dem eigentlichen Erweiterungscode in der Datei extension.js. (falls nicht, befindet sich die extension.js unter dem Ordner /home//.local/share/gnome-shell/extensions/)

In unserer recht simplen Erweiterung können wir dann diejenigen Programme angeben, deren Tray Icons auf dem Oberen Panel erscheinen sollen:

	const Panel = imports.ui.panel;
	const StatusIconDispatcher = imports.ui.statusIconDispatcher;


	function main() {

		// add the notification(s) you want display on the top bar
		// - one per line. Use the english text string displayed when
		// hovering your mouse over the bottom right notification area

		StatusIconDispatcher.STANDARD_TRAY_ICON_IMPLEMENTATIONS['empathy'] = 'empathy';
		StatusIconDispatcher.STANDARD_TRAY_ICON_IMPLEMENTATIONS['dropbox'] = 'dropbox';
		StatusIconDispatcher.STANDARD_TRAY_ICON_IMPLEMENTATIONS['clementine'] = 'clementine';
		StatusIconDispatcher.STANDARD_TRAY_ICON_IMPLEMENTATIONS['radiotray'] = 'radiotray';
		StatusIconDispatcher.STANDARD_TRAY_ICON_IMPLEMENTATIONS['shutter'] = 'shutter';
		StatusIconDispatcher.STANDARD_TRAY_ICON_IMPLEMENTATIONS['keepassx'] = 'keepassx';
		StatusIconDispatcher.STANDARD_TRAY_ICON_IMPLEMENTATIONS['truecrypt'] = 'truecrypt';
		StatusIconDispatcher.STANDARD_TRAY_ICON_IMPLEMENTATIONS['vlc'] = 'vlc';
	 
	}


Der richtige Programname/die richtige Bezeichnung sieht man vorher beim Draufzeigen auf die TrayIcons in der unteren "Notification Area". Wichtig ist, dass diese Bezeichnung in <em>Kleinbuchstaben</em> in der Erweiterung angegeben wird. Nach Abspeichern der Datei muss die Gnome Shell noch neu gestartet werden. Dies geht z.B. über das Tastenkürzel Alt + F2 und den Befehl 'r'. (ohne Anführungszeichen)

Der Erweiterungs-Tipp stammt übrigens von <a href="http://blog.fpmurphy.com/">http://blog.fpmurphy.com/</a>, eine sehr gute Adressse, wenn man ein bisschen mehr über die Erstellung von Erweiterungen in Gnome 3 wissen möchte!

Bei Problemen mit den Erweiterung hilft häufig die <em>Debugging-Konsole</em> weiter. Diese erreicht man über Alt + F2 und den Befehl 'lg'. Im Errors-Tab werden eventuell aufgetretene Fehler angezeigt, im Extensions-Tab stehen die erfolgreich geladenen Erweiterungen. Zum zwischenzeitlichen Deaktivieren einzelner Erweiterungen, kann <a href="http://live.gnome.org/GnomeTweakTool">gnome-tweaktool</a> benutzt werden.

Weitere Erweiterungen
=====================
Mitlerweile gibt es auch bereits einige andere interessante Erweiterungen für Gnome 3/Gnome Shell. Leider gibt es (noch) keine zentrale/offizielle Website, auf der diese genauer vorgestellt werden.

Ich setze momentan folgende Erweiterungen ein:
<ul>
	<li><a href="http://git.gnome.org/browse/gnome-shell-extensions/commit/?id=064a4c5891b9a4674ece3c60fa5c472beb9d8769">Alternative Status Menu</a> - fügt einen Shutdown-Button in das Systemmenü ein</li>
	<li><a href="https://github.com/ecoleman/noa11y-colemando.com">noally</a> - Entfernt den Accessibility-Eintrag im Panel</li>
	<li><a href="http://www.webupd8.org/2011/05/gnome-shell-weather-extension.html">Weather Extension</a> - fügt ein Wetter-Applet neben der Systemuhr im Panel ein.</li>
	<li><a href="http://www.webupd8.org/2011/05/new-gnome-shell-extensions-that-provide.html">Panel Favorites</a> - zeigt die Dash-Favoriten auch links im Panel an (siehe Screenshot oben)</li>
	<li>Für Laptops bietet sich die Erweiterung <a href="https://github.com/RaphaelKimmig/Gnome-Presentation-Mode">Presentation Mode</a> an. Dort werden im "Presentation Mode" die Energie-Sparfunktionen (z.B. Bildschirmschoner) deaktiviert:</li>
</ul>

<img class="borderimg centered" title="Screenshot-1" src="/wp-content/uploads/Screenshot-1.png" alt="" width="254" height="226" />
