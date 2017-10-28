# https://www.weather-forecast.com/locations/Paris/forecasts/latest

import re
import urllib.request
#url = "https://www.weather-forecast.com/locations/"
city = input("Enter the name of the City ?")
url = "https://www.weather-forecast.com/locations/" + city + "/forecasts/latest"
print(url)
urldata = urllib.request.urlopen(url).read()
urlDecodeData = urldata.decode("utf8")
m = re.search('span class="phrase">' , urlDecodeData)
print(m)
start = m.end()  # This will trim all the front data i.e span class = phrase part.
end = start + 300 # This will collect 300 characters after the start position defined above
newString = urlDecodeData[start:end]
print(newString)
p = re.search("</span>",newString)
end = p.start() - 1
final = newString[0:end]
print(final)

print("Weather Details for " + city + " :" + final)
