---
layout: post
title: Weshalb Archlinux die Distribution meiner Wahl ist...
wordpress_id: 1433
wordpress_url: https://ganz-sicher.net/blog/?p=1433
date: 2011-09-01 13:05:00.000000000 +02:00
category: linux-distributionen
---
<img class="lefticon" src="{{site.url}}/wp-content/uploads/archlinux_small.png" alt="" width="66" height="65" />

Wenn man sich für Linux entscheidet, steht man häufig vor der Frage "<em>Welche <a href="http://de.wikipedia.org/wiki/Distribution_(Software)">Distribution</a> verwende ich denn jetzt?</em>". Auf <a href="http://www.distrowatch.com/">Distrowatch</a> gibt es eine Übersicht der Linux-Distributionen. Es sind angeblich 312 aktive, was die Sache nicht gerade leichter macht...
Deswegen habe ich in diesem Artikel die Gründe zusammengefasst, weshalb ich mich für <a href="http://www.archlinux.org/">Archlinux</a> entschieden habe. Archlinux gefällt mir sehr als Distribution, aber ich habe auch versucht, die Nachteile (die es bei <em>jeder</em> Distribution gibt) anzugeben, damit Niemand die falsche Wahl trifft. ;)
<!--more-->

Freiheit, Flexibilität &amp; Zielgruppe
=========================================
Archlinux hat für mich einen entscheidenden Vorteil gegenüber den meisten bekannten Linux-Distributionen: Es kommt nicht einer vorgegebenen Desktop-Umgebung daher. Die grafische Oberfläche muss nachträglich installiert werden. (es gibt auch andere <a href="https://wiki.archlinux.org/index.php/Arch_Based_Distributions_(Active)">Arch-Distributionen</a> mit Desktop) Für etwas erfahrenere Linux-User bedeutet das, dass Archlinux sehr vielseitig eingesetzt werden und das System nahezu beliebig an die eigenen Bedürfnisse angepasst werden kann. Es heißt auch, dass man keine Anwendungen "vorgesetzt bekommt", die man nicht benötigt (und damit i.d.R. auch ein schnelleres Grundsystem hat). Andererseits bedeutet es aber auch, dass Archlinux nicht für blutige Linux-Anfänger gedacht ist. Die gängigen Grundbefehle sollte man beherrschen, außerdem sollte der Wille/die Geduld vorhanden sein, sich das nötige Wissen aus dem (guten) <a href="https://wiki.archlinux.org/">Archlinux Wiki</a> (<a href="https://wiki.archlinux.de/">kleineres dt. Wiki</a>) anzueignen.

Einfach und aufgeräumt
=======================
Dennoch is Arch nicht kompliziert oder schwer. Archlinux hält sich an das <a href="https://wiki.archlinux.de/title/KISS-Prinzip">KISS-Prinzip</a> (Keep it simple, stupid.) und versucht dabei nichts zu verschleihern. Ein Satz des Arch-Erfinders und Hauptentwicklers <span style="font-family: sans-serif; font-size: 13px; line-height: 19px; background-color: #ffffff;">Judd Vinet dazu:</span>
> „Wenn Du versuchst, die Komplexität des Systems zu verschleiern, landest Du am Ende bei einem viel komplexeren System.“
Bei Archlinux versteht man also was man tut und kennt mit der Zeit sein System. Es gibt einige wichtige Konfigurationsdateien, sobald man diese jedoch kennt (siehe *Installationsanleitungen* unten), ist der Umgang mit Archlinux vergleichsweise simpel.

Riesige Software-Auswahl und immer neuste Versionen dank AUR
=============================================================
Die offiziellen Paktequellen (sie werden mit dem Programm <a href="https://wiki.archlinux.org/index.php/Pacman">pacman</a> verwaltet) werden in Archlinux durch das sogenannte Arch User Repository, kurz <a href="https://aur.archlinux.org/">AUR</a> ergänzt. Dabei handelt es sich um von Benutzern eingestellte Pakete, die passende Kompilierungsinformationen (mit Abhängigkeiten) haben, um weitgehend automatisch aus dem Quellcode übersetzt werden zu können.
Die Flags für die Verwaltung mit Pacman mögen zu Beginn verwirrend sein (<em>z.B. pacman -S zum installieren, pacman -Ss zum Suchen, pacman -R zum Entfernen, pacman -Syu für's Systemupdate</em>) sind dann aber schneller zu handhaben als z.B. bei <a href="http://www.ubuntu.com/">Ubuntu</a>/Aptitude (<em>dpki -i zum installieren, apt-cache search zum Suchen und apt-get install zum Installieren, apt-get update und apt-get upgrade für's Update</em>). Auch gibt es Paketmanager die sowohl die Pacman-Repositorys als auch das AUR verwalten können, wie z.B. <a href="https://wiki.archlinux.org/index.php/Yaourt">yaourt</a>. Das ist ein Hauptgrund weshalb ich Arch einsetze, denn die Paketverwaltung mit yaourt per Terminal ist einfach viel Praktischer als irgendwelche *.deb oder *.rpm-Pakete im Netz suchen zu müssen:

<a href="{{site.url}}/wp-content/uploads/terminal.jpg"><img src="{{site.url}}/wp-content/uploads/terminal.jpg" alt="" width="470" height="470" /></a>

Mit yaourt können natürlich auch AUR-Pakete mitaktualisiert (<em>yaourt -Syua</em>), oder nur die AUR-Pakete aktualisiert werden (<em>yaourt -Sbua</em>). Ein Blick in's <a href="https://wiki.archlinux.org/">Wiki</a> lohnt sich (wie so oft), beispielsweise kann man auch die installierten Pakete per <em>yaourt -Qm</em> (äquivalent bei pacman) auflisten.

Rolling Release und Stabilität
===============================
Anders als Distributionen wie <a href="http://fedoraproject.org/">Fedora</a> oder <a href="http://www.ubuntu.com/">Ubuntu</a> ist Archlinux eine <a href="http://de.wikipedia.org/wiki/Rolling_Release">Rolling Release</a> Distribution. Das bedeutet, dass hier nicht alle paar Monate neue Versionen herausgebracht werden, sondern dass das System laufend aktualisiert werden kann, ohne extra neue Versionen herunterladen und installieren zu müssen. Für mich ist das ein großer Vorteil, denn ich möchte nicht unbedingt alle paar Monate eine Neuinstallation machen! Bei Pacman und der Paketverwaltung von Archlinux muss andererseits aber auch erwähnt werden, dass Updates sehr schnell verfügbar sind und es bei mir stellenweise schon zu Problemen nach Updates kam: So musste z.B. schon einmal der Druckertreiber (cups) nach einem Update neu eingestellt werden, Module von VirtualBox müssen regelmäßig nach einem Kernelupdate neu generiert werden usw..

Fehlende "Komfortfunktionen" &amp; "The Arch Way"
=================================================
Wie bereits gesagt kommt Archlinux nur mit einer eher <em>spartanischen Grundausstattung</em> (Linux selbst + einige Bash-Tools) daher. Das hat Vorteile (siehe "<em>Freiheit</em>" oben) sowie Nachteile. Fans von Ubuntu wird womöglich einiges an Komfortfeatures fehlen. Beispielsweise ist die Installation von Treibern z.B. bei Druckern weniger einfach, denn Ubuntu kommt schon mit vielen vorinstallierten Treibern daher und kann viele Geräte daher automatisch erkennen. Archlinux ist auch <em>kein Ersatz</em> für Distributionen wie Ubuntu, denn es ist basiert auf einer anderen Philosophie und wendet sich an eine andere Zielgruppe. Siehe dazu: <a href="https://wiki.archlinux.org/index.php/The_Arch_Way">https://wiki.archlinux.org/index.php/The_Arch_Way</a>. Wer sein System unter Kontrolle haben und verstehen möchte und wem neue Software wichtig ist, kann mit Archlinux sehr glücklich werden. ;-)

Problemhilfe? Gute Community!
=============================
Wer in das <a href="https://wiki.archlinux.org/">ArchWiki</a> oder das <a href="https://bbs.archlinux.org/">Forum</a> schaut wird schnell feststellen, dass ein großer Vorteil von Archlinux die aktive und Hilfsbereits Community der Distribution ist. Bei Problemfällen die nicht im Wiki beschrieben sind, bekommt man im Forum mit Sicherheit zügig Hilfe. Wenn ich mir eine neue Distribution suchen würde, wären übersichtliche Anleitungen und gute Anlaufstelle bei Problemen die Hauptargumente. Beides ist meiner Meinung nach bei Archlinux durchaus vorhanden.

Neugierig geworden? Weiterführende Links
==========================================
* [http://board.gulli.com/thread/1219910-tutorial-workshop-linux-verstehen-und-einsetzen](http://board.gulli.com/thread/1219910-tutorial-workshop-linux-verstehen-und-einsetzen) (Gute Einführung in Linux und Archlinux)
* [https://wiki.archlinux.de/title/Offizielle_Arch_Linux_Installations-Anleitung](https://wiki.archlinux.de/title/Offizielle_Arch_Linux_Installations-Anleitung)
* [Archlinux.org](http://www.archlinux.org) sowie das [ArchLinux Wiki](https://wiki.archlinux.org/)
