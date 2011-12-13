---
layout: post
title: Gnome 3 Fallback Tweaks
wordpress_id: 1395
wordpress_url: http://ganz-sicher.net/blog/?p=1395
date: 2011-06-30 23:40:20.000000000 +02:00
category: linux-distributionen
---
Ich hatte es glaube ich schonmal erwähnt - <a href="http://gnome3.org/">Gnome 3</a> gefällt mir. Wenn man allerdings nicht über einen halbwegs aktuellen Rechner verfügt oder auf die neuen Funktionen von Gnome Shell gut verzichten kann, ist (neben anderen Desktopumgeben wie <a href="http://www.xfce.org/">Xfce</a>) der Gnome 3 Fallback-Mode eine mögliche Option. Der Fallback-Mode ist nicht so schlecht wie sein Ruf! Auf den ersten Blick mag er weniger Funktionen als Gnome 2 bieten, mit einigen versteckten Tricks wird er jedoch zu einer guten Alternative.
<!--more-->

Fallback-Modus aktivieren
=============================
Sofern der Gnome 3 Fallback-Modus nicht aufgrund der Hardware automatisch gewählt wird, kann dieser in den Gnome-Einstellungen erzwungen werden:

<img class="borderimg centered" title="gnome_settings_fallback" src="http://ganz-sicher.net/blog/wp-content/uploads/gnome_settings_fallback.jpeg" alt="" width="330" height="230" />

Der Fallback-Modus wird fortan bei künftigen Logins gestartet, soll wieder Gnome-Shell gestartet werden muss diese Einstellung natürlich wieder rückgängig gemacht werden.


Customizing
============
Andere Themes und Icons
------------------------
Wie bei Gnome Shell ist das Ändern von Themes oder der Icons standardmäßig nicht vorgesehen. Mit dem <a href="https://live.gnome.org/GnomeTweakTool">Gnome-Tweak-Tool</a> können solche Änderungen dennoch durchgeführt werden. Ich verwende im Fallback-Modus das Gtk2-Theme <a href="http://lassekongo83.deviantart.com/art/Zukitwo-203936861">Zukitwo-Dark</a> (<em>entpacken nach ~/.themes</em>) sowie die <a href="http://danrabbit.deviantart.com/art/elementary-Icons-65437279">Elementary-Icons</a> (<em>entpacken nach /usr/share/icons</em>).
Zudem ist das Tweak-Tool für einige andere (eigentlich selbstverständliche) Einstellungsmöglichkeiten (z.B. Icons auf dem Desktop) nützlich.

Panel anpassen und Applets hinzufügen
---------------------------------------
Obwohl im ersten Moment der Eindruck entstehen kann, dass die aus Gnome 2 bekannten Panel-Einstellungen und die Möglichkeit, Elemente zum Panel hinzuzufügen in Gnome 3 Fallback nicht mehr existieren, hat sich lediglich der Shortcut für diese Funktion geändert. Anpassungen können nun nur noch bei gedrückter <strong>Alt-Taste + Rechtsklick</strong> auf das Panel vorgenommen werden, die Konfiguration erinnert sonst aber stark an Gnome 2.
<a href="{{site.baseurl}}/wp-content/uploads/gnome_screen_2.jpeg"><img class="borderimg centered" title="gnome_screen_2" src="{{site.baseurl}}/wp-content/uploads/gnome_screen_2.jpeg" alt="" width="500" height="250" /></a>
<a href="{{site.baseurl}}/wp-content/uploads/gnome_fallback_screen.jpeg"><img class="borderimg centered" title="gnome_fallback_screen" src="{{site.baseurl}}/wp-content/uploads/gnome_fallback_screen.jpeg" alt="" width="500" height="250" /></a>
<center>(﻿das Theme auf den Screenshots ist <a href="http://grvrulz.deviantart.com/art/Hope-gtk3-206207315">Hope/Hope_old</a>)</center>

Die Panelfarbe kann natürlich auch über Themes angepasst werden. Beispiel aus einer gtk.css (befindet sich normalerweise unter ~/.themes/&lt;themename&gt;/gtk-3/):

	@define-color os_chrome_bg_color #ededed;
	@define-color os_chrome_fg_color #000000;
	@define-color os_chrome_selected_bg_color #333;
	@define-color os_chrome_selected_fg_color white;


Startprogramme hinzufügen, Startmenü-Einträge anpassen
-------------------------------------------------------
Um Programme beim Start von Gnome 3 ausführen zu lassen, muss ebenfalls in die Trickkiste gegriffen werden. Genau wie bei Gnome Shell kann aber per Alt-F2 und<strong> gnome-session-properties</strong> das Tool gestartet werden, mit dem die Startprogramme verwaltet werden können. (Für jedes Startprogramm wird dadurch unter ~/.config/autostart eine passende .desktop-Datei angelegt.)
Zum Anpassen des Fallback-Startmenüs steht per default nur ein recht minimalimalistisches. grafisches Tool zur Verfügung (<em>gmenu-simple-editor</em>). Mehr Optionen (abändern der Einträge oder Hinzufügen neuer Einträge) erhält man mit dem aus Gnome 2 bekannten <a href="http://git.gnome.org/browse/alacarte/">alacarte</a>. Auch die Applications-Einträge von Gnome-Shell können damit übrigens verändert werden.


Komfort &amp; Funktionen
=========================

Thumbnail-Bilder bei Videos (Nautilus) aktivieren und "Bevorzugte Programme" festlegen
------------------------------------------------------------------------------------------
Ich bin mir nicht sicher, ob es sich dabei um ein Archlinux-spezifisches Problem handelt oder ob es an Gnome 3 liegt, dass Nautilus bei Videos bei mir keine Thumbnails anzeigt. Die Vorschaubilder lassen sich mit der Anleitung von https://returnfalse.net/log/gnome-3-and-nautilus-video-thumbnails-with-ffmpegthumbnailer/ wieder aktivieren:
<ul>
	<li><a href="http://code.google.com/p/ffmpegthumbnailer/">ffmpegthumbnailer</a> installieren (für Archlinux siehe <a href="http://aur.archlinux.org/packages.php?ID=49555">AUR</a>)</li>
	<li>Im Terminal:</li></ul>
	
	$ rm -rf ~/.thumbnails/
	$ nautilus -q
	
Auch nervt, dass Gnome bei der Installation neuer Programme von Zeit zu Zeit diese als Standardprogramm für bestimmte Dateiendungen wählt. Unter Archlinux verwende ich deswegen <a href="http://aur.archlinux.org/packages.php?ID=23170">gnome-defaults-list</a>, das unter /usr/share/applications die Datei defaults.list anlegt. Über diese Datei können dann die Standardprogramme für alle Dateiendungen eingestellt werden.


Tiling Windows
--------------
Leider Besitzt der Fallback-Modus nicht wie Gnome Shell oder Ubuntu 11.04 die Möglichkeit, Fenster durch einfaches Verschieben an den Rand ("Snap"-Funktion), schnell auszurichten. Ein kleines Tool (mit einigen weiteren Ausrichtungsmöglichkeiten) kann aber hier Abhilfe  verschaffen. <a href="https://github.com/TheWanderer/stiler">Stiller</a> ist ein python-Script, mit dem einige Parameter zur Verfügung stehen, um Fenster bei Window-Managern wie Gnome auszurichten. Natürlich kann man den verschiedenen Einstellungen auch Tastenkombinationen in den Gnome-Einstellungen zuweisen, um das Ausrichten leichter zu machen. Das könnte dann beispielsweise so aussehen:
<a href="{{site.baseurl}}/wp-content/uploads/tiling.jpeg"><img class="borderimg centered" title="tiling" src="{{site.baseurl}}/wp-content/uploads/tiling.jpeg" alt="" width="500" height="300" /></a>
Mir gefällt diese Lösung besser als ein expliziter Tiling Window-Manager, denn so werden die Fenster nur auf Wunsch angeordnet und das sonstige Desktoperlebnis bleibt das selbe. Eine andere Möglichkeit, die Snapping-Windows-Funktion im Fallback-Modus zu bekomen, ist das Nutzen von Compiz, welches auch ein entsprechendes Plugin besitzt.</p>

Compiz
-------
[Compiz](http://www.compiz.org/) kann problemlos unter Gnome 3 installiert werden. Falls als Login Manager GDM zum Einsatz kommt, wird sogar bei einigen Distributionen (Fedora, Archlinux,..) ein zusätzicher "Gnome Classic"-Eintrag hinzugefügt, sodass leicht zwischen Gnome mit Compiz und Gnome mit Gnome Shell gewechselt werden kann. Ich selbst habe Compiz nie langfristig eingesetzt, weil mir die meisten Funktionen zu Effekt-Lastig sind und dafür zu wenig Mehrwert bringen. Mit dem Einstellungsmanager ccsm lässt sich Compiz dennoch sehr vielseitig konfigurieren und ist daher vielleicht eine gute Ergänzung zum eher spartanischen Fallback-Desktop. Weitere Informationen dazu gibt es z.B. im <a href="http://wiki.ubuntuusers.de/compiz">Ubuntuusers-Wiki</a>.



Was fehlt beim Gnome 3 Fallback?
=================================

Besserer TabSwitcher
----------------------
Im Vergleich zum dem neuen TabSwitcher von Gnome-Shell, hat sich im Fallback-Modus leider nichts an der Alt-Tab-Funktion getan. Praktisch wäre auch hier ein TabSwitcher, der die laufenden Programme auf allen Arbeitsflächen/Desktops anzeigt. (Das Tool <a href="http://code.google.com/p/superswitcher/">Superswitcher</a>, was genau dies macht, funktioniert leider bereits seit einer Weile nicht mehr)
Auch hier hilft die Installation von Compiz, sofern man dies einsetzen möchte. (<a href="http://wiki.compiz.org/Plugins/Switcher">Switcher-Plugin</a>)

Fallback-Extensions
--------------------
Die Erweiterbarkeit von Shell durch Extensions ist eine Interessante Sache. Ich selbst hatte bereits über einige davon hier im Blog geschrieben. Wenngleich Applets in das Gnome-Panel eingebunden können, sind Gnome-Fallback-User von solchen Erweiterungen leider komplett ausgeschlossen. Schön wäre, wenn es zumindest einige dieser Funktionen auch in den Fallback-Modus schaffen würden. Allgemein hoffe ich, dass der Fallback-Modus nicht außen vor gelassen sondern aktiv weiterentwickelt wird, denn auch er hat Potential, es fehlen nur auch hier (sichtbare) Einstellungen, Einstellungen und nochmals Einstellungen. ;)

Habt ihr weitere Tipps, die euch den Umgang mit Gnome 3 erleichtern? Ich freue mich über eure Beiträge. ;-)
