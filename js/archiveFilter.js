/* the listFilter is taken from http://kilianvalkhof.com/2010/javascript/how-to-build-a-fast-simple-list-filter-with-jquery/ - thanks :) */
	
(function ($) {
  // custom css expression for a case-insensitive contains()
  jQuery.expr[':'].Contains = function(a,i,m){
      return (a.textContent || a.innerText || "").toUpperCase().indexOf(m[3].toUpperCase())>=0;
  };

  // filters the links in the specified area
  function listFilter(area) { 
    $("#searchText")
      .change( function () {
        var filter = $(this).val();
        
        $(area).removeHighlight();
        
        if(filter) {
		  
		  // hide category headings (years/months) and footer
  		  $('.nicehead').hide();$('.nicehead').first().show();$('.bighead').hide(); $('#bottomnotes').hide();
			
          // this finds all links in a list that contain the input, hide others
          $(area).find("a:not(:Contains(" + filter + "))").parent().hide();
          $(area).find("a:Contains(" + filter + ")").parent().show();          
          $(area).find(".archiveDate:Contains(" + filter + ")").parent().show();
          $(area).find(".archiveTag:Contains(" + filter + ")").parent().show();
          
          // highlight results
          $(area + ' a').highlight(filter);
          $(area + ' .archiveDate').highlight(filter);
          $(area + ' .archiveTag').highlight(filter);
          
        } else {
          // show all links
          $(area).find("li").show();
          
          // show all category headings and footer
          $('.nicehead').show();$('.bighead').show(); $('#bottomnotes').show();
        }
        return false;
      })
    .keyup( function () {
        // fire the above change event after every letter
        $(this).change();
    });
  }

  //ondomready
  $(function () {
    listFilter("#archive");
  });
}(jQuery));
