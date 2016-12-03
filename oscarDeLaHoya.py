from bs4 import BeautifulSoup
import urllib2

file = open('oscar.txt', 'w+')
errorFile = open('errorOscar.txt', 'w+')

url = urllib2.urlopen("https://en.wikipedia.org/wiki/Oscar_De_La_Hoya")
soup = BeautifulSoup(url, "lxml")

table = soup.find_all('table', class_="wikitable")[1]

x = 0
for row in table.find_all('tr'):
    y = 0
    for name in row.find_all('td', style="text-align:left;")[0:1]:
	x += 1
	try:
	    file.write(name.text+' ')
	except Exception as e:
	    errorFile.write(str(x)+' '+str(e)+'\n')
	    y += 1
	    pass
    for result in row.find_all('td')[1:2]:
        if y == 0:
	    try:
		file.write(result.text+'\n')
	    except Exception as e:
	        errorFile.write(str(x)+' '+str(e)+'\n')
	        pass
file.close()
errorFile.close()
