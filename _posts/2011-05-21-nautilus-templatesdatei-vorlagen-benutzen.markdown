---
layout: post
title: Nautilus - Templates/Datei-Vorlagen benutzen
wordpress_id: 1306
wordpress_url: http://ganz-sicher.net/blog/ubuntu/nautilus-templatesdatei-vorlagen-benutzen/
date: 2011-05-21 23:30:58.000000000 +02:00
category: linux-distributionen
---
<img class="lefticon" src="{{site.url}}/wp-content/uploads/nautilus.png" alt="" width="48" height="48" />

Eine Funktion, die ich bisher gar nicht weiter beachtet hatte, die mir beim Dateimanager Nautilus (Standard-Manager unter Ubuntu und Gnome) aber sehr gut gefällt, ist die Möglichkeit, auf einfache Weise Dateivorlagen anzulegen, die dann im Kontextmenü (Rechtsklick) beim Erstellen neuer Dateien ausgewählt werden können. Vor allem wenn man regelmäßig Scripts oder Programme in verschiedenen Programmiersprachen erstellt, spart man mit dieser Funktion auf jeden Fall einiges an Zeit.
<!--more-->

Neue (Datei-)Templates anlegen
==============================
Vorlagen werden angelegt, indem im Homeverzeichnis unter dem Ordner Templates neue Dateien erstellen werden.
Die dort erstellen Vorlagen sind fortan über das Kontextmenü erreichbar:

<img class="borderimg centered" src="{{site.url}}/wp-content/uploads/Templates-verwenden.jpeg" alt="" />

Wie man sieht, wird der Dateiname im Kontexmenü angezeigt. Der Dateiinhalt wird beim Anlegen neuer Dateien aus dem Templates-Verzeichnis kopiert. Besonders praktisch ist dies bei Scripts (z.B. Bashscripts), denn wenn die nötigen Ausführungsrechte für die Datei bereits im Templates-Ordner gesetzt wurden, muss dies dann bei den neuen Dateien nicht mehr extra gemacht werden.


Ein paar Template-Beispiele
============================
Ich habe mal einige Dateivorlagen (siehe Screenshot unten) für häufig benötigte Dateitypen erstellt. Die Dateien müssen wie oben beschrieben in das Verzeichnis <strong>~/Templates</strong> entpackt werden.
Das Archiv mit den Templates findet ihr unter [http://www.ganz-sicher.net/files/public/config/Nautilus-Templates.zip](http://www.ganz-sicher.net/files/public/config/Nautilus-Templates.zip).

<img class="borderimg centered" src="{{site.url}}/wp-content/uploads/Screenshot-Templates.png" alt="" width="675" height="525" />
