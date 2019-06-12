# googleporks

A project to automate google dorks, I've tried it with threads, but google does not like it, and responds with error 428.

They're bad people.

Use **googlesearch** and **terminal_text_color** to be cuter.

**pip install google.**

Good people -> (https://github.com/MarioVilas/googlesearch.git)

**pip install terminal_text_color**

**from PyPDF2 import PdfFileReader**

Usage examples:

./googleporks -u renfe.com -d dicts/files.txt -n 30 

That shit use dictionary files.txt ("filetype:pdf, filetype:xls...") and the the search is equal to: (site:renfe.com + filetype:pdf) the (-n 30) option shows the first 30 results.

./googleporks -u renfe.com -d dicts/files.txt -n 30 -e www.renfe.com

It similar, but exclude the domain www.renfe.com and only serach in subdomains. Is equal to: (site:renfe.com + filetype:doc -site:www.renfe.com)

./googleporks -u renfe.com -d dicts/files.txt -n 30 -e www.renfe.com -o "intext:euros"


The "-o" option, it's a good option to look for more cool things. 

q:Can I save a souvenir from my search?

Yes! with the option w in raw format. Can add -w souvenir.txt and all the results will be saved there.

---------------------------------------------------------------------------------------------------------------------
12/06/2019

Well, today I have smoked a joint, and it occurred to me to add  module --meta. To search and subtract metadata in pdf (for now).

Example:

./googleporks -u renfe.com --meta -v -n 50
That will create a folder called renfe.com, download the files and subtract the metadata.
And it's so cool, that he created a ./renfe.com/metadata_results.txt file, where the results will be.

That shit reminds me of something:
https://www.youtube.com/watch?v=hkC-hX_i3pw&has_verified=1


                ,-,------,
              _ \(\(_,--'
         <`--'\>/(/(__
         /. .  `'` '  \
        (`')  ,        @
         `-._,        /
            )-)_/--( >  jv
           ''''  ''''
