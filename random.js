/* this function reads some lines/solgans from an external file line by line and puts them into an array */

function getRandomSlogan()
{
	var slogans = new Array();

	/* fill the new array */
	slogans =   
	[
		"everything that matters - and a little bit more. ;)",
		"Über die Welt, das Universum und den ganzen Rest...",
		"...aus 100%ig recyclebaren Pixeln zusammengesetzt.",
		"...über das WehWehWeh und mehr!",
		"Web 2.0 von seiner unmenschlichsten Seite.",
		"Völliger Blödsinn. Aber konsequent.",
		"Linux, Freeware, Coding und der ganze Rest.. :)",
		"Bekleben Verboten!",
		"0101010",
		"// Normal funktioniert's aber!",
		"Relax, its only ONES and ZEROS!",
		"Any fool can use a computer. Many do...",
		"Ein weiteres Blog über Pinguin-Fetisch"
	];
	
	/* get one random element */
	var n = slogans.length - 1;
	var randValue = Math.floor(Math.random() * n );
	
	/* set the random slogan in the header */
	document.getElementById("slogan").innerHTML = slogans[randValue];
}
