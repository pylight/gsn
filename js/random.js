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
		"Ein weiteres Blog mit Pinguin-Fetisch",
		"21 is only half of the truth!",
                "..is the world ready for this??",
                "now without evil ads!",
                "Only 45% obsolete",
                "Generating slogans since 2009!",
                "KISS my Arch",
                "...feels like 127.0.0.1",
                "Makepkg, not war!",
                "One day, this will feature a sane slogan",
                "think different, use linux you must!",
                "/* i'm going to fix this later */"
         ];
	
	/* get one random element */
	var randValue = Math.floor(Math.random() * slogans.length );
	
	/* set the random slogan in the header */
	document.getElementById("slogan").innerHTML = slogans[randValue];
}
