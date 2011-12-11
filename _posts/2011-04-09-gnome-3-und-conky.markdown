---
layout: post
title: Gnome 3 und conky
wordpress_id: 1180
wordpress_url: http://ganz-sicher.net/blog/?p=1180
date: 2011-04-09 11:51:47.000000000 +02:00
category: tutorials-tipps
---
Wie schonmal geschrieben hatte, benutze ich <a href="http://conky.sourceforge.net/">Conky</a> um mein System zu überwachen. Nach dem Wechsel von Gnome 2 zu Gnome 3 war conky leider komplett vom Desktop verschwunden, nach einigen Änderungen verschwand es immer beim Klick auf den Desktop. Nach einigem Googlen und Herumprobieren habe ich es letztendlich doch wieder so hinbekommen, wie ich haben will:
<!--more-->

<img class="borderimg centered" title="conky_screen_gnome3" src="/wp-content/uploads/conky_screen_gnome3.jpg" alt="" width="500" height="300" />

Hier meine neue Config (gehört in die Datei ~/.conkyrc):
---------------------------------------------------------

	alignment tr
	double_buffer yes
	gap_x 10
	gap_y 10
	background yes
	own_window yes
	own_window_transparent yes
	own_window_hints sticky,undecorated,below,skip_taskbar

	use_xft yes
	xftfont Sans:size=9

	TEXT

	${font openlogos:size=20}${font Arial:size=20}${color #0088cc}ARCH ${color Ivory}${font openlogos:size=20}STATS${font }

	${font size=11:italic}${color slate grey}CPU Usage $hr${color }${font }

	CPU1 ${alignr}${cpu cpu1}%
	${cpugraph cpu1 16, 200}
	CPU2 ${alignr}${cpu cpu2}%
	${cpugraph cpu2 16, 200}
	CPU-Temp.${alignr}${hwmon temp 1}Â°C

	${font size=11:italic}${color slate grey}Ram Usage $hr${color }${font }

	RAM ${alignr}$mem/$memmax
	${membar 6, 200}
	Swap ${alignr}$swap/$swapmax
	${swapbar 6, 200}


	${font size=11:italic}${color slate grey}Filesystem $hr${color }${font }

	/ ${alignr}${fs_free /}
	${fs_bar 6, 200 /}
	/home ${alignr}${fs_free /home}
	${fs_bar 6, 200 /home}


	${font size=11:italic}${color slate grey}Top CPU Tasks $hr${color }${font }

	${color #ddaa00}${top name 1}${alignr}${top cpu 1}%${color }
	${top name 2}${alignr}${top cpu 2}%
	${top name 3}${alignr}${top cpu 3}%
	${top name 4}${alignr}${top cpu 4}%
	${top name 5}${alignr}${top cpu 5}%


	${font size=11:italic}${color slate grey}Top RAM Tasks  $hr${color }${font }

	${color #ddaa00}${top_mem name 1}${alignr}${top_mem mem 1}%${color }
	${top_mem name 2}${alignr}${top_mem mem 2}%
	${top_mem name 3}${alignr}${top_mem mem 3}%
	${top_mem name 4}${alignr}${top_mem mem 4}%
	${top_mem name 5}${alignr}${top_mem mem 5}%


	${font size=11:italic}${color slate grey}Infos $hr${color }${font }

	Kernel: ${alignr}$kernel ($machine)
	Uptime: ${alignr}$uptime
	Zeit: ${alignr}${time %H:%M:%S}
	User: ${alignr}$alignc${exec whoami} @ $nodename
	Dateisystem: $alignr${fs_type}


	${font size=11:italic}${color slate grey}Network $hr${color }${font }

	IP (Lan): $alignr${addr eth0}
	IP (extern): $alignr${execi 600 wget http://checkip.dyndns.org/ -q -O - | grep -Eo '\<[[:digit:]]{1,3}(\.[[:digit:]]{1,3}){3}\>'}
	Total Down $alignr${totaldown eth0}
	Total Up   $alignr${totalup eth0}

	Download ${alignr}${downspeed eth0}
	${downspeedgraph eth0}

	Upload ${alignr}${upspeed eth0}
	${upspeedgraph eth0}
	</pre></blockquote>

	<pre><span class="Apple-style-span" style="font-family: Georgia, 'Times New Roman', 'Bitstream Charter', Times, serif; font-size: 13px; line-height: 19px; white-space: normal;">(nochmal nochmal <a href="http://www.ganz-sicher.net/sonstiges/configs/.conkyrc%20%28gnome3%29">hier</a>)</span></pre>
	Wichtig sind vor allem die Befehle am Anfang:
	<blockquote>own_window yes
	own_window_transparent yes
	own_window_hints sticky,undecorated,below,skip_taskbar

**Achtung**: Das "skip_taskbar" führt zu Problemen, wenn die gnome-shell-extension "alternate tab" aktiviert ist! Ich musste diese deaktivieren, da der Alt-Tab Shortcut nicht mehr funktioniert hat.
