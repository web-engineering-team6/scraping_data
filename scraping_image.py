#-*- coding:utf-8 -*-
import json
from urllib.request import Request, urlopen
import bs4
import os
from time import sleep 

url = "https://search.yahoo.co.jp/image/search?fr=sfp_as&p=%E5%A1%A9%E3%81%8C%E3%81%8A&oq=&ei=UTF-8&b="
file_name = "img_test"
dir_name = "img_test"
try:
	os.mkdir(dir_name)
except:
	pass

for i in range(1, 201, 20):
	req = Request(url + str(i), headers={'User-Agent': 'Mozilla/5.0'})
	res = urlopen(req)
	html = res.read()

	encoding_list = ["utf-8", "utf_8", "euc_jp", 
                    "euc_jis_2004", "euc_jisx0213", "shift_jis",
                    "shift_jis_2004","shift_jisx0213", "iso2022jp",
                     "iso2022_jp_1", "iso2022_jp_2", "iso2022_jp_3",
                    "iso2022_jp_ext","latin_1", "ascii"]

	for enc in encoding_list:
		try:
			html.decode(enc)
			break
		except:
			enc = None

	print(enc)

	soup = bs4.BeautifulSoup(html, "html.parser")
	resources = []
	for a_tag in soup.find("div", id = "gridlist").find_all("a")[::2]:
		href_str = a_tag.get("href")
		resources.append(href_str)
    
	print(len(resources))

	for (j, resource) in enumerate(resources):
		req = Request(resource, headers={'User-Agent': 'Mozilla/5.0'})
		res = urlopen(req)
		sleep(1)
		f = open(dir_name +  "/" + file_name + "_" + str(i + j), "wb")
		f.write(res.read())
		f.close()
		
	sleep(1)
	



