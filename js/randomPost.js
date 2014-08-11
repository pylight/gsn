---
layout: none
---
function getRandomPost()
{
	var posts = new Array();

	/* fill the new array */
	posts =   
	[
	{% for post in site.posts %}
		"{{ site.url }}{{ post.url }}",
	{% endfor %}
	""
	];
	
	/* get one random element */
	var randValue = Math.floor(Math.random() * posts.length - 1 );
	
	/* redirect to the random post */
	window.location = posts[randValue];
}
