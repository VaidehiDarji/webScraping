print "hello python !!"
from bs4 import BeautifulSoup
import urllib2
url="http://www.imdb.com/chart/top"
page=urllib2.urlopen(url)
soup = BeautifulSoup(page.read())
data = []
info = []
table = soup.find('table', attrs={'class':'chart'})
table_body = table.find('tbody')

rows = table_body.findAll('tr')
c=0
for row in rows:
    cols = row.findAll('td')
    info = []
    plots = []
    for item in cols:
	#for i in range(1,11):        	
	cols = item.text.strip().encode('utf-8')
        info.append(cols)
    for link in soup.select('td > a[href^=/title/]'):
	    print "helloooooo"
            href = 'http://www.imdb.com' + link.get('href')
            #title = link.string
            #print title
            #get_single_item_data(href)
	    page2=urllib2.urlopen(href)
	    soup2 = BeautifulSoup(page2.read())
            plot = soup2.findAll('div' , 'plot_summary')
  	    for p in plot:
		synopsis = p.find("div","summary_text").text
		plots.append(synopsis) #problem is here somewhere..
            #print info  
            print plots          
    data.append(info)
    c=c+1
    if c==10:
	break
for item in data:
    print item[1]

