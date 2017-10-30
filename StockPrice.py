# Get the stock Value from Google Finance

import re
import urllib.request

arrayOfStocks = ['TCS','HDFC','RELIANCE','YES']

try:
    for i in arrayOfStocks:

        url ="https://finance.google.com/finance?q="
        #stock = "TATA"
        url = url + i
        #print(url)
        urldata = urllib.request.urlopen(url).read()
        urlDecodeData = urldata.decode("utf8")
        m = re.search('meta itemprop="price"' , urlDecodeData)  # This will get you the position of the searched string the start and end positon
        start = m.start()
        end = start + 50
        newString = urlDecodeData[start:end]
        #print(newString)
        m = re.search('content="', newString)
        start = m.end()
        newString1 = newString[start:]

        m = re.search("/",newString1)
        start = 0
        end = m.end() - 3
        final = newString1[0:end]
        print("The value of " + i + " is " + final)
except:
    print("Sorry we could not find your desired stock " + i + ".")
