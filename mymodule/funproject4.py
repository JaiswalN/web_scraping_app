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
def innerdoc(html_doc):
    s=BeautifulSoup(html_doc,"html.parser")
    return s.select('p p p')

def main():
    for x in range(1,11):
        s = "http://m.jagran.com/top-news-page" +str(x)+ ".html"
        print s
        html_doc = fetchurl(s)
        if html_doc:
            result = parsedoc(html_doc)
	    for a in range(len(result)):
                print x, a
                print result[a].find_all('a')[0].text
                print "-------------------------"
                inp = raw_input("Do you want to look into description? Press y for yes and n for next and q for exit]")
                if inp=='n':
                    continue
                elif inp =='q':
                    break
                inner=result[a].a['href']
                s1="http://m.jagran.com" + str(inner)
                html_doc1 = fetchurl(s1)
                if html_doc1:
                    result1 = innerdoc(html_doc1)
                    for xx in result1:
                        print xx.text
        if inp=='q':
            break            


