# googleporks

A project to automate google dorks, I've tried it with threads, but google does not like it, and responds with error 428. They're bad people.

Use google search and terminal_text_color to be cuter.

pip install google.

Good people -> (https://github.com/MarioVilas/googlesearch.git)

pip install terminal_text_color

Usage examples:

./googleporks -u renfe.com -d dicts/files.txt -n 30 

That shit use dictionary files.txt ("filetype:pdf, filetype:xls...") and the the search is equal to: (site:renfe.com + filetype:pdf) the (-n 30) option shows the first 30 results.

./googleporks -u renfe.com -d dicts/files.txt -n 30 -e www.renfe.com

It similar, but exclude the domain www.renfe.com and only serach in subdomains. Is equal to: (site:renfe.com + filetype:doc -site:www.renfe.com)

./googleporks -u renfe.com -d dicts/files.txt -n 30 -e renfe.com -o "intext:euros"

The "-o" option, it's a good option to look for more cool things. 
