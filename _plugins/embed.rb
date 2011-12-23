# this litte jekyll plugin takes links from video sites and embeds these videos as html5 valid code in the posts
# i found the html code (thanks!) here: http://www.brucelawson.co.uk/2009/html-5-flash-embedding-and-other-validation-erors/ 
#
# supported sites:
#	- youtube.com
#	- vimeo.com

require 'uri'

module Jekyll
	class EmbedTag < Liquid::Tag
		def initialize(tag_name, text, tokens)
			super
			@url = text
		end
	
		# generate the html to embed the flash object
		def makehtml(embedurl)
		  html = 	"<div class=\"video\"><object width=\"560\" height=\"344\" data=\"#{embedurl}\">
					<param name=\"movie\" value=\"#{embedurl}\" />
					<param name=\"allowFullScreen\" value=\"true\" />
					<param name=\"allowscriptaccess\" value=\"always\" />
					<embed src=\"#{embedurl}\" type=\"application/x-shockwave-flash\" allowscriptaccess=\"always\" allowfullscreen=\"true\" width=\"560\" height=\"344\" />
					</object></div>"		
		end
	
		# find out provider and prepare url
		def render(context)	
			provider = URI.parse(URI.encode(@url)).host
			
			if provider == 'vimeo.com' || provider == 'www.vimeo.com'
				vimeo_regexp = /^(?:http:\/\/)?(?:www\.)?vimeo\.com\/(\d+)/
				vID = vimeo_regexp.match(@url)[1]
				makehtml("http://player.vimeo.com/video/#{vID}")
			
			elsif provider == 'youtube.com' || provider == 'www.youtube.com'
				yt_regexp = /^(?:http:\/\/)?(?:www\.)?youtube\.com\/watch\?v=([a-zA-Z0-9_-]*)/
				vID = yt_regexp.match(@url)[1]
				makehtml("http://www.youtube.com/v/#{vID}")	
			else
				html = "<a href=\"#{@url}\">#{@url}</a>"
			end
			
		end
	end
end

Liquid::Template.register_tag('embed', Jekyll::EmbedTag)

