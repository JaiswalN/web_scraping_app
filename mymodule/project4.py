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
    return s.find_all("li", class_="first")

def main():
    for x in range(1,11):
        s = "http://m.jagran.com/top-news-page" +str(x)+ ".html"
        html_doc = fetchurl(s)
        if html_doc:
            result = parsedoc(html_doc)
	    for a in range(len(result)):
                print result[a].find_all('a')[0].text
                print "-------------------------"
                inp = raw_input("Do you want to look into description? Press y for yes and n for next and q for exit]")
                if inp=='n':
                    continue
                elif inp=='q':
                    break
                yy=result[a].a['href']
                ss="http://m.jagran.com" + str(yy)
                req=requests.get(ss)
                if req.status_code == 200:
                    html_doc1=req.text
                    soup=BeautifulSoup(html_doc1,"html.parser")
                    aa=soup.select('p p p')
                    for xx in aa:
                        print xx.text



