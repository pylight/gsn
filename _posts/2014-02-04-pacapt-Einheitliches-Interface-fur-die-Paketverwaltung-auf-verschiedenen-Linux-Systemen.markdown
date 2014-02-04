---
layout: post
title: pacapt - Einheitliches Interface für die Paketverwaltung auf verschiedenen Linux-Systemen
date: 2014-02-04 07:03
category: software
---
<img src="{{site.url}}/images/blog/Package.png" class="lefticon" alt="" />
Die Linux-Distribution meiner Wahl ist [Archlinux](https://www.archlinux.org), das hatte ich schon an verschiedenen Stellen in diesem Blog durchblicken lassen. Dennoch muss/darf ich häufig auch mit anderen Linux-Systemen arbeiten. Gerade bei Debian & und Ubuntu stört mich bei der Paketverwaltung, dass man für verschiedene Aktionen komplett andere Befehle in der Konsole aufrufen muss. Die Anwendung [Pacapt](https://github.com/icy/pacapt) überträgt das Kommando-Interface von [Pacman](https://wiki.archlinux.de/title/pacman) (Paketmanager unter ArchLinux) auch auf andere Distributionen.
<!--more-->

	# system updaten
	at-get update && apt-get upgrade => pacapt -Syu

	# Paket 'fun' installieren
	apt-get install fun => pacapt -S fun

	# Paket 'donuts' komplett löschen
	apt-get remove donuts --purge => pacapt -Rs donuts

	# nach einem Paket mit 'muffins' im Namen/Beschreibung suchen
	apt-cache search muffins => pacapt -Ss muffins

	# installierte Pakete auflisten
	dpkg --get-selections => pacapt -Q

	# infos über installiertes paket 'cupcake' anzeigen (z.B. version)
	apt-cache show cupcake => pacapt -Qi cupcake

Die oben gezeigten Beispiele zeigen eine Gegenüberstellung wichtiger Befehle mit aptitude (Ubuntu/Debian) und pacapt. Letzteres kann noch einige weitere Paket-Queries durchführen, welche auf der [Github-Seite](https://github.com/icy/pacapt) oder mittels <code>pacapt -h</code> eingesehen werden können. Neben den genannten Systemen kann pacapt auch unter anderen Distributionen wie z.B. Gentoo, Fedora oder Opensuse und sogar unter Mac OS X verwendet werden. 
Eine super Sache, denn so kann man die Paketverwaltung mit einer homogenen, einfachen Schnittstelle bedienen und spart sich einige Zeit und google-Arbeit. :)
