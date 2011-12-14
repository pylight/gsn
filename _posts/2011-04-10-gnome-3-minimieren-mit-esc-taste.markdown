---
layout: post
title: Gnome 3 - Minimieren mit ESC-Taste
wordpress_id: 1193
wordpress_url: http://ganz-sicher.net/blog/?p=1193
date: 2011-04-10 11:47:14.000000000 +02:00
category: tutorials-tipps
---
Aller guten Dinge sind 3, deshalb nochmal ein kurzer Blogeintrag zu Gnome 3. ;) Neben dem Maximieren-Button ist ja auch der Minimieren-Button aus den Fenstern verschwunden. Da ich (wie schon hier geschrieben) tint2 als Tastleiste verwende, kann ich die Minimieren-Funktion durchaus noch gebrauchen. Maximieren geht ja durch Doppelklick auf die Fensterleiste, für's Minimieren bietet sich meiner Meinung nach die ESC-Taste an.
<!--more-->

Zwar kann man Fenster mit der mittleren Taustaste/dem Mausrad in den Hintergrund auf dem Desktop verschieben, Minimieren geht bei Gnome 3 allerdings nur noch umständlich per Rechtsklick. In den Systemeinstellungen kann man unter "Windows/Fenster" zwar einen shortcut für diese Funktion festlegen, die ESC-Taste bricht jedoch die Tastenzuweisung ab und kann deshalb nicht von dort aus der Funktion zugewiesen werden. :/

Lösung
=======
Abhilfe schafft mal wieder der <a href="http://wiki.ubuntuusers.de/Gnome_Konfiguration">gconf-editor</a>. Startet man diesen und navigiert zu /apps/metacity/window_keybindings, so findet man dort einen passenden Eintrag namens "minimize". Setzt man dessen Wert auf "Escape" (ohne Anführungszeichen), kann man künftig alle Fenster auch mit der ESC-Taste minimieren lassen.

<img class="borderimg centered" title="gconf_editor_screen" src="{{site.url}}/wp-content/uploads/gconf_editor_screen.jpg" alt="" width="475" height="340" />

<div class="infobox">Übrigens gibt es zu den Tastenbelegungen hier noch einen kleinen Spickzettel von Gnome:<br />
- <a href="http://live.gnome.org/GnomeShell/CheatSheet">http://live.gnome.org/GnomeShell/CheatSheet</a><br />

Gnome 3 kann man auch auf viele Arten mit dem Tool gsettings (hieß früher gconftool-2) weiter anpassen. Ein sehr Interessanter Artikel dazu findet sich hier:
<a href="http://blog.fpmurphy.com/2011/03/customizing-the-gnome-3-shell.html">http://blog.fpmurphy.com/2011/03/customizing-the-gnome-3-shell.html</a></div>

Delete Shortcut
================
Wie man die Nautilus-Tastenkombination (ohne dafür jetzt extra ein  Script zu basteln) zum Löschen von Dateien (bei Gnome 3 STRG+Del statt Del)  umstellt, habe ich leider noch nicht herausbekommen. Über Tipps dazu  würde ich mich freuen. ;)
