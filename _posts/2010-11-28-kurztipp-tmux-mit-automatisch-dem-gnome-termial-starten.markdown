---
layout: post
title: ! '[Kurztipp] Tmux automatisch mit dem (Gnome-)Termial starten'
wordpress_id: 882
wordpress_url: https://ganz-sicher.net/blog/?p=882
date: 2010-11-28 10:13:49.000000000 +01:00
category: tutorials-tipps
---
<img class="lefticon" title="terminal_icon2" src="{{site.url}}/wp-content/uploads/terminal_icon2.png" alt="Terminal Icon" width="48" height="48" />

Vor 3 Artikeln hatte ich über <a href="{{site.baseurl}}/software/tmux-viele-terminals-in-einem-terminal-anzeigen/" target="_self">die Vorteile von Tmux</a> im Linux-Terminal gesprochen. Da ich das Tool als Must-Have bezeichnet habe, wäre es doch ganz sinnvoll, tmux jeweils immer automatisch mit dem Terminal zu starten.

<!--more-->
Der nachfolgende Code sorgt dafür, dass immer eine neue tmux-Session gestartet wird, wenn ihr gnome-terminal öffnet, oder euch in einem Terminal einloggt. Fügt eurer .bashrc (Homeverzeichnis) hinzu:

	if [ -z $TMUX ]; then
	tmux new -d -s all
	if [ 0 -eq $? ]; then
	tmux set -t all status on
	tmux -q new \; linkw -t all \; kill-window -t all:0
	else
	tmux -q new \; linkw -t all
	fi
	fi

Fortan kann man tmux immer direkt mit dem Gnome-Terminal nutzen. :]

Weiterer Hinweis:
=================
Unter Archlinux habe ich in meiner .bash_profile eingestellt, dass mit 

	if [[ -z "$DISPLAY" ]] && [[ 
	$(tty) = /dev/tty1 ]]; then
	  xinit
	  logout
	fi

...immer automatisch der X-Server gestartet wird, wenn ich mich im 1. Terminal einlogge. (ich benutze keinen grafischen Loginmanager um Zeit zu sparen ;) ) Damit der Tipp mit tmux nach wie vor funktioniert und der X-Server richtig startet, muss der Befehl 
> . $HOME/.bashrc
in dieser Datei dahinterstehen!

