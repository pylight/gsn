---
layout: post
title: Rsnapshot - Automatisierte Backups leicht gemacht
wordpress_id: 1635
wordpress_url: http://ganz-sicher.net/blog/?p=1635
date: 2011-10-03 12:27:38.000000000 +02:00
---
<a href="http://ganz-sicher.net/blog/wp-content/uploads/backups.png"><img class="size-full wp-image-1649 alignleft" title="backups" src="http://ganz-sicher.net/blog/wp-content/uploads/backups.png" alt="" width="32" height="32" /></a>Ich geb's ja zu! Ich habe bisher höchstens manuelle Backups gemacht. Wiederkehrende Erfahrungen mit kaputten Festplatten, versehentlich gelöschten Daten oder <em>verschlimmbesserten</em> Konfigurationsdateien haben mich dann aber doch motiviert, mich etwas intensiver mit der Thematik zu befassen. Und es kann tatsächlich so einfach sein: In meinem Fall heißt die Antwort <a href="http://rsnapshot.org/">rsnapshot</a> - ein kleines Shelltool, mit dem man regelmäßige Backups machen kann.
<h3><!--more--></h3>
<h3>Vorausgehende Fragen (und Antworten)</h3>
Wer sich mit Backups beschäftigt, sollte einige Fragen vorausschicken, damit ein sinnvolles Backupsystem entsteht:

<strong>Wohin sollen meine Daten gespeichert werden?
</strong>Hier bietet sich natürlich an, eine logisch und physikalisch vom normalen System getrennte Festplatte zu wählen. Mit rsnapshot ist aber beispielsweise auch ein Backup per SSH auf einem entfernten Server möglich.

<strong>Was will ich backupen? In meinem Fall:</strong>
<ul>
	<li>/home-Verzeichnis</li>
	<li>/etc und /var für die Einstellungen</li>
	<li>/usr für lokal installierte Programme</li>
	<li>/boot für die Bootinformationen</li>
</ul>
<strong>Wie oft will ich meine Daten backupen?
</strong>Ich habe dazu ein Script geschrieben (dazu unten mehr), welches als Cronjob täglich und monatlich aufgerufen wird. Außerdem habe ich rsnapshot so eingestellt, dass nach 5 Tagen bzw. 3 Monaten die Daten wieder überschrieben werden.

<strong>Besonders wichtig: Wie werden die Daten später wiederhergestellt?
</strong>Im Falle von rsnapshot kann man sie einfach aus dem Backupverzeichnis kopieren.
<h3>Warum rsnapshot?</h3>
Auf der Suche nach einem <strong>unkomplizierten</strong> und möglichst <strong>schlanken</strong> Backuptool, bin ich auf rsnapshot gestoßen. Wie viele Backuptools, verwendet Rsnapshot das altbewährte <a href="http://wiki.ubuntuusers.de/rsync">rsync</a> für Backups. Eine Besonderheit von rsnapshot ist, dass nur beim ersten Mal eine komplette Kopie der Daten erfolgt. Anschließend werden nur noch diejenigen Dateien kopiert, die sich geändert haben, für alle Anderen werden <strong>Hardlinks</strong> zum ersten Backup gesetzt. Das spart natürlich Platz und wirkt sich auch deutlich positiv auf die Laufzeit der nachfolgenden Backups aus.
Die Dateien werden unkomprimiert in der selben Verzeichnisstruktur wie auf dem eigentlichen System abgelegt, was die Wiederherstellung einzelner Dateien natürlich erleichtert.
Ich denke auf Desktopsystemen reicht es auch, eine Kopie der aktuellen Datei zu haben,  auf Serversystemen, auf denen Datensicherheit besonders wichtig ist, muss man sich natürlich überlegen, ob man nicht lieber zu einem Tool greifen möchte, das jedes Mal "komplette" Backups anlegt.
<h3>Rsnapshot konfigurieren</h3>
Die Konfigurationsdatei (Standard: <em>/etc/rsnapshot.conf</em>) ist gut kommentiert und schnell angepasst. Im Wesentlichen müssen hier nur ein Zielverzeichnis (snapshot_root), die Backuppoints (Verzeichnisse, die gespeichert werden sollen) und eventuelle Ausnahmen (exclude-Anweisungen) festgelegt werden. Außerdem sollte man auswählen, welche in Zeiträumen (und wie lange) die Daten gesichert werden sollen. Danach kann das Backup schon mittels <em>z.B. rsnapshot -t daily</em> getestet und mit <em>rsnapshot -v daily</em> durchgeführt werden!
<h3>Rsnapshot Backupscript (Backup auf gesonderte Platte)</h3>
Ich habe mir ein kleines Script geschrieben, damit meine Backuppartition (die ich zuvor in <em>/etc/fstab</em> eingetragen habe) automatisch gemountet wird und ich entsprechende <em>Notifications</em> über das Backup in Gnome bekomme. Außerdem erstellt das Script anschließen immer eine Liste der installierten Pakete (Pacman / Archlinux). Ich habe dieses Script unter <em>/etc/cron.daily</em> sowie (in angepasster Form) nach <em>/etc/cron.monthly</em> gepackt, damit regelmäßige Backups abgelegt werden können. Falls Fehler beim Backup auftreten, werden diese auf der Backupplatte in einer errors.log gespeichert und es erscheint passende Benachrichtigung auf dem Desktop.

<a href="http://ganz-sicher.net/blog/wp-content/uploads/backup_successful.png"><img class="alignleft size-medium wp-image-1638" title="backup_successful" src="http://ganz-sicher.net/blog/wp-content/uploads/backup_successful-300x36.png" alt="" width="300" height="36" /></a>

&nbsp;

&nbsp;

<strong>Wer Interesse hat, darf das <a href="http://www.ganz-sicher.net/scripts/myscripts/dailybackup">Script</a> natürlich nach Belieben an die eigenen Bedürfnisse anpassen.</strong>. Garantie, dass das Script funktioniert, gibt's natürlich nicht - Verbesserungsvorschläge sind immer willkommen! ;)
