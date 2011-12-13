---
layout: post
title: ! '[Firefox 4] Tipp: Mehr Platz & Übersicht mit versteckten Toolbars'
wordpress_id: 1148
wordpress_url: http://ganz-sicher.net/blog/?p=1148
date: 2011-03-25 00:59:35.000000000 +01:00
category: tutorials-tipps
---
<img class="lefticon" title="firefox_icon" src="{{site.baseurl}}/wp-content/uploads/firefox_icon.png" alt="" width="48" height="48" />
Mozilla holt auf! Mit <a href="http://www.mozilla-europe.org/de/">Firefox 4</a> bin ich bis auf Kleinigkeiten (Flackern bei Flashobjekten, einige fehlende <a href="http://www.google.com/chrome?hl=de">Chrome</a>-Komforfunktionen) sehr zufrieden, vor allem in Sachen Geschwindigkeit legt der Browser im Vergleich zu Vorgängerversionen deutlich zu. Besonders der Seitenaufbau ist sehr zügig, häufig auch schneller als bei Googles Chrome.
<!--more-->

Außerdem hat es beim neuen Firefox einige strukturelle Änderungen gegeben. So können Icons von Erweiterungen beispielsweise jetzt immer in der Addon-Leiste am unteren Rand des Browsers abgelegt werden. Um (ähnlich wie bei Chrome) möglichst keinen Platz der eigentlichen Website zu "verschenken", habe ich zusätzlich Firefox so angepasst, dass die Lesezeichenleiste (bei mir voll mit Icons diverser Websites) und die Addon-Bar automatisch ausgeblendet werden, wenn sie gerade nicht benutzt werden.

Da Firefox selbst für die Benutzeroberfläche auch (bestimmte) CSS-Einstellungen verwendet, ist es mittels Addons wie <a href="https://addons.mozilla.org/de/firefox/addon/stylish/">Stylish</a>, welche den CSS-Code verändern, möglich dieses Verhalten und Aussehen recht individuell anzupassen. Auf <a href="http://userstyles.org/">Userstyles.org </a>habe ich bereits fertige Codes gefunden, die wenige Wünsche offen lassen:
<em>Aufgeräumter Feuerfuchs:</em>

<img class="borderimg centered" title="firefox_4" src="{{site.baseurl}}/wp-content/uploads/firefox_4.png" alt="" width="600" height="375" />

Code 1: Addonbar verkleinern und evtl. automatisch ausblenden
==============================================================
Nach aktivieren der oben bereits erwähnten Erweiterung <a href="https://addons.mozilla.org/de/firefox/addon/stylish/">Stylish</a> kann der Code für <a href="http://userstyles.org/styles/39555/addonbar-minimizer">Addonbar Minimizer</a> (siehe Screenshot rechts unten) in 2 verschiedenen Ausführungen gewählt und einfach per Mausklick installiert werden. Ich habe hier die Version ohne automatisches Ausbelden der Toolbar gewählt, da dies beim Bedienen der Addon-Kontextmenüs manchmal auch hinderlich sein kann. Wie man auf dem obigen Screen sieht, lohnt sich auch so das Verwenden des Codes, denn links gewinnt man einiges an zusätzlichem Platz. Gerade auf kleineren Geräten wie Netbooks ist das schon von Vorteil.

Code 2: Bookmarkbar automatisch ein/ausblenden
===============================================
Meine Lesezeichenleiste besteht nur aus Icons (Lesezeichen mit leerem Namen) um einige häufig genutzen Seiten schnell ansurfen zu können. Mit "<a href="http://userstyles.org/styles/41338/firefox-4-autohide-bookmarks-toolbar-timed-delayed">Autohide Bookmarks Toolbar Timed Delayed</a>" lässt sich auch die Lesezeichenleiste bei Bedarf aus- bzw. wieder einblenden. Die dort festgelegte Zeit, die bis zum Ausblenden der Leiste gewartet wird, halte ich mit 30 Sekunden für zu lange, ich benutze deswegen eine leicht angepasste Version mit 3 Sekunden Einblendezeit:

	@namespace url(http://www.mozilla.org/keymaster/gatekeeper/there.is.only.xul);

	#PersonalToolbar {
		visibility: collapse !important;
		opacity: 0.5;
		-moz-transition: visibility 2s, opacity 30s ease !important;
	   }

	#navigator-toolbox:hover &gt; #PersonalToolbar {
		visibility: visible !important;
		opacity: 1;
		-moz-transition: visibility !important;
	   }

Code 3: Dropdownmenü der Adressleiste anpassen
===============================================
Dass bei Firefox die Hintergrundfarbe des Adressleisten-Dropdownmenüs immer vom aktuellen Gnome-Style abhängt halte ich für nicht besonders hilfreich. Bei dunklen Themes kann man diesen Bereich häufig schlecht lesen. Auf Basis von <a href="http://userstyles.org/styles/13324/awesomebar-popup-green-italic">AwesomeBar Popup</a> habe ich dies etwas angepasst:

Mein Ergebnis:

<img class="borderimg centered" title="firefox_4_screen" src="{{site.baseurl}}/wp-content/uploads/firefox_4_screen.png" alt="" width="550" height="440" />

Code:
-----

	@namespace url(http://www.mozilla.org/keymaster/gatekeeper/there.is.only.xul);

	.ac-comment
		{font-size: 120%! important;}

	.ac-url-text
		{color: green !important;
		 font-size: 105% ! important;
		 font-style: italic !important;}

	richlistitem.autocomplete-richlistitem{
	background-color: white !important;
	color: black !important;
	}

	richlistitem.autocomplete-richlistitem[selected="true"]{
	background-color: #ccc !important;
	}
