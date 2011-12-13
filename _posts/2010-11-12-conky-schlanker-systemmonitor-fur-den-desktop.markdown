---
layout: post
title: Conky - Schlanker Systemmonitor für den Desktop
wordpress_id: 787
wordpress_url: http://ganz-sicher.net/blog/?p=787
date: 2010-11-12 20:21:00.000000000 +01:00
category: linux-distributionen
---
<img class="lefticon" title="System-Monitoring" src="{{site.baseurl}}/wp-content/uploads/monitoring.png" alt="" width="63" height="63" /> 
Applets für den Desktop sind oft nur eine Spielerei und verlangsamen den PC zusätzlich. Anders sieht der Ansatz bei dem Linux-Tool <a title="Conky" href="http://conky.sourceforge.net/">conky</a> aus: <a href="http://conky.sourceforge.net/">Conky</a> ist sehr schlank und - wie bei vielen Programmen unter Linux individuell anpassbar. Dadurch, dass man zum Beispiel die Augaben sämtlicher Befehle auf einfache Weise (nämlich mit dem ${execi}-Befehl) auf dem Desktop anzeigen lassen kann, sind der Fantasie wenig grenzen gesetzt. Dass es folglich viele Beispielkonfigurationen im Netz gibt, brauche ich wohl kaum erwähnen - ein paar Links für Interessierte habe ich im folgenden Abschnitt gesammelt...

<!--more-->

Conky-Hilfe
============
<div class="infobox">
<a class="homelink" href="http://conky.sourceforge.net/">Conky Homepage</a> |
<a class="info" href="http://conky.sourceforge.net/variables.html">Conky Befehlsübersicht / Dokumentation</a> |
<a class="info" href="http://wiki.conky.be/index.php?title=Conky_Wiki">Conky Wiki</a> |
<a class="info" href="http://maketecheasier.com/how-to-create-a-minimal-and-beautiful-desktop-with-conky/2008/10/30">Einige Tipps zum Einstieg</a>
</div>

Gute Anlaufstellen für Beispielkonfigurationen
===============================================
* [http://blog.conky.be/](http://blog.conky.be/)
* [http://ubuntuforums.org/showthread.php?t=281865](http://ubuntuforums.org/showthread.php?t=281865)
* [http://www.junauza.com/2009/09/15-really-awesome-conky-configurations.html](http://www.junauza.com/2009/09/15-really-awesome-conky-configurations.html)
* [http://www.linuxhaxor.net/?p=1677](http://www.linuxhaxor.net/?p=1677)
* [http://www.webupd8.org/2010/11/3-beautiful-conky-configurations.html](http://www.webupd8.org/2010/11/3-beautiful-conky-configurations.html)
* [http://www.gnome-look.org/](http://www.gnome-look.org/)

Meine Conky-Config
==================
Natürlich konnte ich es mir nicht entgehen lassen, selbst ein wenig mit Conky herumexperimentieren ;), deswegen möchte ich auch mein <em>Zwischenergebnis</em> hier nicht verschweigen:
Meine aktuelle Conky-Konfiguration: <a href="{{site.baseurl}}/wp-content/uploads/screen_conky.jpg">Klicke hier für einen Screenshot des gesamten Desktops.</a>
<img class="borderimg centered" src="http://ganz-sicher.net/blog/wp-content/uploads/conky_small.jpg" alt="Conky" />
Meine .conkyrc (gehört in den Ordner /home/<em>DEINUSERNAME</em>):

	background yes
	use_xft yes
	xftfont Sans:size=8
	xftalpha 1
	update_interval 1.0
	total_run_times 0
	own_window yes
	own_window_transparent yes
	#own_window_type desktop
	own_window_hints undecorated,below,sticky,skip_taskbar,skip_pager
	double_buffer yes
	minimum_size 200 200
	maximum_width 200
	draw_shades yes
	draw_outline no
	draw_borders no
	draw_graph_borders yes
	default_color white
	default_shade_color black
	default_outline_color white
	alignment top_right
	gap_x 12
	gap_y 50
	no_buffers yes
	uppercase no
	cpu_avg_samples 2
	override_utf8_locale yes

	TEXT
	${font sans-serif:bold:size=8}SYSTEM ${hr 2}
	${font sans-serif:normal:size=8}$sysname $kernel $alignr $machine
	Host:$alignr$nodename
	Uptime:$alignr$uptime
	File System: $alignr${fs_type}

	${font sans-serif:bold:size=8}PROCESSORS ${hr 2}
	${font sans-serif:normal:size=8}${cpugraph cpu1}
	CPU1: ${cpu cpu1}% ${cpubar cpu1}
	CPU2: ${cpu cpu2}% ${cpubar cpu2}

	${font sans-serif:bold:size=8}MEMORY ${hr 2}
	${font sans-serif:normal:size=8}RAM $alignc $mem / $memmax $alignr $memperc%
	$membar

	${font sans-serif:bold:size=8}DISKS ${hr 2}
	${font sans-serif:normal:size=8}/ $alignc ${fs_used /} / ${fs_size /} $alignr ${fs_used_perc /}%
	${fs_bar /}
	SWAP $alignc ${swap} / ${swapmax} $alignr ${swapperc}%
	${swapbar}


	${font sans-serif:bold:size=8}HEAT ${hr 2}
	${font sans-serif:normal:size=8}HDD ${alignr}${execi 30 hddtemp /dev/sda | cut -c 28-29}°C
	GPU ${alignr}${execi 30 nvidia-settings -t -q GPUCoreTemp}°C

	${font sans-serif:bold:size=8}TOP PROCESSES ${hr 2}
	CPU 
	${font sans-serif:normal:size=8}${top name 1}${alignr}${top cpu 1} %
	${top name 2}${alignr}${top cpu 2} %
	$font${top name 3}${alignr}${top cpu 3} %
	$font${top name 4}${alignr}${top cpu 4} %
	$font${top name 5}${alignr}${top cpu 5} %

	${font sans-serif:bold:size=8}MEMORY
	${font sans-serif:normal:size=8}${top_mem name 1}${alignr}${top mem 1} %
	${top_mem name 2}${alignr}${top mem 2} %
	${top_mem name 3}${alignr}${top mem 3} %
	${top_mem name 4}${alignr}${top mem 4} %
	${top_mem name 5}${alignr}${top mem 5} %

	${font sans-serif:bold:size=8}NETWORK ${hr 2}
	${font sans-serif:normal:size=8}IP address: $alignr ${addr ppp0}
	${downspeedgraph eth0}
	DLS:${downspeed eth0} kb/s $alignr total: ${totaldown eth0}
	${upspeedgraph eth0}
	ULS:${upspeed eth0} kb/s $alignr total: ${totalup eth0}

