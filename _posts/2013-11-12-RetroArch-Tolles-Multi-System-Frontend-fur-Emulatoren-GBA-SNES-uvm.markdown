---
layout: post
title: RetroArch - Tolles Multi-System-Frontend für Emulatoren (GBA, SNES uvm.)
date: 2013-11-12 20:00
category: software
---
<table cellpadding="0" cellspacing="0" border="0">
<tr>
<td>
<img src="{{site.url}}/images/blog/joypad.png" class="lefticon" alt="" />
</td>
<td markdown="1">
Linux wird ja in letzter Zeit auch attraktiver für Spieler: Entwicklungen wie [Steam für Linux](http://store.steampowered.com/browse/linux/?l=german), Steam OS und die [Humble Indie Bundles](https://www.humblebundle.com/) lassen hoffen, dass es in Zukunft den einen oder anderen Spiele-Titel gibt, bei dem nicht der umständlichere Weg über [Wine](http://www.winehq.org/) eingeschlagen werden muss. Doch auch alte Spiele-Klassiker sind unter Linux dank entsprechender Emulatoren kein großes Problem mehr. 
</td>
</tr>
</table>
<!--more-->
Mit [RetroArch](http://themaister.net/retroarch.html) habe ich erst kürzlich ein super FrontEnd für viele Emulatoren gefunden, mit dem man bequem viele alte Spieletitel verwalten und spielen kann: RetroArch ist modular aufgebaut und verwendet die [libretro-API](http://www.libretro.com/), eine Schnittstelle, für welche es bereits [viele Implementierungen für verschiedene Systeme](http://www.libretro.com/?page_id=218) (sogenannte Cores) gibt. Das bedeutet, dass man in der Oberfläche von RetroArch nur den entsprechenden Core und das passende Spiel wählen muss und schon kann der Spielspaß beginnen! :)

Installation & Konfiguration
============================
RetroArch ist für viele verschiedene System verfügbar, darunter Windows, Linux, Mac und Android! Unter ArchLinux findet man RetroArch, sowie viele libretro implementierungen im [AUR](https://aur.archlinux.org/). Installiert man diese, so findet man die entsprechenden Cores unter <code>/usr/lib/libretro</code> (dieses Verzeichnis am Besten in RetroArch in den "Path settings" setzten).
Für Windows gibt es auf der [Homepage](http://themaister.net/retroarch.html) bereits ein "RetroArch megapack", welches viele libretro cores enthält.

Beim Konfigurieren meiner Gamepads hatte ich einige Probleme. Dafür empfiehlt es sich, diese mit dem Befehl <code>retroarch-joyconfig</code> in der Konsole einzurichten, falls es in den Einstellungen von RetroArch selbst nicht klappen sollte. Notfalls kann die Einstellungsdatei retroarch.cfg auch mit einem Text-Editor nachträglich angepasst werden. Unter Archlinux findet man sie unter <code>~/config/retroarch/retroarch.cfg</code>.

<img src="{{site.url}}/images/blog/retroArch.jpg" class="borderimg centered" alt="" />

<div class="imageinfo">RetroArch unter ArchLinux</div>

RetroPie - die Retro-Spielkonsole
=================================
Wer einen [Raspberry Pi](http://www.raspberrypi.org/) sein Eigen nennt, kann sich vielleicht auch für das [RetorPie projekt](http://blog.petrockblock.com/retropie/) begeistern: Hier wurde RetroArch zusammen mit [EmulatorsStation](https://github.com/Aloshi/EmulationStation) für den Raspberry-Pi angepasst. Damit hat man direkt ein komplett fertiges System, welches beispielsweise per HDMI an den Fernseher angeschlossen werden kann! Ein entsprechendes Setup samt Anleitung [gibt es auf Github](https://github.com/petrockblog/RetroPie-Setup).

Viel Spaß beim Zocken! ;-)
