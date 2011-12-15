##########################################################################
# PostMore Plugin
# plugin info: splits blog posts at the <!--more--> tag like in wordpress
##########################################################################
# got inspiration from the following sites - thanks! :)
#     * http://saltmypeanuts.com/technology/dr-jekyll/
#     * http://paulstamatiou.com/how-to-wordpress-to-jekyll

module PostMore
    def postmorefilter(input)
			input.split("<!--more-->").first 
    end
end
Liquid::Template.register_filter(PostMore)
