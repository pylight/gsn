---
layout: post
title: (Script) urxvt - In neuem Tab statt neuem Terminal-Fenster öffnen
date: 2013-11-09 22:41
category: linux-distributionen
---
<img src="{{site.url}}/wp-content/uploads/terminal1.png" class="lefticon" alt="" />

OH, ja es lebt noch, dieses Blog! Und da ich ja auch noch da bin, schreibe ich halt mal wieder einen Artikel. :P
Aber ich schweife ab, zurück zum Thema: Wie ich bereits in früheren Blogbeiträgen geschrieben habe setze ich [urxvt](https://wiki.archlinux.org/index.php/rxvt-unicode) (rxvt unicode) als bevorzugten Terminal-Emulator ein. Seine Vorteile sind dessen flotte Geschwindigkeit, viele Konfigurationsmöglichkeiten und Erweiterungen sowie das simple Design ohne unnötigen Schickschnack. 
<!--more-->
Da das Terminal Tabs unterstützt, habe ich bisher dennoch eine Funktion vermisst, für welche ich nun ein kleines Script geschrieben habe: Die Möglichkeit ein neues Terminal per Tastenkombination in einem neuen Tab des aktiven Urxvt-Fensters zu öffnen statt jedes Mal ein komplett neues Fenster zu öffnen.

<img alt="urxvt screenshot" class="borderimg centered" src="{{site.url}}/images/blog/urxvt_screen.jpg" />

<div class="imageinfo">urxvt mit Tabs in Aktion ;)</div>

Das folgende Script erfüllt diesen Zweck und kann in einem Desktop Environment eurer Wahl einem Shortcut zugewiesen werden. Es setzt ein installiertes urxvt samt tabbed-Erweiterung voraus. Außerdem müssen pidof, awk und xdotool installiert sein. Ihr könnt das Script gerne frei verwenden (MIT-Lizenz), die neuste Version findet ihr immer auf [Github](https://github.com/pylight/scripthub/blob/master/bash/runUrxvt.sh).

{% highlight bash %}
#!/bin/bash

# ------------------------------------------------------------------------------------
# Author: Sven Kammerer (admin@ganz-sicher.net)
# Description:    This little scripts checks if an instance of urxvt is running.
#                 If so, it is able to determine the window-id using xdotool 
#                 and append a new tab (urxvt tab extension).
#
#                You can run this script from a keyboard shortcut (e.g. Ctrl+Alt+T)
#                so that only one instance of urxvt will be used.
#
# Usage:        Call the script without arguments. Use -h or --help to see this text.
# ------------------------------------------------------------------------------------

# dependencies:
# pidof, awk, xdotool, (urxvt with perl tab extension) 

# settings
appendToSession=true        # true = append tabs, false = always open a new urxvt instance

# variables
progName="urxvt"
newInstanceCommand="urxvt -pe tabbed"
processId=$(pidof $progName | awk '{print $NF}' | awk '{print $1}')


# print help?
if  [ $# -gt 0 ] ; then
 if [ $1 == "--help" ] || [ $1 == "-h" ] ; then
  awk '/# ----/{++t}t==1' $0
  exit
 fi
fi

if $appendToSession && [ $? -eq 0 ]; then
 # process found. get windowid and create a new tab
 idList=$(xdotool search --pid $processId 2>/dev/null)

 if [ $? -eq 0 ]; then
  # windowid(s) found, use the first one
  windowId=$(echo $idList | awk 'NR == 1' | awk '{print $1}')

  if [ ! -z "$windowId" ] ; then
   xdotool windowfocus $windowId
   xdotool windowraise $windowId
   xdotool keydown shift 
   xdotool key Down 
   xdotool keyup shift
   exit
  fi
 fi
fi

# process not found - start a new instance
$($newInstanceCommand &)

exit
{% endhighlight %}

So wird immer nur eine Instanz von Urxvt geöffnet. Vor dem Benutzen empfiehlt sich, zunächst alle offenen urxvt Fenster mit 'killall urxvt' zu schließen, damit das Script nicht durcheinander kommt. 
Viel Spaß mit dem Script. Über Verbesserungsvorschläge freue ich mich natürlich immer! :)
