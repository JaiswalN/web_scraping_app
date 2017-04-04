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
    return s.select('a[href^="http://www.mobmp4.org/Mp4-Videos"]')


    
    
def main():
    for x in range(0,65,8):
        s = "http://www.mobmp4.org/Songs/3406/Mp4-Videos/default/" + str(x) + ".html"
        html_doc = fetchurl(s)
        if html_doc:
            result = parsedoc(html_doc)
	    for a in result:
                print a.text
        else:
            print "Didn't got correct response for this url -> %s" % s


