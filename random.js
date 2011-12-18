/* this function reads some lines/solgans from an external file line by line and puts them into an array */

function getRandomSlogan()
{
	var slogans = new Array();

	/* fill the new array */
	slogans =   
	[
		"...aus 100%ig recyclebaren Pixeln!.",
		"...über das WehWehWeh und mehr!",
		"Völliger Blödsinn. Aber konsequent.",
		"Linux + OpenSource + Coding == Fun",
		"Bekleben Verboten!",
		"awesome blog is awesome",
		"0101010",
		"// Normal funktioniert's aber!",
		"Relax, its only ONES and ZEROS!",
		"Almost as good as beer.",
		"it works! ...without apache :]",
		"Ein weiteres Blog mit Pinguin-Fetisch"
	];
	
	/* get one random element */
	var randValue = Math.floor(Math.random() * slogans.length );
	
	/* set the random slogan in the header */
	document.getElementById("slogan").innerHTML = slogans[randValue];
}
