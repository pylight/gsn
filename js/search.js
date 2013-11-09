/* js/jQuery Ganz-Sicher.Net Search (admin@ganz-sicher.net)
 * This is a simple search script that searches for results in the  blog xml-feed!    
 * Original version is here: http://joevennix.com/2011/05/25/How-I-Implement-Static-Site-Search.html (thanks!)
 * feel free to use/remix ;>
 * */

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
  
  
// convert the jekyll date format into DD.MM.YY
function simpleDate(xmlDate) {
	year = xmlDate.substring(0, 4);
	month = xmlDate.substring(5,7);
	day = xmlDate.substring(8,10);
	
	return day+'.'+month+'.'+year;
}


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
		resultString = "<span id='articleinfo' style='font-size: 14px; padding: 2px 20px; background-position: 2px 2px; border: 1px solid #ddd;'>Zu deiner Suchanfrage wurden " + resultCount + " Einträge gefunden! :)</span><br />";
		
		for (var i = 0; i < resultCount ; i++) {	
			resultString += '<span style="color: rgb(170, 170, 170); font-family: Monaco,\'Courier New\',monospace; font-size: 13px;">' +matches[i]['date'] + ' » </span> <a href="' + matches[i]['link'] + '">' + matches[i]['title'] + '</a><br />';
		}
				
	}
	else {
		resultString = "Leider keine Eintr&auml;ge zu deiner Suchanfrage gefunden ;/<br />Versuche es mit anderen Suchbegriffen.";
	}
	
	// show the hidden result-div
	$('#results').html(resultString);
	$('#searchresults').show();
	$('#query').focus();
}



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


