---
layout: post
title: Produktivität - Duckduckgo als Standardsuche in Chrome
wordpress_id: 1515
wordpress_url: http://ganz-sicher.net/blog/?p=1515
date: 2011-09-02 15:03:42.000000000 +02:00
---
<img style="float: left;" src="http://ganz-sicher.net/blog/wp-content/uploads/logo1.png" alt="" width="100" height="66" />Über die alternative Suchmaschine <a href="http://duckduckgo.com/">Duckduckgo</a> hatte ich bereits <a href="http://ganz-sicher.net/blog/linktipps/3-interessante-suchmaschinen-abseits-von-google/">kurz geschrieben</a>. Die Hauptvorteile gegenüber Google liegen darin, dass mehr Wert auf Privatspäre (keine Suchstatistiken) gelegt wird und man durch kurze Befehle (<a href="http://duckduckgo.com/bang.html">!bang</a>) mit vorangestelltem Ausrufezeichen viele andere Suchdienste ansprechen kann, also beispielsweise auch nicht auf Google verzichten muss. Mitlerweile verwende ich Duckduckgo statt Google als Standardsuche in Chromium. Nach etwas Eingewöhnung komme ich damit deutlich schneller an's Ziel als mit Google!

<!--more-->
<h3>Was interessiert mich Privatsphäre?</h3>
Firmen wie Google oder Facebook erstellen im Hintergrund Userprofile mit dem Surfverhalten der Nutzer. Das wird dann beispielsweise dazu genutzt, passendere Werbung einblenden zu können. Man könnte jetzt meinen, dass personalisierte Suche oder Werbung eine super Sache ist, denn so bekommt man ja nur direkt die Ergebnisse präsentiert, die einen in der Regel interessieren. Achtet man jedoch genauer darauf, was diese Seiten im Hintergrund machen, ist schon erschreckend wie unterschiedlich Suchergebnisse für Ein und den Selben Suchbegriff mitlerweile sein können. Personalisierung mag von der Idee her interessant sein, bei den meisten großen Websites ist aber zu intransparent was gefiltert wird und wie die Algorithmen dafür arbeiten. Als Lesestoff zum Thema kann ich definitiv diesen <a href="http://lifehacker.com/5814100/the-problem-with-your-google-search-results-and-what-you-can-do-about-it">Artikel zum Thema</a>  (und das Video am Anfang!) empfehlen.
<h3>Duckduckgo !bangs</h3>
Eine Besonderheit von Duckduckgo sind die <a href="http://duckduckgo.com/bang.html">!bang-Befehle</a>, mit denen es möglich ist bestimmte Websites direkt durch die Suche anzu sprechen. Ist man sich sicher, dass das erste Ergebnis der Suche bereits das passende ist, kann man durch ein einfaches <strong>!</strong> neben dem Suchbegriff beispielsweise die "I'm feeling ducky"-Suche (funktioniert wie "I'm feeling lucky" bei Google) verwenden ohne extra die Suchergebnisseite aufrufen zu müssen:

<a href="http://ganz-sicher.net/blog/wp-content/uploads/ducky.jpg"><img src="http://ganz-sicher.net/blog/wp-content/uploads/ducky.jpg" alt="" width="350" height="320" /></a>

Kennt man die wichtigesten !bang-Befehle, so lässt sich mit der Duckduckgo-Suche sehr komfortabel auf anderen Seiten Suche, z.B. Google mit <strong>!g</strong>:

<a href="http://ganz-sicher.net/blog/wp-content/uploads/google_search.jpeg"><img src="http://ganz-sicher.net/blog/wp-content/uploads/google_search.jpeg" alt="" width="350" height="320" /></a>

<strong>Hier einige Beispiele für weitere Befehle, ich nützlich finde:</strong>
<ul>
	<li><strong>linux server !a</strong> - <a href="http://www.amazon.de/">Amazon</a>-Suche</li>
	<li><strong>brandenburger tor !i</strong> - <a href="http://images.google.com/">Google Bildsuche</a></li>
	<li><strong>amazon bestellung !gmail </strong>- <a href="https://mail.google.com/">Google-Mail</a>-Suche</li>
	<li><strong>x^2+3 !wolfram</strong> - Suche mit <a href="http://www.wolframalpha.com/">WolframAlpha</a></li>
	<li><strong>windows 8 !wde</strong> - <a href="http://de.wikipedia.org/wiki/Wikipedia:Hauptseite">Wikipedia Deutschland</a></li>
	<li><strong>halloween documents !w</strong> - <a href="http://en.wikipedia.org/wiki/Main_Page">Englische Wikipedia</a></li>
	<li><strong>subprocess !py3k</strong> - <a href="http://docs.python.org/">Python 3 Dokumentation</a>, DDG eignet sich auch gut für andere Sprachen/Dokus</li>
	<li><strong>sophisticated !leo</strong> - <a href="http://dict.leo.org/">Leo</a> Wörterbuch</li>
	<li><strong>ubuntu !gr</strong> - die RSS-Feeds in <a href="http://www.google.com/reader">Google Reader</a> nach 'ubuntu' durchsuchen</li>
	<li><strong>!bang</strong> - <a href="http://duckduckgo.com/bang.html">komplette Übersicht der Befehle</a></li>
</ul>
Natürlich lassen sich auch jeweils die Hauptseiten so sehr schnell aufrufen, indem man nur den jeweiligen Kurzbefehl eingibt. Damit DDG nicht auf englisch Sucht, empfiehlt es sich einige Einstellungen vom dem Suchen festzulegen. (siehe nächster Abschnitt)
<h3>Suche von der Chrome-Adressleiste aus einrichten</h3>
Auf der <a href="http://duckduckgo.com/">Duckduckgo-Website</a> gibt es unter der Suchleiste einen Link "Add to Chrome", der erklärt, wie man die Suchmaschine zu Chrome hinzufügt und als Standard festlegt. Die Suchadresse in dem Chrome-Einstellungen lautet dann wahrscheinlich so:
<blockquote>http://duckduckgo.com/?q=%s</blockquote>
Dabei handelt es sich um die Suche ohne Einstellungen. Um persönliche Einstellungen für die Suche vorzunehmen müssen noch die Optionen auf <a href="http://duckduckgo.com/settings.html">http://duckduckgo.com/settings.html</a> festgelegt werden. Unten auf dieser Seite unter der Überschrift "<strong>Load/Reset Settings</strong>" erscheint dann eine neue Adresse, beispielsweise
<blockquote>https://duckduckgo.com/?kj=w&amp;kl=de-de&amp;kp=-1</blockquote>
<span style="color: #333333; font-family: 'Segoe UI', Arial, sans-serif; line-height: 17px; background-color: #ffffff;">Um diese neuen Einstellungen auch in Chrome/Chromium zu verwenden, muss der gesamte Text hinter dem Fragezeichen (also z.B. kj=w&amp;kl=de-de&amp;kp=-1) kopiert werden und mit einem <strong>&amp;</strong> an die Suchadresse in den Chrome-Einstellungen angehängt werden. Bei mir lautet das Endergebnis dann:</span>
<blockquote>http://duckduckgo.com/?q=%s&amp;kj=w&amp;kl=de-de&amp;kp=-1</blockquote>
<a href="http://ganz-sicher.net/blog/wp-content/uploads/chrome_settings.jpeg"><img src="http://ganz-sicher.net/blog/wp-content/uploads/chrome_settings.jpeg" alt="" width="450" height="175" /></a>

Fertig! Die <strong>magische Duckduckgo-Suche</strong> in Chrome kann beginnen. :-)
