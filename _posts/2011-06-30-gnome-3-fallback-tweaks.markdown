---
layout: post
title: Gnome 3 Fallback Tweaks
wordpress_id: 1395
wordpress_url: http://ganz-sicher.net/blog/?p=1395
date: 2011-06-30 23:40:20.000000000 +02:00
---
Ich hatte es glaube ich schonmal erwähnt - <a href="http://gnome3.org/">Gnome 3</a> gefällt mir. Wenn man allerdings nicht über einen halbwegs aktuellen Rechner verfügt oder auf die neuen Funktionen von Gnome Shell gut verzichten kann, ist (neben anderen Desktopumgeben wie <a href="http://www.xfce.org/">Xfce</a>) der Gnome 3 Fallback-Mode eine mögliche Option. Der Fallback-Mode ist nicht so schlecht wie sein Ruf! Auf den ersten Blick mag er weniger Funktionen als Gnome 2 bieten, mit einigen versteckten Tricks wird er jedoch zu einer guten Alternative.
<h3><!--more--></h3>
<h3><span style="text-decoration: underline;">Fallback-Modus aktivieren</span></h3>
Sofern der Gnome 3 Fallback-Modus nicht aufgrund der Hardware automatisch gewählt wird, kann dieser in den Gnome-Einstellungen erzwungen werden:

<a href="http://ganz-sicher.net/blog/wp-content/uploads/gnome_settings_fallback.jpeg"><img class="size-full wp-image-1415 alignnone" title="gnome_settings_fallback" src="http://ganz-sicher.net/blog/wp-content/uploads/gnome_settings_fallback.jpeg" alt="" width="330" height="230" /></a>

Der Fallback-Modus wird fortan bei künftigen Logins gestartet, soll wieder Gnome-Shell gestartet werden muss diese Einstellung natürlich wieder rückgängig gemacht werden.

&nbsp;
<h3><span style="text-decoration: underline;">Customizing</span></h3>
<strong>Andere Themes und Icons</strong>

Wie bei Gnome Shell ist das Ändern von Themes oder der Icons standardmäßig nicht vorgesehen. Mit dem <strong><a href="https://live.gnome.org/GnomeTweakTool">Gnome-Tweak-Tool</a></strong> können solche Änderungen dennoch durchgeführt werden. Ich verwende im Fallback-Modus das Gtk2-Theme <a href="http://lassekongo83.deviantart.com/art/Zukitwo-203936861">Zukitwo-Dark</a> (<em>entpacken nach ~/.themes</em>) sowie die <a href="http://danrabbit.deviantart.com/art/elementary-Icons-65437279">Elementary-Icons</a> (<em>entpacken nach /usr/share/icons</em>).
Zudem ist das Tweak-Tool für einige andere (eigentlich selbstverständliche) Einstellungsmöglichkeiten (z.B. Icons auf dem Desktop) nützlich.

<strong>
Panel anpassen und Applets hinzufügen</strong>

<strong> </strong>Obwohl im ersten Moment der Eindruck entstehen kann, dass die aus Gnome 2 bekannten Panel-Einstellungen und die Möglichkeit, Elemente zum Panel hinzuzufügen in Gnome 3 Fallback nicht mehr existieren, hat sich lediglich der Shortcut für diese Funktion geändert. Anpassungen können nun nur noch bei gedrückter <strong>Alt-Taste + Rechtsklick</strong> auf das Panel vorgenommen werden, die Konfiguration erinnert sonst aber stark an Gnome 2.
<p style="text-align: center;"><span style="font-size: 13px; font-weight: normal;"><a href="http://ganz-sicher.net/blog/wp-content/uploads/gnome_screen_2.jpeg"><img class="aligncenter size-full wp-image-1404" title="gnome_screen_2" src="http://ganz-sicher.net/blog/wp-content/uploads/gnome_screen_2.jpeg" alt="" width="500" height="250" /></a></span></p>
<p style="text-align: center;"><span style="font-size: 13px; font-weight: normal;"><a href="http://ganz-sicher.net/blog/wp-content/uploads/gnome_fallback_screen.jpeg"><img class="size-full wp-image-1401 aligncenter" title="gnome_fallback_screen" src="http://ganz-sicher.net/blog/wp-content/uploads/gnome_fallback_screen.jpeg" alt="" width="500" height="250" /></a></span></p>
(﻿das Theme auf den Screenshots ist <a href="http://grvrulz.deviantart.com/art/Hope-gtk3-206207315">Hope/Hope_old</a>)

Die Panelfarbe kann natürlich auch über Themes angepasst werden. Beispiel aus einer gtk.css (befindet sich normalerweise unter ~/.themes/&lt;themename&gt;/gtk-3/):
<blockquote>@define-color os_chrome_bg_color #ededed;
@define-color os_chrome_fg_color #000000;
@define-color os_chrome_selected_bg_color #333;
@define-color os_chrome_selected_fg_color white;</blockquote>
<strong>
Startprogramme hinzufügen, Startmenü-Einträge anpassen</strong>

Um Programme beim Start von Gnome 3 ausführen zu lassen, muss ebenfalls in die Trickkiste gegriffen werden. Genau wie bei Gnome Shell kann aber per Alt-F2 und<strong> gnome-session-properties</strong> das Tool gestartet werden, mit dem die Startprogramme verwaltet werden können. (Für jedes Startprogramm wird dadurch unter ~/.config/autostart eine passende .desktop-Datei angelegt.)
Zum Anpassen des Fallback-Startmenüs steht per default nur ein recht minimalimalistisches. grafisches Tool zur Verfügung (<em>gmenu-simple-editor</em>). Mehr Optionen (abändern der Einträge oder Hinzufügen neuer Einträge) erhält man mit dem aus Gnome 2 bekannten <strong><a href="http://git.gnome.org/browse/alacarte/">alacarte</a></strong>. Auch die Applications-Einträge von Gnome-Shell können damit übrigens verändert werden.

&nbsp;

<span style="text-decoration: underline;"><span style="font-size: 15px; font-weight: bold;">Komfort &amp; Funktionen</span></span>

<strong>Thumbnail-Bilder bei Videos (Nautilus) aktivieren und <strong>"Bevorzugte Programme" festlegen</strong></strong>

Ich bin mir nicht sicher, ob es sich dabei um ein Archlinux-spezifisches Problem handelt oder ob es an Gnome 3 liegt, dass Nautilus bei Videos bei mir keine Thumbnails anzeigt. Die Vorschaubilder lassen sich mit der Anleitung von https://returnfalse.net/log/gnome-3-and-nautilus-video-thumbnails-with-ffmpegthumbnailer/ wieder aktivieren:
<ul>
	<li><strong><a href="http://code.google.com/p/ffmpegthumbnailer/">ffmpegthumbnailer</a></strong> installieren (für Archlinux siehe <a href="http://aur.archlinux.org/packages.php?ID=49555">AUR</a>)</li>
	<li>Im Terminal:
$ rm -rf ~/.thumbnails/
$ nautilus -q</li>
</ul>
Auch nervt, dass Gnome bei der Installation neuer Programme von Zeit zu Zeit diese als Standardprogramm für bestimmte Dateiendungen wählt. Unter Archlinux verwende ich deswegen <strong><a href="http://aur.archlinux.org/packages.php?ID=23170">gnome-defaults-list</a></strong>, das unter /usr/share/applications die Datei defaults.list anlegt. Über diese Datei können dann die Standardprogramme für alle Dateiendungen eingestellt werden.

<strong>
Tiling Windows</strong>

Leider Besitzt der Fallback-Modus nicht wie Gnome Shell oder Ubuntu 11.04 die Möglichkeit, Fenster durch einfaches Verschieben an den Rand ("Snap"-Funktion), schnell auszurichten. Ein kleines Tool (mit einigen weiteren Ausrichtungsmöglichkeiten) kann aber hier Abhilfe  verschaffen. <strong><a href="https://github.com/TheWanderer/stiler">Stiller</a></strong> ist ein python-Script, mit dem einige Parameter zur Verfügung stehen, um Fenster bei Window-Managern wie Gnome auszurichten. Natürlich kann man den verschiedenen Einstellungen auch Tastenkombinationen in den Gnome-Einstellungen zuweisen, um das Ausrichten leichter zu machen. Das könnte dann beispielsweise so aussehen:
<p style="text-align: center;"><a rel="http://ganz-sicher.net/blog/wp-content/uploads/tiling.jpeg" href="http://ganz-sicher.net/blog/wp-content/uploads/tiling.jpeg"><img class="aligncenter size-full wp-image-1399" title="tiling" src="http://ganz-sicher.net/blog/wp-content/uploads/tiling.jpeg" alt="" width="1000" height="500" /></a></p>
<p style="text-align: left;">Mir gefällt diese Lösung besser als ein expliziter Tiling Window-Manager, denn so werden die Fenster nur auf Wunsch angeordnet und das sonstige Desktoperlebnis bleibt das selbe. Eine andere Möglichkeit, die Snapping-Windows-Funktion im Fallback-Modus zu bekomen, ist das Nutzen von Compiz, welches auch ein entsprechendes Plugin besitzt.</p>
<strong>
Compiz</strong>

<a href="http://www.compiz.org/">Compiz</a> kann problemlos unter Gnome 3 installiert werden. Falls als Login Manager GDM zum Einsatz kommt, wird sogar bei einigen Distributionen (Fedora, Archlinux,..) ein zusätzicher "Gnome Classic"-Eintrag hinzugefügt, sodass leicht zwischen Gnome mit Compiz und Gnome mit Gnome Shell gewechselt werden kann. Ich selbst habe Compiz nie langfristig eingesetzt, weil mir die meisten Funktionen zu Effekt-Lastig sind und dafür zu wenig Mehrwert bringen. Mit dem Einstellungsmanager ccsm lässt sich Compiz dennoch sehr vielseitig konfigurieren und ist daher vielleicht eine gute Ergänzung zum eher spartanischen Fallback-Desktop. Weitere Informationen dazu gibt es z.B. im <a href="http://wiki.ubuntuusers.de/compiz">Ubuntuusers-Wiki</a>.

&nbsp;

<span style="font-size: 15px; font-weight: bold;">Was fehlt beim Gnome 3 Fallback?</span>

<strong>Besserer TabSwitcher</strong>

Im Vergleich zum dem neuen TabSwitcher von Gnome-Shell, hat sich im Fallback-Modus leider nichts an der Alt-Tab-Funktion getan. Praktisch wäre auch hier ein TabSwitcher, der die laufenden Programme auf allen Arbeitsflächen/Desktops anzeigt. (Das Tool <a href="http://code.google.com/p/superswitcher/">Superswitcher</a>, was genau dies macht, funktioniert leider bereits seit einer Weile nicht mehr)
Auch hier hilft die Installation von Compiz, sofern man dies einsetzen möchte. (<a href="http://wiki.compiz.org/Plugins/Switcher">Switcher-Plugin</a>)

<strong><strong>
Fallback-</strong>Extensions </strong>

Die Erweiterbarkeit von Shell durch Extensions ist eine Interessante Sache. Ich selbst hatte bereits über einige davon hier im Blog geschrieben. Wenngleich Applets in das Gnome-Panel eingebunden können, sind Gnome-Fallback-User von solchen Erweiterungen leider komplett ausgeschlossen. Schön wäre, wenn es zumindest einige dieser Funktionen auch in den Fallback-Modus schaffen würden. Allgemein hoffe ich, dass der Fallback-Modus nicht außen vor gelassen sondern aktiv weiterentwickelt wird, denn auch er hat Potential, es fehlen nur auch hier (sichtbare) Einstellungen, Einstellungen und nochmals Einstellungen. ;)

Habt ihr weitere Tipps, die euch den Umgang mit Gnome 3 erleichtern? Ich freue mich über eure Beiträge. ;-)
