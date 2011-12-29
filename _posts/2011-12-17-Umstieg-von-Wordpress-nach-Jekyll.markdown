---
layout: post
title: Umstieg von Wordpress nach Jekyll
date: 2011-12-17
category: blognews
---
Mein Blog hat sich in den letzten Tagen ziemlich verändert. Der Grund dafür ist, dass ich [Wordpress](http://wpde.org/) verlasse und hier in Zukunft auf ein neues Tool mit dem schönen Namen [jekyll](http://jekyllrb.com/) setzen werde! :) Dieser Artikel fasst meine Beweggründe und Erfahrungen bisher zusammen.
<!--more-->

Was ist Jekyll?
===============
Oh richtig, das hatte ich ja noch gar nicht gesagt. Jekyll ist ein in Ruby geschriebener Postgenerator von Tom Preston-Werner (github.com cofounder):
> Jekyll is a simple, blog aware, static site generator. It takes a template directory (representing the raw form of a website), runs it through Textile or Markdown and Liquid converters, and spits out a complete, static website suitable for serving with Apache or your favorite web server.
Wie schon geschrieben ist es ein *Postgenerator* und kein Blogging-Framework, der direkte Vergleich mit Wordpress wäre also eher unfair. Jekyll will kein CMS mit komplettem Admin Control Panel und anderweitigen Komfortfunktionen sein, denn es ist ein schlankes Kommandozeilen-Tool, das aus den vorliegenden Artikel- und Layout-Dateien statische HTML-Webseiten generiert. Das mag nun Einsteiger wahrscheinlich abschrecken, für mich ist es aber genau richtig. Da Jekyll nur normale HTML-Dateien erzeugt, läuft es beinahe auf jedem beliebigen Webserver und benötigt auch keine Datenbank, die im Hintergrund die ständig gleichen Beiträge ausließt!

Meine Motivation zum Umstieg
============================
Vor einiger Zeit hatte ich bereits zusammen mit einem [Freund](http://ganz-sicher.net/chlange/) überlegt, ein statisches Blogsystem zu programmieren. Wie das bei großen neuen Projekten und wenig freier Zeit so ist, blieb das jedoch zunächst nur bei Planungsphase. ;) Bei meiner github-Suche nach ähnlichen Projekten stieß ich schnell auf jekyll. 
Andererseits empfand ich das Bloggen unter Wordpress oftmals als zu aufwändig. Wordpress ist super, wenn man schnell eine Blog aufsetzen will: Es ist sehr Anpassbar durch die vielen Erweiterungen und Themes, aber dennoch hat es Macken. Der eigentliche Erstellungsprozess für neue Artikel war mir oft zu aufwändig. Beispielsweise generiert der Wordpress-Editor viel unsinnigen HTML-Code, kam nicht immer gut mit eingefügten Codeschnipseln oder Absatzabständen zurecht. Viele kleine Dinge haben mich gestört. Die vielen Erweiterungen führen eben auch dazu, dass man sich einen Blog eher "zusammen-klickt", als ihn komplett von Grund auf selbst an eigene Bedürfnisse anzupassen. Manche Plugins entwickeln dann mitunter ein Eigenleben und geben dann Anlass zu einer nervtötenden Fehlersuche...
Was bisher bei mir auf dem Rechner mit [Archlinux als Betriebssystem](http://ganz-sicher.net/blog/linux-distributionen/weshalb-archlinux-die-distribution-meiner-wahl-ist/) galt, gilt nun auch hier im Blog: 
KISS (Keep it simple, stupid) - und den Rest selbst machen!

Die Vorteile von Jekyll
=======================
Vorteile für mich im Vergleich zu Wordpress:
* Keep It Simple: in Zukunft mehr Fokus auf den Inhalt, *Content is King*
* mehr Spaß am Schreiben: übersichtliches und unkompliziertes Schreiben mit [Markdown](http://daringfireball.net/projects/markdown/) auch unter (Arch)linux ohne extra Software
* alternativ zu Markdown kann übrigens auch [Textile](http://bradchoate.com/mt/docs/mtmanual_textile2.html) als Auszeichnungssprache verwendet werden.
* statische Blogbeiträge: keine Datenbank mehr nötig - bei einem "Ein-Mann-Blog" braucht man ja auch keine
* neues Layout mit (bald) validem HTML5-Code
* ich kann "mal was neues" ausprobieren - jekyll ist in Ruby geschrieben & das wollte ich mir sowieso schon länger ansehen. Nun kann ich das tun, indem ich [Plugins](https://github.com/mojombo/jekyll/wiki/Plugins) für dieses Blog schreibe!
* Synchronisierung über Github, d.h ich habe immer eine funktionierende Version lokal auf dem Rechner die ich auch mit normalen Linuxbefehlen leicht durchsuchen oder anpassen kann

<a href="{{site.url}}/images/blog/sublime_screen_jekyll_wordpress.jpg"><img class="borderimg centered" src="{{site.url}}/images/blog/sublime_screen_jekyll_wordpress.jpg" alt="" width="450" height="370" /></a>
<div class="imageinfo">(Leicht optimierter) Markdown-Artikel vs. importierter Wordpress-Artikel</div>


Erfahrungen & Hürden beim Umstieg
=================================
Import
-------
Das Importieren alter Wordpress-Artikel ist sehr gut [im Wiki beschrieben](https://github.com/mojombo/jekyll/wiki/blog-migrations) und funktionierte soweit auch gut. Leider hat der WYSIWYG-Editor von Wordpress häufig unnötigen HTML-Code erzeugt, also Dinge wie:

	<p style="text-align: justify;"></p>

Da das sehr unterschiedliche Dinge waren, musste ich die Posts nachträglich also doch noch von Hand bearbeiten. Teilweise hat mir dabei [Markdownify](http://milianw.de/projects/markdownify/demo.php) geholfen, das HTML-Text in Markdown-Markup umwandelt.

"Baseurl"-Probleme
------------------
Mein Blog liegt nicht im Hauptverzeichnis des Webservers sondern im Unterordner /blog/. Wenn das der Fall ist, muss das bei jekyll konkret angegeben werden, daher verwende ich in meiner jekyll Konfigurationsdatei (_config.yml) die Einstellung 
> baseurl: /blog 
>
> url: http://ganz-sicher.net/blog
Bei allen Adressen (z.B. beim href-Attribut von Links) muss zusätzlich ein <code>&#123;&#123;site.baseurl&#125;&#125;</code> vorangestellt werden. Bei Bilder in Artikeln verwende ich die direkte Adresse (also mit vorangestelltem <code>&#123;&#123;site.url&#125;&#125;</code>, damit diese auch mit dem RSS-Feed ([Feedburner](http://feeds.feedburner.com/GanzSicherNet), [siehe auch](http://www.slightlytallerthanaverageman.com/2010/02/22/jekyll-feedburner-and-global-urls/)) funktionieren. Diese Einstellungen hatte ich beim Ersten durchgehen der Artikel nicht bedacht. Glücklicherweise kann man bekannte Linuxtools verwenden um die Dateien zu verändern, also konnte ich das auch nachträglich lösen per:

	cd _posts
	sed -i 's/="\/wp-content/="{{site.url}}\/wp-content/g' *
	
Sehr zu Hilfe kommt mir auch die verbesserte Tab Completion bei [zsh](https://wiki.archlinux.org/index.php/Zsh) (ich benutze die alternative Shell zusammen mit [oh-my-zsh](https://github.com/robbyrussell/oh-my-zsh)), denn nun kann ich im \_posts-Ordner einfach einen beliebigen Begriff aus dem Beitragstitel eingeben und die Tabtaste drücken und kann so sehr schnell die gesuchte Datei finden und bearbeiten.

Kommentare nun mit disqus
-------------------------
Der Kommentarbereich ist im Idealfall nicht statisch, sondern ändert sich laufend. Deshalb verwende ich den Service [Disqus](http://disqus.com/). Die Kommentare lassen sich - sofern sich die Adressen der Artikel nicht ändern - leicht von Wordpress zu Disqus importieren und dann später auch mit jekyll anzeigen. Bei deutschen Sonderzeichen (Umlaute, ß) hat disqus bei mir teilweise Darstellungsprobleme, die aber wohl durch den Import kommen und nicht an Disqus selbst liegen.

HTML-Generierung bei Jekyll
----------------------------
Jekyll erzeugt aus den Dateien und Ordnern (ausgeschlossen sind Ordner mit vorangestelltem Unterstrich) statische HTML-Dateien, für Templates können [liquid filter](https://github.com/mojombo/jekyll/wiki/Liquid-Extensions) benutzt werden, damit die Quelldateien übersichtlich bleiben. Ein Manko hat Jekyll aber doch: Es gibt keine Möglichkeit zur Inkrementellen Generierung. Auch wenn beispielsweise nur ein neuer Beitrag erstellt wurde, wird das gesamte Projekt neu generiert. Bei kleineren Blog (wie bei mir) fällt das nicht so sehr in's Gewicht, die Erstellung dauert nur wenige Sekunden. Bei größeren Seiten könnte das aber ein echtes Problem werden. Glücklicherweise liegt Jekyll in OpenSource-Form auf github und dementsprechend gibt es auch Forks anderer Nutzer, die sich darum [bereits gekümmert haben](https://github.com/graysky/jekyll/commit/39ae8c7c3f4a3cffd095e3b7638cfa8025c5a67a).

Beitragsauszug wie bei Wordpress
--------------------------------
Bei Wordpress wurden Einleitung und Artikel durch die Kennzeichnung <code>&lt;!--more--&gt;</code> voneinander getrennt. Das Funktioniert natürlich standardmäßig bei Jekyll nicht mehr, daher habe ich mir ein [Mini-Plugin](https://github.com/pylight/gsn/blob/master/_plugins/postmorefilter.rb) geschrieben, das diese Trennung vornimmt. Mittels <code>&#123;&#123; post.content | postmorefilter &#125;&#125;</code> kann man nun auf die Einleitung eines Artikels in der index.html zugreifen.

Artikelerstellung & Posts auf github
=====================================
Natürlich habe ich auch ein kleines [Python Script](https://github.com/pylight/gsn/blob/master/_scripts/newpost.py) geschrieben, um auf einheitlich Weise neue Beiträge erstellen zu können. Zusätzlich verwende ich nun [git](http://git-scm.com/) als Versionsverwaltung für meinen Blog und synchronisiere dies mit [github.com](https://github.com/):
> [https://github.com/pylight/gsn](https://github.com/pylight/gsn)
Jedem interessierten steht es selbstverständlich frei, dieses Projekt zu forken und nach den eigenen Wünschen anzupassen. (Hinweise zur [Lizenz]({{site.url}}/licence.html))

Bilder aus Artikeln befinden sich natürlich nicht im Repository und liegen nur auf dem eigenen Server, ich überlege derzeit noch, eventuell einen anderen Dienst dafür zu benutzen, damit die Bilder nicht immer gesondert hoch geladen werden müssen.

Noch einige ToDos
==================
Natürlich gibt es auch noch einige Dinge, die ich noch verbessern möchte, z.B:
* das Syntax Highlighting bei Codeblöcken funktioniert noch nicht mit [pypgments](http://pygments.org/) 
* Blog-Suche mit [indextank](https://github.com/PascalW/jekyll_indextank)
* jekyll hat noch etwas Probleme beim Einbetten von Videos, das [emedly plugin](https://github.com/robb/jekyll-embedly-client) sieht interessant aus
* eine verbesserte Archivseite (derzeit nur Textlinks)
* Kategorie-Übersicht und bessere Fehlerseiten
* Für weitere Tipps und Wünsche bin ich offen :)

Zwischenfazit & Links
=====================
Jekyll ist nicht für Jedermann, denn es richtet sich nicht an Einsteiger, sondern eher an die technisch versiertere Fraktion. Wenn man sich aber zu jener zählt und ein wenig Zeit kann & aufbringen will, um das Projekt an eigene Bedürfnisse anzupassen, wird man auf jeden Fall mit einem tollen System belohnt, mit dem sich auch komfortabel Bloggen lässt. Jekyll macht mir jetzt schon mehr Spaß als Wordpress, es fühlt sich mehr wie das eigene und nicht wie ein fremdes System an. ;D Falls der Jekyll-Ansatz Anklang findet, das System dir aber zu Feature-arm erscheint: mit [Octopress](http://octopress.org/) gibt es auch ein Framework, das auf jekyll aufsetzt und ähnliche Funktionen wie Wordpress anbietet.

Artikel, die mir beim Umstieg geholfen haben
--------------------------------------------
* [http://vitobotta.com/how-to-migrate-from-wordpress-to-jekyll/](http://vitobotta.com/how-to-migrate-from-wordpress-to-jekyll/)
* [http://vitobotta.com/migrating-from-wordpress-to-jekyll-part-one-why-I-gave-up-on-wordpress/](http://vitobotta.com/migrating-from-wordpress-to-jekyll-part-one-why-I-gave-up-on-wordpress/)
* [http://paulstamatiou.com/how-to-wordpress-to-jekyll](http://paulstamatiou.com/how-to-wordpress-to-jekyll)

<div class="infobox">
<a href="http://jekyllrb.com/" class="homelink" target="_blank">Jekyll Homepage</a> (<a href="https://github.com/mojombo/jekyll" target="_blank" class="packagelink">auf github</a>) | Weiterführendes: <a href="http://octopress.org/" class="info">Octopress (jekyll Framework)</a>
</div>

Interesse geweckt?
==================
Für Fragen bezüglich Jekyll stehe ich natürlich gerne zur Verfügung. Außerdem freue ich mich über eure Reaktionen: Wie gefällt euch der neue Blog?
