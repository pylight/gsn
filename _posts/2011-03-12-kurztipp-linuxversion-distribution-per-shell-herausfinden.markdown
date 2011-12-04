---
layout: post
title: ! '[Kurztipp] Linuxversion/-distribution per Shell herausfinden'
wordpress_id: 1070
wordpress_url: http://ganz-sicher.net/blog/tutorials-tipps/kurztipp-linuxversion-distribution-per-shell-herausfinden/
date: 2011-03-12 01:02:00.000000000 +01:00
---
<p>Wenn man auf einen (fremden) Linuxsystem Software &Auml;nderungen durchf&uuml;hren will, ist es oft von Vorteil, Linuxversion und -distribution zu kennen. Mit den nachfolgenden Shellbefehlen bekommt man schnell geeignete Informationen. <span style="font-size: x-small;">(nicht jede Distribution verh&auml;lt sich hier gleich, daher die verschiedenen Ans&auml;tze)</span>

<span style="font-size: x-small;"><!--more--></span></p><h3>Kernelversion</h3><p>Die Linuxkernel-Version findet man in der Regel heraus mit
 <blockquote>uname -a</blockquote></p><h3>Distribution</h3><p>Bei einigen Distributionen (z.B. Debian, Ubuntu) gibt es einen extra Befehl zu diesem Zweck:
 <blockquote>lsb_release -a</blockquote>

Eventuell hilft das Auslesen der Informationen vom Bootvorgang (head -5 besch&auml;nkt Ausgabe auf erste 5 Zeilen)
 <blockquote>dmesg | head -5</blockquote>

Bei einzelnen Distributionen gibt es spezielle Dateien, die Datei-Ausgabe (cat-Befehl) von...
 <blockquote>cat /etc/*release</blockquote>

oder

<blockquote>cat /etc/*version</blockquote>

oder

<blockquote>cat /etc/issue</blockquote>

oder ein

<blockquote>cat /proc/version</blockquote>

..f&uuml;hrt oft zum gew&uuml;nschten Ergebnis</p>
