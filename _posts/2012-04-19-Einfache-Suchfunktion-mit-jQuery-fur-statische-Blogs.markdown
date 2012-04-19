---
layout: post
title: Einfache Suchfunktion mit jQuery für (statische) Blogs
date: 2012-04-19 23:05
category: programmierung-scripting
---
<img src="{{site.url}}/images/blog/old-edit-find.png" class="lefticon" alt="" />
Nachdem ich mit meinem Blog auf [Jekyll](http://jekyllrb.com/) <a href="{{site.url}}/blognews/Umstieg-von-Wordpress-nach-Jekyll/">umgestiegen bin</a>, habe ich zunächst auf eine Suchfunktion verzichtet. Da Jekyll statische HTML-Seiten erzeugt, werden für die Suche oft externe Dienste wie die [Googles Custom Search](https://developers.google.com/custom-search/v1/overview), [Tapir](http://tapirgo.com/) oder [indexthank](http://indextank.com/) empfohlen. Letzterer Anbieter hat sein Angebot mittlerweile bereits eingestellt und verweist auf der Homepage auf Alternativen. Die Abhängigkeit von einem solchen Dienst hat mich daher eher abgeschreckt. Gerade weil eine Suchfunktion meist keine ressourcenschonende Sache ist, ist eine lange Lebensdauer dieser Suchdienste keine Selbstverständlichkeit. Auch erschien es mir für ein paar zig HTML-Seiten ein ziemlicher Overkill zu sein. ;) 
Jetzt besitzt das Blog eine kleine Javascript/jQuery-getriebene Suche (oben rechts!) - reicht meiner Meinung nach völlig und ist mit einem einfachen Ajax-Request / dem Filtern des RSS-Feeds mit wenig Code einsatzbereit.<!--more-->

Eigene Suchfunktion mit jQuery
===============================
Um mich nicht mit fremden Federn zu schmücken: Die Idee für die jQuery-Suchfunktion stammt von [hier](http://joevennix.com/2011/05/25/How-I-Implement-Static-Site-Search.html). Ich habe den Code leicht angepasst, die wesentliche Funktionsweise bleibt aber die selbe: Der RSS-Feed (der eine einfache XML-Datei ist), wird mit einem $ajax-Call geladen und mit Query und javascript in einem Array gespeichert. Dessen Einträge werden dann mit einem einfachen Regex auf die Suchbegriffe geprüft und bei Treffern in ein anderes Array gelegt. Das Treffer-Array kann dann als HTML-Code ausgegeben werden. Damit auch Suchadressen direkt in den Browser eingegeben werden können, wird [jQuery BBQ](http://benalman.com/projects/jquery-bbq-plugin/) verwendet, die einfache Benutzung von "Hash-Adressen" (z.B. [ganz-sicher.net/blog/#search=test](http://ganz-sicher.net/blog/#search=test)) ermöglicht.

HTML-Code
---------

{% highlight html %}
	<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.7.2/jquery.min.js" type="text/javascript"></script>
	<script src="https://raw.github.com/cowboy/jquery-bbq/v1.2.1/jquery.ba-bbq.min.js" type="text/javascript"></script>

	<!-- Suchfeld -->
	<input type="search" name="query" id="query" placeholder="Search me!">

	<!-- main code: jQuery siteSearch -->
	<script src="js/search.js" type="text/javascript"></script>

	<!-- show search input after page loaded / show search results when user starts search from the browser-address-bar -->
	<script>$(document).ready(function(){ $('#query').show(); $(window).trigger( 'hashchange' ); });</script>

	<!-- hidden by default, matches will be added to #results later -->
	<div id="searchresults">
		<h3 id="searchtitle">Search results</h3>
		<div id="results"></div>
	</div>	
{% endhighlight %}

Da die Suche nur mit JavaScript nutzbar ist, wird Suchfeld sowie Ergebnisbereich (#searchresults) per Default nicht angezeigt und erst mit JavaScript sichtbar gemacht.


CSS-Code
---------

{% highlight css %}
#query 
{
	background-image: url("http://ganz-sicher.net/blog/images/icons/search.png");
	background-position: 2px center;
	background-repeat: no-repeat;
	border: 1px solid #CBD0D5;
	color: gray;
	float: right;
	margin: 2px 2px 0 0;
	padding: 1px 3px 1px 24px;
	width: 200px;
	display: none;
}

#searchresults
{
	display: none;
	margin: 15px 0 35px 0;
	display: none;
	border: 1px solid yellowGreen;
	padding: 5px;
	background: whitesmoke;
}

#searchtitle
{
	color: #ccc;
	text-shadow: 1px 1px white;
	float: right;
}
{% endhighlight %}


search.js Code
==============

Die <a href="{{site.baseurl}}/js/search.js">search.js</a> enthält den die wichtigsten Funktionen für die Suche, im Einzelnen sind das: 

	* ein jQuery-Eventhandler, der beim Abschicken (Eingabetaste) einer Suchanfrage die Browseradresse ändert
	* eine jQuery .bind()-Funktion, die daraufhin aufgerufen wird, den Feed (und die Einträge) lädt und dann findEntries() aufruft
	* eine findEntries()-Funktion, die Treffer in ein Array legt und den Ergebnis-HTML-Code erzeugt
	* eine (optionale) simpleDate()-Funktion, die das Jekyll-Datum in ein lesbares Datum umwandelt

jQuery-Eventhandler für das Suchfeld
--------------------------------------
{% highlight javascript %}
var feedLocation = '/blog/feed.xml';
var defaultSearchInput = 'Search me!'; 

var oldHtml = null;
var entries = null;


// start searching if enter key is pressed in the focused search field
$('#query').keypress(function(e) {
  var code = (e.keyCode ? e.keyCode : e.which);
  var query = $('#query').val();

  if (code == 13) {
	  
	if (query != '') {
		window.location.hash = 'search='+escape(query.replace(/\s/g, '+'));
		e.preventDefault();
	}
	else {
		$('#searchresults').hide();
	}
  }
});
{% endhighlight %}

Die findEntries()-Funktion
---------------------------
{% highlight javascript %}
// given regex q, find matches in entries dom document
// generates a HTML string (resultString) with the search result, adds it to the #results div and
// makes the result element visible
function findEntries(q) {
	var matches = [];
	var rq = new RegExp(q, 'im');
  
	for (var i = 0; i < entries.length; i++) {
		var entry = entries[i];
		
		// get elements
		var title = $(entry.getElementsByTagName('title')[0]).text();
		var link = $(entry.getElementsByTagName('link')[0]).text();             
		var content = $(entry.getElementsByTagName('description')[0]).text();

		// add matches
		if (rq.test(title) || rq.test(link) || rq.test(content)) {
		  var updated = simpleDate($(entry.getElementsByTagName('published')[0]).text());
		  matches.push({'title':title, 'link':link, 'date':updated});
		}
	}
  
	// Build search results
	var resultCount = matches.length;
	var resultString;
  
	if (resultCount > 0){
		resultString = "<span id='articleinfo' style='font-size: 14px; padding: 2px 20px; background-position: 2px 2px; border: 1px solid #ddd;'>" + resultCount + " Entries were found! :)</span><br />";
		
		// show all entries
		for (var i = 0; i < resultCount ; i++) {	
			resultString += '<span style="color: rgb(170, 170, 170); font-family: Monaco,\'Courier New\',monospace; font-size: 13px;">' +matches[i]['date'] + ' » </span> <a href="' + matches[i]['link'] + '">' + matches[i]['title'] + '</a><br />';
		}
				
	}
	else {
		resultString = "No entries found. ;/";
	}
	
	// show the hidden result-div
	$('#results').html(resultString);
	$('#searchresults').show();

}
{% endhighlight %}

jQuery .bind()-Funktion
------------------------
{% highlight javascript %}
$(window).bind('hashchange', function(e) {
		
  // called when the part of the URL after the hash (#) changes
  var query = $.param.fragment();  // e.g. "#search=text"
  
  if (/[#]*search=(.*)/.test(query)) {
    query = $.param.fragment().replace('+', ' ').replace('search=', '');
    $('#query').val(query);  // in case the user browsed to the search
    if (query) {
      if (oldHtml == null) { // save state!
        oldHtml = $('#content').html(); 
      }
      $('#content').html('<div id="loader"></div>');
      $('#footer').hide();
      $('#query').blur().attr('disabled', true);
      if (entries == null) {

        // lazily load and parse the atom.xml feed
        $.ajax({type: 'GET', url: feedLocation, data: '', dataType:'xml', async: false, success: function(data) {
          entries = data.getElementsByTagName('item');
          findEntries(query);         
        }});
      } else { 
        // search the pre-loaded atom.xml feed
        findEntries(query);
      }
      // disable the search bar until current search is complete
      $('#query').blur().attr('disabled', false);
    }
  } else {
    // revert to original page, hide search results
    if (oldHtml == null) { 
      oldHtml = $('#content').html(); 
    }
    $('#content').html(oldHtml);
    $('#footer').show();
    $('#query').blur();
    oldHtml = null;
  }
});
{% endhighlight %}

Demo
----
Wie bereits geschrieben, kann diese Suchfunktion nach Herzenslust oben rechts getestet werden. Wenn ihr die Suche bei eurem eigenen XML-Feed ausprobieren möchtet, solltet ihr darauf achten, dass Sonderzeichen richtig escaped werden (z.B. &amp; statt &), der ajax-Request schlägt sonst z.B. beim Chrome fehl.
Falls ihr weitere Fragen dazu habt, antworte ich gerne im Kommentarbereich, auch für Verbesserungsvorschläge bin ich immer offen. ;)


Linkliste (Archiv) filtern mit jQuery
======================================
Neben dieser netten kleinen Suche, habe ich mich auch auf meiner <a href="{{site.baseurl}}/archive.html">Archivseite</a> inspirieren lassen. Die Filter-Funktion auf [dieser 404-Seite](http://edwardhotchkiss.com/404.html) hat es mir angetan. ([Blogeintrag dazu](http://edwardhotchkiss.com/blog/2012/03/11/jekyll-live-search-with-angular.js/)). Da ich neben jQuery nicht auch noch [AngularJS](http://angularjs.org/) einsetzen wollte, habe ich das mit jQuery (mithilfe von eines [jQuery Listfilters](http://johannburkard.de/blog/programming/javascript/highlight-javascript-text-higlighting-jquery-plugin.html) und [jQuery highlight](http://johannburkard.de/blog/programming/javascript/highlight-javascript-text-higlighting-jquery-plugin.html)) nachgebaut. Das Ergebnis findet sich unter <a href="{{site.baseurl}}/js/archiveFilter.js">archiveFilter.js</a>.
