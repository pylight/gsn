##########################################################################
# PostMore Plugin
# @name: PostMore - Plugin
# @desc: Splits blog posts at the <!--more--> tag like in wordpress
# @thanks: 4 inspiration :) 
#     * http://saltmypeanuts.com/technology/dr-jekyll/
#     * http://paulstamatiou.com/how-to-wordpress-to-jekyll

# @example: usage in a html/markdown/layout-file:
# -------------------------------------------------
# 	{% for post in site.posts limit:5 %}
#
# 		<!-- post title --title>
# 		<a href="{{ site.baseurl }}{{ post.url }}">{{ post.title }}</a>
#
# 		<!post-- abstract -->
# 		{{ post.content | postmorefilter: post.url }} 
#
# 	{% endfor %} 
# -------------------------------------------------


module Jekyll
	module PostMore
		def postmorefilter(input, url)
			# variables
			readmoreClass = "readmore" 	# the div class used for the more-link
			moreText = "weiterlesen..." # the link text for the more link (e.g. 'read on...')
			splitSequence = "<!--more-->" 	# the sting that seperates abstract and tail in your posts
			baseurl = @context.registers[:site].config['baseurl'] 	# baseurl is read from the _config.yml

			parts = input.split(splitSequence)
			if parts.length == 2
				parts.first << "<div><a class=\"" + readmoreClass + "\" href=\"" + baseurl + url  + "\">" + moreText + "</a></div>"
			else
				parts.first
			end
    end
  end
end
Liquid::Template.register_filter(Jekyll::PostMore)
