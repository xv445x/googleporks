# googleporks
**NEW UPDATE!!** 
**CVE-2019-11510**

A project to automate google dorks, I've tried it with threads, but google does not like it, and responds with error 428.

They're bad people.

Use **googlesearch** and **terminal_text_color** to be cuter.

**pip install google.**

Good people -> (https://github.com/MarioVilas/googlesearch.git)

**pip install terminal_text_color**

**pip install pypdf2**

Usage examples:

./googleporks.py -u renfe.com -d dicts/files.txt -n 30 

That shit use dictionary files.txt ("filetype:pdf, filetype:xls...") and the the search is equal to: (site:renfe.com + filetype:pdf) the (-n 30) option shows the first 30 results.

./googleporks.py -u renfe.com -d dicts/files.txt -n 30 -e www.renfe.com

It similar, but exclude the domain www.renfe.com and only serach in subdomains. Is equal to: (site:renfe.com + filetype:doc -site:www.renfe.com)

./googleporks.py -u renfe.com -d dicts/files.txt -n 30 -e www.renfe.com -o "intext:euros"


The "-o" option, it's a good option to look for more cool things. 

q:Can I save a souvenir from my search?

Yes! with the option w in raw format. Can add -w souvenir.txt and all the results will be saved there.

---------------------------------------------------------------------------------------------------------------------
12/06/2019

Well, today I have smoked a joint, and it occurred to me to add  module --meta. To search and subtract metadata in pdf (for now).

Example:

./googleporks.py -u renfe.com --meta -v -n 50

That will create a folder called renfe.com, download the files and subtract the metadata.
And it's so cool, that he created a ./renfe.com/metadata_results.txt file, where the results will be.

That shit reminds me of something:
https://www.youtube.com/watch?v=hkC-hX_i3pw&has_verified=1

-------------------------------------------------------------------------------------------------------------------
21/08/2019
**CVE-2019-11510**
That shit it's so funny, search for CVE-2019-11510 in google. To use that:

Search first 20 results:

./googleporks.py --dana

Select a url like .es to search for only .es pages, it's similar to site:.es in google and search for first 450 results:

./googleporks.py --dana -u .es -n 450

if you use the dana mode, googleporks create 2 files, in your fcking folder:

dana_gift.txt -> and dana_vulnerbles.txt.

dana_vulnerbles.txt -> only save info just save information about vulnerable hosts

![alt text](https://github.com/xv445x/googleporks/blob/master/CVE-2019-11510.png)


                ,-,------,
              _ \(\(_,--'
         <`--'\>/(/(__
         /. .  `'` '  \
        (`')  ,        @
         `-._,        /
            )-)_/--( >  jv
           ''''  ''''
