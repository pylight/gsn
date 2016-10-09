---
layout: post
title: Filezilla und die gespeicherten Passwörter
wordpress_id: 1131
wordpress_url: https://ganz-sicher.net/blog/?p=1131
date: 2011-03-18 22:39:20.000000000 +01:00
category: tutorials-tipps
---
<img class="lefticon" src="{{site.url}}/wp-content/uploads/filezilla.png" alt="" />

[FileZilla](http://filezilla-project.org/) gefällt mir als FTP-Client sehr gut, gerade weil es Open Source und damit für mehrere verschiedene Plattformen verfügbar ist. Weniger gefällt mir, dass FileZilla immer die Passwörter meiner zuletzt benutzen FTP-Verbindungen als Klartext in einer XML-Datei speichert...
<!--more-->

Das Problem
===========
FileZilla legt im <span style="text-decoration: underline;">Konfigurationsordner</span> (<strong>Windows 7</strong>: <span style="font-family: arial, sans-serif; line-height: 15px; font-size: small;">C:\Users\<em>Benutzername</em>\AppData\Roaming\FileZilla | <strong>Linux</strong>: ~/.filezilla) standardmäßig immer die datei <em>recentservers.xml</em> für Quickconnects (Verbindungen über die Eingabefelder in der Toolbar) und eine <em>sitemanager.xml</em> für Verbindungen mit dem Servermanager (Datei -&gt; Servermanager bzw. File -&gt; Site-Manager) an. Schaut man sich diese Dateien genauer an, sieht man, dass die benutzen Passwörter dort im Klartext abgespeichert werden:</span>

<img class="borderimg" src="{{site.url}}/wp-content/uploads/sitemanager-xml.gif" alt="" width="436" height="360" />

Dies ist laut Entwickler angeblich so gewollt, im offiziellen FileZilla-Forum gab es <a href="http://forum.filezilla-project.org/viewtopic.php?f=2&amp;t=7800">auf eine Frage dazu</a> die Antwort:
> "This is by design, it is the task of the operating system to protect your private data."
Die Erklärung, dass das Betriebsystem für die Sicherheit der Daten zuständig ist, mag zwar auf den ersten Blick richtig sein. Andererseits halte ich es dennoch für recht unverantwortlich, solche Daten im Klartext abzuspeichern. Kein Betriebsystem kann 100%ige Sicherheit garantieren. Software ist heute auch so komplex, dass der Nutzer nicht zwingend einen Fehler machen muss, damit Schadsoftware auf den eigenen Rechner gelangen kann. Schon einfache Baukasten-Trojaner könnnen so die Passwörter auslesen. Daher habe ich mal nach einem Weg gesucht, die Klartext-Speicherung der Passwörter zu verhindern.

Keepass zum Speichen der Passwörter verwenden
==============================================
Ich bin ein großer Fan von <a href="http://keepass.info/">Keepass</a> (<a href="http://www.keepassx.org/">keepassx</a> unter Linux). Mit diesem Tool ist es möglich, die Zugangsdaten in einer verschlüsselten Datei/Datenbank abzuspeichern. Trotzdem wird das Verbinden zu verschiedenen FTP-Servern nicht wesentlich komplizierter als mit der Quickconnect-Funktion in FileZila!

Keepass-Einstellungen vornehmen
--------------------------------
Um die FTP-Passwörter sicherer zu speichern, muss eine passwortgeschützte Keepass-Datenbank erstellt werden. Pro FTP-Verbindung wird nun ein neuer Eintrag angelegt. Ich speichere dabei die Serveradresse im Titel-Eingabefeld des  Eintrags und gebe in den Feldern für Benutzername und Passwort die passenden Verbindungsdaten an. In das Adressfeld (URL) wird der Speicherort von Filezilla mit vorangehendem <em>cmd://</em> eingetragen, also unter Windows  beispielsweise <strong><em>cmd://"C:\Program Files\FileZilla FTP Client\filezilla.exe"</em></strong>, bei Linux-Distributionen z.B. <em><strong>cmd://"/usr/bin/filezilla"</strong></em>. Dadurch kann Filezilla immer direkt per Tastenkombination (STRG + U)  von Keepass aus gestartet werden.
Damit die Daten auch immer bei Filezilla eingefügt werden, kann das <em>Auto-Type</em>-Feature von Keepass benutzt werden. Dabei handelt es sich um eine Art Makrofunktion, die einfach im <em>Kommentarfeld</em> des jeweiligen Eintrags eingestellt werden kann. In unserem Fall fügen wir einfach irgendwo im Kommentarfeld den folgenden Text ein:
<blockquote>Auto-Type: {TITLE}{TAB}{USERNAME}{TAB}{PASSWORD}{ENTER}</blockquote>
Selbstverständlich kann diese Funktion auch noch individuell angepasst werden. Weitere Hinweise dazu finden sich im <a href="http://keepass.info/help/base/autotype.html">Keepass Help Center</a>.

FileZilla mithilfe von Keepass verwenden
-----------------------------------------
Wurden die oben genannten Einstellungen vorgenommen, kann FileZilla immer mit der Tastenkombination <span style="text-decoration: underline;"><em>STRG + U</em></span> (alternativ natürlich auch manuell) gestartet werden. Wenn der Cursor im Host-Eingabefeld in der FileZilla-Toolbar steht, kann dann wieder zu Keepass gewechselt werden und die Auto-Type-Funktion mit der Tastenkombination <span style="text-decoration: underline;"><em>STRG + V</em></span> aufgerufen werden. Alternativ lässt sich auch in den Keepass-Einstellungen eine globale Tastenkombination für diese Funktion festlegen. Keepass füllt dann automatisch die benötigten Felder aus und verbindet zum angegeben FTP-Server.
<h3>FileZilla davon abhalten, Passwörter zu speichern</h3>
Funktioniert die Eingabe und Verbindung mithilfe von Keepass, muss Filezilla natürlich noch so konfiguriert werden, dass keine Kennwörter mehr in den .xml-Dateien hinterlegt werden. Um dies zu erreichen, muss die Datei <em>fzdefaults.xml.example </em>in den Konfigurationsordner (siehe oben) kopiert und in <em>fzdefaults.xml </em>umbenannt werden. Außerdem muss in der Datei die Einstellung <em>Kiosk Mode</em> aktiviert werden, was durch Ändern der Zeile:
<blockquote>&lt;Setting name="Kiosk mode"&gt;<strong>1</strong>&lt;/Setting&gt;</blockquote>
...erreicht wird. Die Datei <em>fzdefaults.xml.example</em> befindet sich im docs Ordner (unter Windows im FileZilla Installationsverzeichnis, unter Linux unter <em>/usr/share/filezilla/docs</em>). Unnötige Einstellungen in der <em>fzdefaults.xml, </em>wie z.B. die Zeile <em>&lt;Setting name="Config Location"&gt;$SOMEDIR/filezilla/&lt;/Setting&gt; </em>sollten entfernt werden, um Fehler zu vermeiden. Auch in der Konfigurationsdatei <em>filezilla.xml</em> muss unter Umständen noch die Einstellung für <em>Kiosk Mode</em> auf 1 gesetzt werden.
Sofern alles geklappt hat, sollte FileZilla fortan keine Passwörter mehr speichern. Die Dateien <em>recentservers.xml</em> und <em>sitemanager.xml</em>, die eventuell noch sensible Daten enthalten sollten dann auch entfernt werden.

**Tipp:** Sollte sich der gewünschte Effekt nicht einstellen und FileZilla nach wie vor Passwörter abspeichern kann auch mit der <em>Holzhammermethode</em> unter Linux der Lese-/Schreibzugriff auf die beiden Dateien mit einem

	chmod -rw dateiname

verhindert werden. Unter Windows gibt es für einen Sicheren Modus auch entsprechende Einträge in der Regestry, welche auf '1' gesetzt werden können:
> HKEY_LOCAL_MACHINE\SOFTWARE\FileZilla\Run in Secure Mode
sowie
> HKEY_USERS\[username]\Software\FileZilla\Run in Secure Mode

Auch die Serveradresse verschleiern
====================================
Mit dem oben beschriebenen Verfahren können eventuell noch Serveradresse und Benutzername von einem FTP-Zugang ausgelesen werden. Ein weiterer kleiner Trick kann auch die Serveradresse verschleiern:

Aliasnamen für Serveradresse festlegen:
----------------------------------------
Durch Anpassen der Hostsdatei, z.B. mit dem notepad-Editor (unter Windows ist die Datei unter *Windowsverzeichnis*/system32/drivers/etc/hosts, bei Linux unter /etc/hosts) kann für die eigene Serveradresse ein Aliasnamen bestimmt werden. Dazu wird einfach in die Datei eine Zeile nach dem Muster <em>*Serveradresse* Aliasname</em> eingefügt, also z.B.:
> 188.40.182.70 meinetolleseite

Aliasname verwenden
====================
Nach Ändern der hosts-Datei kann anschließend im Keepass-Eintrag (bzw. in Filezilla) statt der Serveradresse immer Aliasname verwendet werden. Dies hat zum Vorteil, dass natürlich auch in der Konfigurationsdatei statt der eigentlichen Adresse der Aliasname abgespeichert wird. Die reale Adresse des Servers kann so für simple Schadprogramme schwerer herausgefunden werden.

Andere Meinungen erwünscht!
============================
Welchen FTP-Clienten benutzt du? Oder hast du noch weitere Tipps, wie die Verbindung zu einem FTP-Server mit Filezilla sicherer gemacht werden könnte? In jedem Fall freue ich mich über eurer Feedback. ;-)
