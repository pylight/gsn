---
layout: post
title: Bleachbit - Unnötige (Cache)-Daten im System entfernen
wordpress_id: 1453
wordpress_url: https://ganz-sicher.net/blog/?p=1453
date: 2011-08-30 23:05:22.000000000 +02:00
category: software
---
<img class="lefticon" title="zen_classic_logo" src="{{site.url}}/wp-content/uploads/zen_classic_logo.png" alt="" width="48" height="48" />

Moderne Betriebsysteme und Anwendungen erstellen häufig aus Performance- oder Statiskgründen (Cache)-Daten. Zum Problem wird dies, wenn solche Daten nicht temporär sind, sondern auch bestehen  bleiben, wenn sie eigentlich gar nicht mehr benötigt werden. Dieser Datenmüll belegt mit der Zeit nicht nur viel Platz auf der Festplatte, sondern kann zudem auch zum Sicherheitsrisiko werden - einige Browserdaten (besuchte Seiten,...) könnten beispielsweise von böswilligen Quellen ausgelesen werden. ;-) Das Tool <a href="http://bleachbit.sourceforge.net">Bleachbit</a> will dieses Problem anpacken und bereinigt deswegen Windows- und Linux-Systeme und -Programme von solchen Daten.
<!--more-->

Privatsphäre schützen
=====================
Windows-Benutzern fällt bei dieser Beschreibung möglicherweise <a href="http://www.piriform.com/CCLEANER">CCleaner</a> ein, was ein ganz ähnliches und auch sehr nützliches Tool, das allerdings nur für Windows verfügbar ist. Bei Bleachbit steht zudem noch die Privatspäre im Mittelpunkt, beispielsweise können auch Dateien sicher gelöscht ("geshreddert") werden oder Memory und freier Festplattenspeicher übschrieben werden, sodass keine Datenwiederherstellung möglich sein sollte. Letzteres ist vor allem dann sinnvoll, wenn eine zu löschende Datei mehrfach im System kopiert wurde und deshalb durch ein einfaches löschen nicht sichergestellt werden kann, dass die Datei nicht wiederhergestellt werden kann.
Außerdem bringt Bleachbit für viele Programme - sofern diese installiert - extra Möglichkeiten mit, deren Datenmüll zu entfernen. (<a href="http://bleachbit.sourceforge.net/features">Programmliste auf der Website</a>)

Bleachbit ist derzeit (v0.9) noch nicht in Version 1 verfügbar und könnte gerade bei den Privatsphäre-Funktionen meinem Geschmack nach noch ein paar mehr Optionen haben, dennoch ist es schon jetzt (vor allem für Linuxer) ein sehr nützliches Tool um nicht mehr benötigte Daten zu entfernen. Bei meinem Linux-System hat Bleachbit immerhin 500MB entfernt!

<div class="infobox"><strong>Vorsicht:</strong> Nicht alle Löschoptionen die Bleachbit anbietet löschen auch <span style="text-decoration: underline;">unnötige</span> Daten! Wenn du einen Haken bei einer Option machst, solltest du wissen was du tust, denn andernfalls könnten z.B. deine Account-Logins (Cookies) bei deinem Browser gelöscht werden.
Zudem benötigen einige Funktionen (z.B. das überschreiben des freien Speicherplatzes) viel Performance und sollten nur ausgeführt werden, wenn der PC auch wirklich einige Minuten lang nicht genutzt werden muss.

Links: <a class="homelink" href="http://bleachbit.sourceforge.net">Homepage von Bleachbit</a></div>


Update vom 3. September 2011:
-------------------------------
Ein weiteres sehr nützliches Tool um Datenmüll unter Linux zu entfernen habe ich in einem Blogeintrag bei <a href="http://tridex.net/2011-09-02/fslint-saubermacher-im-datensalat/">Tridex.net</a> (thx!) gefunden: <a href="http://freshmeat.net/projects/fslint">FSlint</a> (<a href="https://aur.archlinux.org/packages.php?ID=9550">AUR</a>) findet und entfernt Duplikate, fehlerhafte Dateinamen und Symlinks, leere Verzeichnisse und einiges mehr.
