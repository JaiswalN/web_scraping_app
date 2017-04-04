import requests
from bs4 import BeautifulSoup

def fetchurl(url):
    res = requests.get(url)
    if res.status_code == 200:
        return res.text
    else:
        return False

def parsedoc(html_doc):
    s=BeautifulSoup(html_doc,"html.parser")
    return s.find_all('img',class_="replace-2x img-responsive")

def main():
    for x in range(1,11):
        s = "http://www.zopbazaar.com/6-groceries?=1&p=" + str(x) 
        html_doc = fetchurl(s)
        if html_doc:
            result = parsedoc(html_doc)
	    for a in range(len(result)):
                print result[a]['alt']
        else:
            print "Didn't got correct response for this url -> %s" % s

