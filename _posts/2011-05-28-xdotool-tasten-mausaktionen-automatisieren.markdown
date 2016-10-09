---
layout: post
title: xdotool - Tasten- & Mausaktionen automatisieren
wordpress_id: 1339
wordpress_url: https://ganz-sicher.net/blog/?p=1339
date: 2011-05-28 01:06:37.000000000 +02:00
category: software
---
Mit Terminaltool <a href="http://www.semicomplete.com/projects/xdotool/">xdotool</a> lassen sich von der Konsole aus graphische (X-)Anwendungen bei Linux-Distributionen ändern. So können damit beispielsweise bestimmte Tastenkombinationen mehrfach per Script automatisiert werden, oder z.B. auch Fenster gesucht und deren Titel angepasst werden. Da das Tool ja selbst keine graphische Oberfläche benötigt, sind die Anwendungsfälle sehr vielfältig. Beispielsweise könnte man damit auch ein Script von einem anderen Rechner aus über ssh ansteuern und auf dem entfernten Rechner bestimmte Aufgaben ausführen lassen.

Ich habe mir damit unter Gnome 3 (da hier Nautilus nicht die Desktopverwaltung übernimmt) mal ein kleines Script geschrieben, mit welchem man beim <strong>Dateimanager Nautilus neue Ordner in Tabs</strong> im aktuellen Fenster öffnen kann. Eine solche Funktionalität hat mir bisher gefehlt und gefühlt tausend offene Nautilus-Fenster sind nicht wirklich schön. ;)
<!--more-->


Bash-Script "Opentab.sh"
=========================
Wie bereits beschrieben benutze ich mein Bashscript unter Gnome 3, wo Nautilus nicht für die Darstellung der Desktopicons verwendet wird. Sollte dies der Fall sein, wird das Script eventuell nicht (richtig) funktionieren, da xdotool dann eine falsche Nautilus-Instanz findet. Für Verbesserungsvorschläge und Kritik bin ich natürlich wie immer offen! Mein <a href="http://www.ganz-sicher.net/scripts/myscripts/Opentab.sh">Bashscript</a>:

	#!/bin/bash	
					
	# Opentab.sh by Sven (admin@ganz-sicher.net)        
	# Opens nautilus folders in the same window/a new Tab
	# => Only one instance of Nautilus will be running.  
	# Dependencies: nautilus, xdotool                    
	
	#################       USAGE: ./Opentab.sh [path/to/startfolder]               #################
	#                 (if you don't add a startpath, your home dir will be opened)                  #
	#                                                                                               #
	#       You could also copy it to /usr/bin/tabnautilus to start it with the cmd tabnautilus     #
	#                                                                                               #
	#       NOTE: If you're experience conflicts with some charaters in your argument-sting         #
	#       please check if you set the right keyboard layout in you xorg.conf, e.g.:               #		
	#       Option "XkbLayout" "de"         #for German keyboard layout                             #
	#       or run e.g. 'setxkbmap de' before this script!                                          #
	#                                                                                               #
	#       Please also note that this might not work if nautilus handles the desktop.              #
	#                                                                                               #
	#                                  Have a lot of phun! =)                                       #
	#################################################################################################

	# search for open nautilus window
	window="$(xdotool search --onlyvisible --class nautilus | head -1)"

	# check if opened nautilus was found
	if [ "$window" = "" ]; 	
	then
		echo "Nautilus not found. Starting new instance of it..."
		nautilus $* 2>&1 > /dev/null &
		exit

	else # nautilus is already open :]

		# select the window
		xdotool windowfocus --sync $window
		# add tab and focus adress field
		xdotool key --clearmodifiers ctrl+t+l+BackSpace 

		# wait some time to avoid problems
		sleep 0.2

		# custom path
		if [ $# -gt "0" ]; 
		then
			xdotool type $*

		else # no script arguments 
			xdotool type /home/$(whoami)/
		fi
		
		xdotool key Return+Escape
		xdotool windowactivate --sync $window	
	fi


Benutzung
=========
Nach einem

<blockquote>chmod +x Opentab.sh</blockquote>

...kann ein neuer Nautilustab einfach mit

<blockquote>./Opentab.sh Pfad/zu-einem/Ordner</blockquote>

...hinzugefügt werden. Bei Bedarf kann das Script natürlich auch nach /usr/bin kopiert werden, damit es von überall aus aufrufbar ist.

Nachteile von xdotool
======================
Neben den vielen Möglichkeiten, die sich mit <em><strong>xdotool</strong></em> bieten, muss man leider auch einige Schwächen in Kauf nehmen. Da die laufende Anwendung immer erst gesucht werden muss und in der Regel auf dem System natürlich mehrere Anwendungen laufen, die auch auf die Benutzereingaben reagieren, kommen die Tastensignale nicht immer korrekt &amp; teilweise zu langsam an. Ich musste in meinem Script beispielsweise auch ein kurze Wartezeit mittels des sleep-Befehls einbauen, damit dieses stabiler funktioniert hat.
Für einfache Makro- &amp; Automatisierungsaufgaben ist xdotool aber in jedem Fall ein cooles Spielzeug! :) Auf der <a href="http://www.semicomplete.com/projects/xdotool/">Homepage</a> gibt es einige Beispiele sowie eine <a href="http://www.semicomplete.com/projects/xdotool/xdotool.xhtml">Dokumentation</a> zum Tool.
