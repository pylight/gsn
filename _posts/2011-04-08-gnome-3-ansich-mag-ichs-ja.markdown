---
layout: post
title: Gnome 3 - ansich mag ich's ja!
wordpress_id: 1168
wordpress_url: http://ganz-sicher.net/blog/?p=1168
date: 2011-04-08 21:42:39.000000000 +02:00
category: linux-distributionen
---
<img class="lefticon" title="gnome_icon" src="{{site.url}}/wp-content/uploads/gnome_icon.png" alt="" width="48" height="48" />
Nachdem Gnome 3 vor 2 Tagen nach längerer Entwicklungszeit endlich released wurde, habe ich auch mal erste Gehversuche mit der neuen Desktopumgebung (<a href="http://www.archlinux.org/news/gnome3-in-testing/">unter Archlinux</a>) gemacht. Seitdem ich zu Linux gewechselt bin, war Gnome immer die Desktopumgebung meiner Wahl: Es hat mich i.d.R. nicht unnötig behindert, sonder war "einfach nur da" und hat die nötigsten Funktionen zur Verfügung gestellt. Mit Gnome 3 haben die Entwickler jetzt einen mutigen Schritt gewagt und wollen einiges anders machen.

<!--more-->
Vorgedanken
============
Im Vorfeld habe ich einige Reaktionen zu Gnome 3 gelesen, die meisten davon vielen negativ aus. Von "die brauchen dringend anständige Designer" bis hin zu "ich werde nie wieder Gnome verwenden &amp; wechsle zu <a href="http://www.xfce.org/">Xfce</a>!" war alles dabei. Ich mag naiv sein, aber ich sehe eher die großen Vorteile: Gnome 3 spricht mich vom Design her an, denn es sieht zwar (anders als z.B. KDE 4) moderner aus, nutzt aber nicht zu viele unnötige Effekte wie gläserne/transparente Fenster usw..
Sicher wird es auch genügend Leute geben, die weiterhin den Standarddesktop (ohne gnome-shell) nutzen wollen. Da es sich hier aber um freie Software handelt, denke ich, dass auch das in der Zukunft nicht "aussterben" wird.
<h3>Was ist überhaupt neu?</h3>
Hauptänderung ist <a href="https://live.gnome.org/GnomeShell">gnome-shell</a>. Aktive Fenster und Desktop werden jetzt auf einer Art Übersichtsseite zusammengefasst, zu der man per Windows-/Super-Taste wechseln kann. Außerdem werden Benachrichtigungen jetzt am unteren Rand des Bildschirms angezeigt und zusammengefasst, um möglichst nicht den Arbeitsfluss zu stören. Der folgende Clip fasst die Features gut zusammen:

<object style="height: 390px; width: 640px;"><param name="movie" value="http://www.youtube.com/v/SSGfS6K7pI0?version=3" /><param name="allowFullScreen" value="true" /><param name="allowScriptAccess" value="always" /><embed type="application/x-shockwave-flash" width="640" height="390" src="http://www.youtube.com/v/SSGfS6K7pI0?version=3" allowfullscreen="true" allowscriptaccess="always"></embed></object>

Wo kann ich das umstellen??
============================
Gerade weil bei Gnome 3 viele Neuheiten dazu gekommen sind, stellt sich nach kurzem Testen der neuen Features schnell die Frage: "Kann man da noch was Konfigurieren?".  Leider bleibt Gnome da dem Prinzip "Weniger ist einfacher" treu und beschränkt sich wirklich nur auf die nötigsten Einstellungen (die sich hinter dem Menü oben rechts verstecken). Die (wie ich finde zu große) <strong>Standardtextgröße</strong> bei Fenstern lässt sich so zum Beispiel verkleinern, ein paar weitere Einstellungsmöglichkeiten hätten insgesamt aber sicher nicht geschadet. Natürlich kann man Linux-typisch per Terminal und dem <strong>gconf-editor</strong> beliebige Änderungen vornehmen, eine umfangreiche grafische Konfigurationsmöglichkeit wäre dennoch schön gewesen. Einen Anfang, um diese Lücke zu schließen, wurde mit dem <a href="https://live.gnome.org/GnomeTweakTool">Gnome Tweak Tool</a> gemacht.


<a href="{{site.url}}/wp-content/uploads/gnome_screen1.jpg"><img class="borderimg centered" title="gnome_screen1" src="{{site.url}}/wp-content/uploads/gnome_screen1.jpg" alt="" width="500" height="250" /></a>
<a href="{{site.url}}/wp-content/uploads/gnome_screen2.jpg"> <img class="borderimg centered" title="gnome_screen2" src="{{site.url}}/wp-content/uploads/gnome_screen2.jpg" alt="" width="500" height="250" /></a>

Einiges nervt noch...
======================
Die Sache mit den dynamisch erstellten/entfernten Desktops ist für  mich noch *sehr* gewöhnungsbedürftig. Auch wenn die Idee grundsätzlich  gut ist, wünsche ich mir oft, einfach wieder nur 4 ständige Desktops zu  haben, wie bei Gnome 2. Schließt man z.B. das alle Fenster auf dem  letzten Desktop, wird dieser entfernt und man wird wieder auf die  (dunkle) Übersichtsseite geworfen.
Einstellungsfenster (z.B. bei Gnome-do) erscheinen teilweise gar  nicht! Hängt warscheinlich damit zusammen, dass die Einstellungsfenster  jetzt meist an das Hauptfenster "gepinnt" werden und sich nicht mehr  individuell verschieben lassen. Eine "Feature", das es meiner Meinung  nach sowieso nicht gebraucht hätte...
Ein paar kleinere Bugs sind mit noch aufgefallen. Teilweise wird der Bildschirm bei mir z.B. kurzzeitig schwarz. Schade ist auch, dass die unter Gnome 2 festgelegten Tastenkombinationen nicht direkt funktionieren oder sich die Shortcuts teilweise geändert haben (z.B. Alt+F7 statt gedrückter Alt-Taste zum Verschieben von Fenstern oder Strg+Del statt Del zum Löschen von Dateien).

Einige Probleme lassen sich lösen...
======================================
Natürlich muss man sich bei so vielen Änderungen an vieles erst gewöhnen, einige Dinge habe ich auch schon angepasst, weil sie mir nicht gefiehlen:
Das oben angesprochene <strong>Gnome Tweak Tool</strong> beinhaltet einige nützliche Zusatz-Einstellungen. So können z.B. wieder die <strong>Icons auf dem Desktop</strong> aktiviert und angezeigt werden.

**VLC** hat bei mir (Archlinux) Probleme gemacht, der Ton war sehr verzerrt. Liegt warscheinlich daran, dass Gnome 3 pulseaudio benutzt und ich vorher alsa eingesetzt habe. Eine Neuinstallation (pacman -Sf vlc) hat weitergeholfen...

Gnome 3 verzichtet auf **Minimieren- und Maximieren-Buttons**. Das macht mir soweit nichts aus, denn mit Doppelklick auf die Fensterleiste, funktioniert das Maximieren und mit mittlerer Maustaste das Verschieben des Fensters in den Hintergund. Dass auch die <strong>Taskleiste</strong> komplett fehlt, war mir dann aber doch zu viel. Ich verwende deswegen <a href="http://code.google.com/p/tint2/">tint2</a>, das mir alle Tasks auf allen Desktops anzeigt und das Fenstermanagement vereinfacht. Meine Config-Datei <a href="http://www.ganz-sicher.net/sonstiges/configs/tint2rc">befindet sich hier</a> (Speicherort: ~/.config/tint2rc, siehe auch Screenshots oben). Wer ein Dock mit etwas mehr Effekten haben möchte, kann sich mal <a href="http://www.glx-dock.org/">Cairo Dock</a> anschauen.

Der <strong>Schnellstarter</strong> (Tastenkombination Alt + F2) ist leider nicht so umfangreich wie bei Gnome 2 und die Vervollständigung der Befehle erfolgt erst nach Drücken der Tab-Taste. Ich verwende deswegen <a href="http://mhr3.blogspot.com/2010/11/introducing-synapse-acetylcholine.html">Synapse</a> als alternativen Programmstarter.

Einige Shell-Erweiterungen gibt es bereits unter dem Namen <a href="https://live.gnome.org/GnomeShell/Extensions">gnome-shell-extensions</a> (im AUR unter <a href="http://aur.archlinux.org/packages.php?ID=47501">gnome-shell-extensions-git</a> zu finden), einen kurzen Überblick über die Funktionen der Erweiterung gibt es z.B. bei <a href="http://www.webupd8.org/2011/04/gnome-shell-extensions-additional.html">Webupd8</a>. Ich musste bei nach der Installation allerdings einige Pugins wieder (aus /usr/share/gnome-shell/extensions) löschen, weil Gnome sonst nicht mehr starten wollte. :/

Kurzes Fazit
=============
Nach 2 Tagen des kurzen Testens, habe ich mich entschieden, dass Gnome 3 bei mir so stabil läuft, dass ich es auch weiterhin als Standard-Desktop benutzen werde. Nicht alles funktioniert zu 100%, manches stört, aber ich bin mir sicher, dass die Gnome-Entwicker da noch einiges nachliefern werden und dies erst der Anfang (und nicht schon das teilweise beschworene Ende) ist. Auch bin ich mal positiv optimistisch, dass die Community einiges dazu beitragen wird, dass Gnome 3 besser wird. Das Gnome Tweak-Tool für die weiteren Einstellungen und erste Themes wie <a href="http://half-left.deviantart.com/art/GNOME-Shell-Elementary-Git-193232931">Gnome-Shell Elementary</a> machen auf jeden Fall Hunger auf mehr. ;-) Schön dass sich da einges bei Gnome tut! Ich bin gespannt <a href="http://www.omgubuntu.co.uk/2011/04/zeitgeist-work-towards-gnome-3-2/">was da in Zukunft</a> alles noch kommt...

Was haltet ihr von Gnome 3? :)
