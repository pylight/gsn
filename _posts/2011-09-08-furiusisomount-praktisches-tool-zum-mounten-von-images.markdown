---
layout: post
title: FuriusISOMount - Praktisches Tool zum Mounten von Images
wordpress_id: 1604
wordpress_url: http://ganz-sicher.net/blog/?p=1604
date: 2011-09-08 21:38:21.000000000 +02:00
category: software
---
CD/DVD-Abbilder lassen sich unter Linux zwar per mount-Befehl per Konsole einbinden. Bequem ist das aber nicht, vor allem wenn man viele (z.B. durch Backups erzeugte) Images auf seinem Rechner hat. Ein komfortableres Tool zum Einbinden (und Aushängen) der Abbilder ist <a href="https://launchpad.net/furiusisomount/">FuriusISOMount</a>.

<img class="borderimg centered" title="Furius ISO Mount Tool 0.11.3.1_010" src="{{site.url}}/wp-content/uploads/Furius-ISO-Mount-Tool-0.11.3.1_010-300x172.jpg" alt="" />

Das Tool ist mit Python &amp; Gtk geschrieben und unterstützt die gänigen Image-Formate (<strong>.iso, .img, .bin, .mdf, .nrg</strong>) und können einfach gemounted (ein Mountpoint wird im Homeverzeichnis des Benutzers erstellt) und unmounted werden. Ganz praktisch ist aus, dass es eine <strong>Checksum</strong>-Funktion zur Fehlererkennung der Abbilder sowie eine Brennfunktion (mithilfe von Nautilus oder Brasero) gibt. Die Abbilder können einfach per <strong>Drag &amp; Drop</strong> in das Fenster gezogen werden.

Installation
=============
**Ubuntu (11.04):**

	sudo apt-get install furiusisomount

**Archlinux (AUR):**
	
	yaourt -S furiusisomount
