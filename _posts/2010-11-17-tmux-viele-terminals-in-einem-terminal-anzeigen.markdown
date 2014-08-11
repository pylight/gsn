---
layout: post
title: Tmux - Viele Terminals in einem Terminal anzeigen
wordpress_id: 858
wordpress_url: http://ganz-sicher.net/blog/?p=858
date: 2010-11-17 23:03:29.000000000 +01:00
category: software
---
<img class="lefticon" src="{{site.url}}/wp-content/uploads/termicon.png" alt="Terminal" />

[Tmux](http://tmux.sourceforge.net) ist für mich ein "Must-Have", wenn ich unter Linux arbeite: Mit diesem Tool kann man im Standard-Terminal auf einfache Weise verschiedene Terminals nebeneinander anordnen oder auch mehrere Terminal-Tabs gleichzeitig laufen lassen. So ist zum Beispiel das Editieren mehrerer Textdateien per SSH sehr viel übersichtlicher.
<!--more-->
Tmux ist schnell zu verstehen und erlernen, wenn man sich erstmal an die Tastenkombinationen gewöhnt hat. Die Standardeinstellungen sind jedoch eher auf amerikanische Tastaturlayouts bezogen, weshalb man sie in der Einstellungsdatei .tmux.conf im Home-Verzeichnis anpassen sollte.

<a title="Tmux Screen (Anklicken für Originalgröße)" href="{{site.url}}/wp-content/uploads/tmux_screen1.png" target="_blank">
<img class="borderimg centered" src="{{site.url}}/wp-content/uploads/tmux_screen1.png" alt="Tmux Screen" width="431" height="202" /></a>

<a title="Tmux Screen (Anklicken für Originalgröße)" href="{{site.url}}/wp-content/uploads/tmux_screen2.png" target="_blank">
<img class="borderimg centered" src="{{site.url}}/wp-content/uploads/tmux_screen2.png" alt="Tmux Screen" width="434" height="204" /></a>

Meine .tmux.conf
================

	# Tastenkombination in STRG-A ändern
	unbind C-b
	set -g prefix C-a

	# Copy mode
	unbind [
	bind Escape copy-mode
	# Use Vi mode
	setw -g mode-keys vi
	# Make mouse useful in copy mode
	setw -g mode-mouse on

	# Bessere Tastenkombinationen fuer's Teilen von Fenstern
	unbind %
	bind | split-window -h
	bind h split-window -h
	unbind '"'
	bind - split-window -v
	bind v split-window -v

	# History auf 1000 setzen
	set -g history-limit 1000

	# Status Bar anpassen
	set -g status-bg black
	set -g status-fg white
	set -g status-interval 1
	set -g status-left '#[fg=green]#H#[default]'
	set -g status-right '#[fg=yellow]#(cut -d " " -f 1-4 /proc/loadavg)#[default] #[fg=cyan,bold]%Y-%m-%d %H:%M:%S#[default]'

	# Falls es Aktivitaeten in anderen Tabs/Fenstern gibt, zeige einen Hinweis auf der Status Bar an
	setw -g monitor-activity on
	set -g visual-activity on

	# Aktuelles Fenster in der Statusbar hervorheben
	setw -g window-status-current-bg red







Wichtige Tastenkombinationen:
=============================
Die Hotkeytaste habe ich bei mir auf STRG-A gesetzt. Für jede Aktion muss man immer STRG-A und danach die gewünschte Taste drücken. Eine Ausnahme bildet das Verändern Größe der Teilterminals. Diese lassen sich mit gedrücktem STRG-A und gleichzeitigem Tippen auf die Pfeiltaste verändern.<strong> </strong>

* ***STRG A -&gt; H*** Fenster horizontal teilen
* ***STRG A -&gt; V*** Fenster vertikal teilen
* ***STRG A -&gt; O*** In nächstes Terminal springen
* ***STRG A -&gt; Pfeiltasten*** In benachbarte Terminals springen
* ***STRG A -&gt; T *** Uhr einblenden
* ***STRG A -&gt; C *** Neues Fenster/Tab erstellen
* ***STRG A -&gt; N*** bzw. ***STRG A -&gt; P*** Nächstes bzw. Vorhergehendes Fenster/Tab anzeigen
* ***STRG A -&gt; .*** Fenstername ändern
* ***STRG A -&gt; F*** Fenstertitel suchen
* ***STRG A -&gt; X*** Aktuelles (Unter)Terminal schließen
* ***STRG A -&gt; Q*** Terminalnummern anzeigen. (dann Nummer drücken, um in ein Terminal zu springen)
* ***STRG A -&gt; W*** Fenster auflisten / auswählen
* ***STRG A Bild hoch/runter*** im aktuellen Terminal scrollen

Viel Spaß mit tmux - bei Fragen helfe ich natürlich gern weiter. Weitere Infos gibt es auf der <a href="http://tmux.sourceforge.net">Homepage</a> bzw. schaut euch mal 'man tmux' an. ;-)
