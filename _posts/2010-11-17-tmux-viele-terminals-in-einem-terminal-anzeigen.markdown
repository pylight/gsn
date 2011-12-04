---
layout: post
title: Tmux - Viele Terminals in einem Terminal anzeigen
wordpress_id: 858
wordpress_url: http://ganz-sicher.net/blog/?p=858
date: 2010-11-17 23:03:29.000000000 +01:00
---
<img style="float: left;" src="http://ganz-sicher.net/blog/wp-content/uploads/termicon.png" alt="Terminal" /><a title="Tmux" href="http://tmux.sourceforge.net/">Tmux</a> ist für mich ein <em>Must-Have</em>, wenn ich unter Linux arbeite: Mit diesem Tool kann man im Standard-Terminal auf einfache Weise verschiedene Terminals nebeneinander anordnen oder auch mehrere Terminal-Tabs gleichzeitig laufen lassen. So ist zum Beispiel das Editieren mehrerer Textdateien per SSH sehr viel übersichtlicher.<!--more-->

Tmux ist schnell zu verstehen und erlernen, wenn man sich erstmal an die Tastenkombinationen gewöhnt hat. Die Standardeinstellungen sind jedoch eher auf amerikanische Tastaturlayouts bezogen, weshalb man sie in der Einstellungsdatei .tmux.conf im Home-Verzeichnis anpassen sollte.

<a class="borderimg" title="Tmux Screen (Anklicken für Originalgröße)" href="http://ganz-sicher.net/blog/wp-content/uploads/tmux_screen1.png" target="_blank"><img src="http://ganz-sicher.net/blog/wp-content/uploads/tmux_screen1.png" alt="Tmux Screen" width="431" height="202" /></a> <a class="borderimg" title="Tmux Screen (Anklicken für Originalgröße)" href="http://ganz-sicher.net/blog/wp-content/uploads/tmux_screen2.png" target="_blank"><img src="http://ganz-sicher.net/blog/wp-content/uploads/tmux_screen2.png" alt="Tmux Screen" width="434" height="204" /></a>

<strong>Hier mal meine .tmux.conf</strong>
<blockquote># Tastenkombination in STRG-A ändern
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
setw -g window-status-current-bg red</blockquote>
<div class="infobox"><strong>Wichtige Tastenkombinationen:
</strong>Die Hotkeytaste habe ich bei mir auf STRG-A gesetzt. Für jede Aktion muss man immer STRG-A und danach die gewünschte Taste drücken. Eine Ausnahme bildet das Verändern Größe der Teilterminals. Diese lassen sich mit gedrücktem STRG-A und gleichzeitigem Tippen auf die Pfeiltaste verändern.<strong> </strong>
<strong>STRG A -&gt; H</strong> Fenster horizontal teilen
<strong>STRG A -&gt; V </strong>Fenster vertikal teilen
<strong>STRG A -&gt; O </strong>In nächstes Terminal springen
<strong>STRG A -&gt; Pfeiltasten </strong>In benachbarte Terminals springen
<strong>STRG A -&gt; T </strong>Uhr einblenden
<strong>STRG A -&gt; C </strong>Neues Fenster/Tab erstellen
<strong>STRG A -&gt; N</strong> bzw. <strong>STRG A -&gt; P</strong> Nächstes bzw. Vorhergehendes Fenster/Tab anzeigen
<strong>STRG A -&gt; .</strong> Fenstername ändern
<strong>STRG A -&gt; F </strong>Fenstertitel suchen
<strong>STRG A -&gt; X </strong>Aktuelles (Unter)Terminal schließen
<strong>STRG A -&gt; Q </strong>Terminalnummern anzeigen. (dann Nummer drücken, um in ein Terminal zu springen)
<strong>STRG A -&gt; W </strong>Fenster auflisten / auswählen
<strong>STRG A Bild[hoch/runter] </strong>im aktuellen Terminal scrollen</div>
Viel Spaß mit tmux - bei Fragen helfe ich natürlich gern weiter. Weitere Infos gibt es auf der <a href="http://tmux.sourceforge.net">Homepage</a> bzw. schaut euch mal 'man tmux' an. ;-)
