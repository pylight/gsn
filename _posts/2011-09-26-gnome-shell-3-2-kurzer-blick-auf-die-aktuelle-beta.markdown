---
layout: post
title: Gnome Shell 3.2 - Kurzer Blick auf die aktuelle Beta
wordpress_id: 1611
wordpress_url: http://ganz-sicher.net/blog/?p=1611
date: 2011-09-26 14:35:00.000000000 +02:00
category: kurz-notiert
---
<img class="lefticon" src="{{site.url}}/wp-content/uploads/gnome_icon1.png" alt="" width="48" height="48" />

[Gnome Shell](http://gnome3.org/) gefällt mir vom Design und den Ideen her gut, darüber hatte ich schon mehrfach hier im Blog geschrieben. Es handelt sich aber auch um ein neues Stück Software, einige Dinge fehlen daher und manches kann noch nicht überzeugen. So fehlen beispielsweise viele Einstellungsmöglichkeiten und die Performance ist vor allem auf alten Rechnern eher unzureichend. In den nächsten Tagen erscheint Gnome 3.2, das nächste große Release nach 3.0. Ich habe (unter Arch) bereits einen kurzen Blick auf die aktuelle Beta geworfen.
<!--more-->

Überarbeiteter Login-Screen, Verbesserungen bei Benachrichtigungen und der Chatintegration
=============================================================================================
Gnome 3.2 soll am 28 September erscheinen. Bereits im Juli hat der <a href="http://afaikblog.wordpress.com/2011/07/13/news-from-gnome-shell-land/">Entwickler Allan Day in seinem Blog</a> wichtige Features von 3.2 zusammengefasst. Einiges davon ist in der 2. Beta-Version (3.1.92) bereits implementiert. Der Login-Screen (<em>GDM</em>, Gnome Display Manager) präsentiert sich nun im Gnome 3-Stil (hat aber noch einige Macken, z.B. wird nicht mehr automatisch der erste Benutzer ausgewählt) und Benachrichtigungen können nun (z.B. beim Mounten) unterschiedliche Aktionen auf Benutzerwunsch ausführen. Auch wurde die Messaging-Funktion von <a href="https://live.gnome.org/Empathy">Empathy</a> weiter in die Shell integriert. So kann man nun z.B. nach seinen Kontakten im "Overview"-Modus suchen. Empathy läuft nun eher im Hintergrund, es wird standardmäßig gar kein Kontakte-Fenster angezeigt. Man gewöhnt sich schnell daran, für Anfänger könnte das aber verwirrend sein. Grafisch hat sich ein wenig was getan, z.B. kann das gnome-terminal endlich wieder transparenz :) und Rundungen bei Fenstern/Menüs sehen nun schöner aus. Sehr gut finde ich die Neuerung, dass Fenster nun <em>leichter in der Größe verändert</em> werden können, da ein <a href="http://blog.mecheye.net/2011/08/invisible-borders/">unsichtbarer Rahmen</a> um die Fenster gelegt wurde.

<a href="{{site.url}}/wp-content/uploads/term.jpg"><img class="borderimg centered" src="{{site.url}}/wp-content/uploads/term.jpg" alt="" width="450" height="370" /></a>

<div class="imageinfo">Gnome-Terminal und Nautilus unter Gnome 3.1.92</div>

Onlinekonten: Import des Google-Accounts
==========================================
Eine Funktion, die in Zukunft wohl weiter ausgebaut werden soll, ist die Möglichkeit, Einstellungen und Daten von Online-Accounts zu importieren. Mit Gnome 3.2 macht Google den Anfang, eingebunden werden können <em>Mail-Einstellungen</em> (für Evolution), <em>Kalender-Einträge</em> (für Evolution und die Shell - Evolution wird aber weiter benötigt), <em>Kontakte</em> (gnome-contacts), <em>Google-Chat-Daten</em> (Empathy) und<em> Google Docs-Dokumente</em> (gnome-documents). Die Idee ist ansich interessant, gerade bei Google-Diensten kann man aber so gut über den Browser arbeiten, dass sich mir derzeit noch nicht so ganz erschließt, warum ich die funktionsärmeren (und noch nicht sehr stabilen) Gnome-Programme nutzen sollte. ;)

<a href="{{site.url}}/wp-content/uploads/screen2.jpg"><img class="borderimg centered" src="{{site.url}}/wp-content/uploads/screen2.jpg" alt="" width="500" height="350" /></a>

<div class="imageinfo">Online-Konten und Überarbeitetes Benutzermenü</div>

Dateivorschau mit *Sushi*
==========================
Eine sehr praktische Dateivorschau steht mit einem Tool namens <em>Sushi</em> zur verfügung. Damit lassen sich viele Dateien (seien es Dokumente, Audio- oder Videodaten) durch Drücken der Leertaste ohne ein spezielles Programm in Gnome anzeigen:

<a href="{{site.url}}/wp-content/uploads/sushi.jpg"><img class="borderimg centered" src="{{site.url}}/wp-content/uploads/sushi.jpg" alt="" width="500" height="400" /></a>

<div class="imageinfo">Sushi: Einfache Dateivorschau in der Shell</div>

Überarbeitetes Erweiterungssystem
==================================
Obwohl man sich unter den Gnome-Entwicklern <a href="http://www.pro-linux.de/news/1/17161/gnome-shell-soll-repositorium-fuer-erweiterungen-erhalten.html">nicht ganz einig</a> ist, wie anpassungsfähig die Shell werden soll, ist in Zukunft geplant, dass das Erweiterungssystem eine größere Rolle spielt. In der aktuellen Beta werden Erweiterungen bereits <a href="http://blog.mecheye.net/2011/08/shell-extensions-live-enable-disable/">anders aufgebaut</a>, sodass sie nun ohne das Neustarten der Shell aktiviert und deaktiviert werden könnnen. (<a href="http://www.youtube.com/watch?v=luZuhn5_b_8">Demo-Video</a>)
Zum Release von Gnome 3.2 wird es voraussichtlich auch (vorerst inoffiziell) unter <em>extensions.gnome.org</em> eine zentrale Anlaufstelle für die Erweiterungen geben. Schade ist, dass man wegen der Änderungen die Erweiterungen der vorherigen Versionen nicht mehr verwenden kann. Dementsprechend sind zur Zeit natürlich auch noch sehr wenige Extensions für die Beta verfügbar.

<a href="{{site.url}}/wp-content/uploads/extemsions.jpg"><img class="borderimg centered" src="{{site.url}}/wp-content/uploads/extemsions.jpg" alt="" width="340" height="225" /></a>

<div class="imageinfo">Die neue Alt-Tab-Erweiterung fragt jetzt beim ersten Start nach der gewünschten Einstellung.</div>

Fazit
======
Die Beta von Gnome 3.2 läuft stabiler als 3.0, anfängliche Grafikfehler sind endlich verschwunden. Arbeitsspeicher wird bei mir mittlerweile nicht mehr regelmäßig ohne erkennbaren Grund belegt (wenngleich diese Probleme anscheinend noch nicht komplett gelöst sind). Die Beta würde ich natürlich nicht für ein "laufendes System" empfehlen, vor allem da die finale Version in den nächsten Tagen folgen wird. (die bestimmt noch einige Bugfixes erhält)
Gnome 3.2 bringt einige nette Neuerungen, führt aber auch die Ideen &amp; Konzepte von Gnome 3 weiter. Wer also z.B. deutlich mehr Einstellungsmöglichkeiten der <em>Shell</em> erwartet, wird wahrscheinlich enttäuscht werden. Meine Hoffnung bleibt, dass die Erweiterungen diese Lücke füllen können und sich genügend Entwickler finden, die diese auch aktuell halten.
