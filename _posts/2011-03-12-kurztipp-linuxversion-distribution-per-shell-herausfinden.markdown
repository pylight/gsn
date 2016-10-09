---
layout: post
title: ! '[Kurztipp] Linuxversion/-distribution per Shell herausfinden'
wordpress_id: 1070
wordpress_url: https://ganz-sicher.net/blog/tutorials-tipps/kurztipp-linuxversion-distribution-per-shell-herausfinden/
date: 2011-03-12 01:02:00.000000000 +01:00
category: tutorials-tipps
---
Wenn man auf einen (fremden) Linuxsystem Software &Auml;nderungen durchf&uuml;hren will, ist es oft von Vorteil, Linuxversion und -distribution zu kennen. Mit den nachfolgenden Shellbefehlen bekommt man schnell geeignete Informationen. (nicht jede Distribution verh&auml;lt sich hier gleich, daher die verschiedenen Ans&auml;tze)
<!--more-->

Kernelversion
=============
Die Linuxkernel-Version findet man in der Regel heraus mit

	uname -a

Distribution
=============
Bei einigen Distributionen (z.B. Debian, Ubuntu) gibt es einen extra Befehl zu diesem Zweck:

	lsb_release -a

Eventuell hilft das Auslesen der Informationen vom Bootvorgang (head -5 besch&auml;nkt Ausgabe auf erste 5 Zeilen)
dmesg | head -5

Bei einzelnen Distributionen gibt es spezielle Dateien, die Datei-Ausgabe (cat-Befehl) von...
	
	cat /etc/*release

oder

	cat /etc/*version

oder

	cat /etc/issue

oder ein

	cat /proc/version

..f&uuml;hrt oft zum gew&uuml;nschten Ergebnis
