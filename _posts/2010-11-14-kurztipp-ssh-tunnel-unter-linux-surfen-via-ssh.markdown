---
layout: post
title: ! '[Kurztipp] SSH-Tunnel unter Linux / Surfen via SSH'
wordpress_id: 828
wordpress_url: http://ganz-sicher.net/blog/tutorials/kurztipp-ssh-tunnel-unter-linux-surfen-via-ssh/
date: 2010-11-14 04:27:33.000000000 +01:00
category: tutorials-tipps
---
<img class="lefticon" src="{{site.url}}/wp-content/uploads/ssh.png" alt="ssh" />
Wer aus bestimmten Gründen eine verschlüsselte Datenverbindung zu einem anderen Rechners oder Servers aufbauen möchte, benutzt dazu in der Regel <a href="http://wiki.ubuntuusers.de/ssh">ssh</a>. Voraussetzung dafür ist nur, dass auf dem Zielrechner, ein ssh-Server/-Daemon läuft. Ebenso leicht kann man auch mittels SSH-Tunnel über einen entfernten PC im Netz surfen...
<!--more-->
Im Linuxterminal einfach per ssh mit der Option -D und dem entsprechenden Port verbinden:
<img class="borderimg centered" src="{{site.url}}/wp-content/uploads/ssh_term.png" alt="Beispiel: ssh -D 1080 user@ganz-sicher.net" width="531" height="104" />

Nun müssen wir unserem Browser (in meinem Beispiel der Firefox) nur noch den Port mitteilen:
<img class="borderimg centered" style="display: block; margin-left: auto; margin-right: auto;" src="{{site.url}}/wp-content/uploads/firefox_proxy.png" alt="Firefox Proxy/Port Einstellungen" />

...und schon läuft die Datenverbindung über den entfernten Rechner :). Ob alles geklappt hat, könnt ihr beispielsweise testen, indem ihr auf <a title="Wie ist meine IP-Adresse?" href="http://www.wieistmeineip.de/">http://www.wieistmeineip.de/</a> und nachschaut, ob dort die IP eures Zielrechners/-servers angezeigt wird.

***Hinweis:*** Damit der Firefox mitspielt, muss in der about:config (in der Adresszeile eingeben) der Wert <em>network.proxy.socks_remote_dns</em> auf <em>true</em> gesetzt sein!
