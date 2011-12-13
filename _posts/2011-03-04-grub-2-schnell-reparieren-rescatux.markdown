---
layout: post
title: ! 'Grub 2 schnell reparieren: Rescatux'
wordpress_id: 983
wordpress_url: http://ganz-sicher.net/blog/ubuntu/grub-2-schnell-reparieren-rescatux/
date: 2011-03-04 22:09:16.000000000 +01:00
category: linux-distributionen
---
Wer mehrere (Linux)Betriebsysteme parallel auf einem Rechner installiert hat, wird eventuell auch schonmal das zweifelhafte Vergn&uuml;gen gehabt haben, den Grub (2) Bootmanager reparieren zu m&uuml;ssen. Wenn gleich Grub 2 theoretisch mit den meisten Linux Live-CDs zu reparieren ist, so ist es doch sch&ouml;ner, wenn man dann etwas zur Hand hat, das die Wiederherstellung erleichtert und beschleunigt.
<!--more-->

Ich kannte bisher nur <a href="http://www.supergrubdisk.org/super-grub-disk/">Super Grub Disk</a> (<a href="http://www.supergrubdisk.org/super-grub2-disk/">2</a>), wobei <em>Super Grub Disk 2</em> den Nachteil hatte, dass nur von der CD gebootet und keine &Auml;nderungen auf die Festplatte geschrieben wurden.


Nachdem ich jetzt mal wieder mein Grub 2 zerschossen hatte, bin ich auf <a href="http://www.supergrubdisk.org/rescatux/">Rescatux</a> auf der selben Seite aufmerksam geworden. Im Gegensatz zu den "Vorg&auml;ngern" basiert dies auf Debian und bietet die M&ouml;glichkeit, sowohl Grub 1, als auch Grub 2 mit grafischer Oberfl&auml;che wiederherzustellen. Au&szlig;erdem bietet das Tool die M&ouml;glichkeit an, ein Filesystem zu &uuml;berpr&uuml;fen.&nbsp;

<img class="borderimg centered" src="{{site.baseurl}}/wp-content/uploads/rescatux_main_menu.png" alt="" width="607" height="425" />

Die Erkennung der installierten Distributionen klappte bei mir problemlos - Wer sich also unter Umst&auml;nden einige nervt&ouml;tende Momente ersparen m&ouml;chte, sollte vielleicht erstmal einen Blick darauf werfen.&nbsp;
Ein weiteres n&uuml;tzliches Tool zum einfachen Anpassen (z.B. Festlegen eines Hintergrundbildes, &Auml;ndern der Eintr&auml;ge oder der Anzeigedauer) des Bootmanagers ist (mit grafischer Oberfl&auml;che) <a href="https://launchpad.net/grub-customizer">Grub Customizer</a>.&nbsp;
