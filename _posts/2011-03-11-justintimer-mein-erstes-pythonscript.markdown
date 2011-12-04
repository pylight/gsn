---
layout: post
title: justInTimer - Mein erstes Pythonscript...
wordpress_id: 1051
wordpress_url: http://ganz-sicher.net/blog/?p=1051
date: 2011-03-11 15:37:55.000000000 +01:00
---
<a href="http://ganz-sicher.net/blog/wp-content/uploads/python_code.png"><img class="alignleft size-full wp-image-1052" title="python_code" src="http://ganz-sicher.net/blog/wp-content/uploads/python_code.png" alt="" width="48" height="48" /></a>Viel Gutes habe ich über die Scriptsprache Python gehört, beispielsweise dass es aufgrund des Aufbaus schwer ist,  damit überhaupt unübersichtlichen (und damit schwer wartbaren) Code zu erzeugen. Deswegen wollte ich mir die Sprache schon seit geraumer Zeit unbedingt mal ansehen. Den ersten Schritt habe ich heute gemacht, indem ich mein erstes kleines Script mit Python geschrieben habe.

<!--more-->
<h3>Erste Schritte</h3>
Unter vielen Linuxdistributionen hat man ja den Vorteil, dass Python bereits standardmäßig mitgeliefert wird und man somit gleich loslegen kann (Aufruf über das Terminal mit <em><span style="font-family: 'andale mono', times;">python Scriptname</span></em>). Ich verwende das aktuelle Debian Squeeze, als Editor habe ich <a href="http://www.geany.org/">Geany</a> verwendet. (auch für andere Programmiersprachen einen Blick wert; in den Packetquellen verfügbar)
Eine Sache, die die Übersicht fördert, ist mir gleich zu Beginn aufgefallen: Python verzichtet zwar auf Semikolons nach Befehlen sowie auf geschweifte Klammern (was man vielleicht aus Programmiersprachen wie C++ oder php vielleicht kennt), allerdings sind Einrückungen bei Kontrollstrukturen wie if-Abfragen Pflicht.
<h3>Getting Started</h3>
Da das eigenständige erlernen einer Programiersprache auch immer eine Motivationsfrage ist, lerne ich selbst immer am effektivsten, wenn ich ein sichtbares Ziel in Form einer (einfachen) Aufgabe / eines Scripts vor mir habe. Ich habe mich dabei nicht lange mit Tutorials oder Einführungstexten aufgehalten, sondern einfach mal drauflosgecodet. Sollte ich dabei also heilige Gesetze von Python gebrochen oder anderweitige Fehler gemacht haben, bin ich also über jeden Hinweis dankbar. ;-) Als Hilfen beim Schriben habe ich hauptsächlich die folgenden Quellen verwendet:
<ul>
	<li><a href="http://openbook.galileocomputing.de/python/">Galileo Openbook über Python</a></li>
	<li><a href="http://www.python.org/doc/">offizielle Python Dokumentation &amp; Tutorials</a></li>
	<li><a href="http://www.python-forum.de/">deutsches Pythonforum</a></li>
	<li><a href="http://wiki.python.de/">deutsches Pythonwiki</a></li>
	<li><a href="http://www.thomas-guettler.de/vortraege/python/einfuehrung.html">kurze dt. Pythoneinführung mit weiteren Linktipps</a></li>
</ul>
<h3>Mein erstes Script in Python</h3>
<strong>justInTimer</strong>, mein erste Script erfüllt einen Zweck, der schnell erklärt ist: Das Script soll mir am Abend dabei helfen, rechtzeitig den PC auszuschalten, damit ich am nächsten Tag nicht zu müde bin, weil es im Netz noch so viele interessante Dinge zu sehen gab. ;D Dementsprechend verschwindet das Script nach dem Aufruf (und der Frage nach der verbleibenden Dauer) wieder aus dem Terminal &amp; die Möglichkeit die Funktion vorzeitig abzubrechen wurde bewusst nicht implementiert. Da das <strong>Script für Gnome</strong> gedacht ist, werden 10, 5, und eine Minute vor ablauf der Zeit entsprechende Gnome-Notifications angezeigt.

<code lang="python">#!/usr/bin/env python
# -*- coding: utf-8 -*-
#       Simple shutdown timer-script for gnome to actually shut the computer down sometimes ;p
#       by Sven (admin@ganz-sicher.net)
#	Last Update: 11.03.2011
#
#       Dependencies: gnome, notify-send (libnotify-bin), sudo 
#       Installation: move script to /usr/bin/ and make sure it's executable
#
#       Usages: sudo python justInTimer
#               sudo python justInTimer <minutes>
def main():

        # Modules
        import time
        import subprocess
        import sys

        # Functions

        # differend actions depending on left time (status messages and shutdown)
        def inf(i):
                # Gnome Status messages (10min, 5min & 1min left)
                if i+11 == mytime:
                        subprocess.Popen("notify-send -i /usr/share/icons/gnome/48x48/status/dialog-warning.png 'NOTICE: PC will be shut down in 10 minutes...'", shell=True)
                elif i+6 == mytime:
                        subprocess.Popen("notify-send -i /usr/share/icons/gnome/48x48/status/dialog-warning.png 'NOTICE: PC will be shut down in 5 minutes.'", shell=True)
                elif i+2 == mytime:
                        subprocess.Popen("notify-send -i /usr/share/icons/gnome/48x48/status/user-idle.png 'Warning: Shutting down in 1 minute!'", shell=True)
                # Shutdown when time is over
                elif i+1 == mytime:
                        subprocess.Popen("shutdown -h now", shell=True)

        # script called with (valid) argument?
        try:
                mytime = int(sys.argv[1])
        except:
                # Ask User for duration
                mytime = raw_input("Please enter the minutes you want to have until shutdown: ")
                try:
                        mytime = int(mytime)
                except:
                        print "Unzulaessige Eingabe, bitte Zahl eingeben!"
                        exit(1)
                print 'Okay, shutting down in ',mytime ,' minutes.'
                raw_input('Please confirm this duration with ENTER... ')
                subprocess.Popen(["python","/usr/bin/justInTimer",str(mytime)], shell=False)
                exit(0)

        # count the time and check for actions every minute (inf()-function)
        for i in xrange(mytime):
                time.sleep(60)
                inf(i)
        return 0

if __name__ == '__main__':
        main()
</code>

Die <a href="http://www.ganz-sicher.net/scripts/myscripts/justInTimer">gesamte Datei gibt's auch hier</a> zum direkten Herunterladen. Vielleicht kann ja jemand etwas damit anfangen, über sonstige Anregungen freue ich micht natürlich wie gesagt auch immer. =)

Falls jemand z.B. einen guten <strong>Buchtipp</strong> zu Python haben sollte, wäre ich auch sehr dankbar wenn er das nicht verschweigen würde. :)
