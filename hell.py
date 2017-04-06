# Web scraping ... top 10 movies and its synopsis
print "hello python !!"
from bs4 import BeautifulSoup
import urllib2
url="http://www.imdb.com/chart/top"
page=urllib2.urlopen(url)
soup = BeautifulSoup(page.read(),"html.parser")
data = []
info = []
table = soup.find('table', attrs={'class':'chart'})
table_body = table.find('tbody')

rows = table_body.findAll('tr')[1:10]
#top 10 rows of movies

for row in rows:
    cols = row.find('td',attrs={'class':'titleColumn'}) #find td whse class is titleColumn
    info = []
    plots = []
    a=cols.a
    print a.text

    href = 'http://www.imdb.com' + a.get('href')
    #print href
    #going to other url to find synopsis
    
    page2=urllib2.urlopen(href)
    soup2 = BeautifulSoup(page2.read(),"html.parser")
    synop = soup2.find('div' ,attrs={'class':'summary_text'}).text
    print synop
    
  
