---
layout: post
title: ! '[Kurztipp] Tmux automatisch mit dem (Gnome-)Termial starten'
wordpress_id: 882
wordpress_url: http://ganz-sicher.net/blog/?p=882
date: 2010-11-28 10:13:49.000000000 +01:00
---
<a href="http://ganz-sicher.net/blog/wp-content/uploads/terminal_icon2.png"><img class="alignleft size-full wp-image-883" title="terminal_icon2" src="http://ganz-sicher.net/blog/wp-content/uploads/terminal_icon2.png" alt="Terminal Icon" width="48" height="48" /></a>Vor 3 Artikeln hatte ich über <a href="http://ganz-sicher.net/blog/freeware/tmux-viele-terminals-in-einem-terminal-anzeigen/" target="_self">die Vorteile von Tmux</a> im Linux-Terminal gesprochen. Da ich das Tool als <em>Must-Have</em> bezeichnet habe, wäre es doch ganz sinnvoll, tmux jeweils immer automatisch mit dem Terminal zu starten.

<!--more-->Der nachfolgende Code sorgt dafür, dass immer eine neue tmux-Session gestartet wird, wenn ihr gnome-terminal öffnet, oder euch in einem Terminal einloggt. Fügt eurer .bashrc (Homeverzeichnis) hinzu:
<blockquote>if [ -z $TMUX ]; then
tmux new -d -s all
if [ 0 -eq $? ]; then
tmux set -t all status on
tmux -q new \; linkw -t all \; kill-window -t all:0
else
tmux -q new \; linkw -t all
fi
fi</blockquote>

Fortan kann man tmux immer direkt mit dem Gnome-Terminal nutzen. :]

<div class="infobox"><strong>Weiterer Hinweis:</strong> Unter Archlinux habe ich in meiner .bash_profile eingestellt, dass mit 
<blockquote>if [[ -z "$DISPLAY" ]] && [[ 
$(tty) = /dev/tty1 ]]; then
  xinit
  logout
fi</blockquote>...immer automatisch der X-Server gestartet wird, wenn ich mich im 1. Terminal einlogge. (ich benutze keinen grafischen Loginmanager um Zeit zu sparen ;) ) Damit der Tipp mit tmux nach wie vor funktioniert und der X-Server richtig startet, muss der Befehl 
<blockquote>. $HOME/.bashrc</blockquote> in dieser Datei <em>dahinter</em> stehen!</div>
