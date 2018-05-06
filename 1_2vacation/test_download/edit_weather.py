import sys
import urllib.request as req
import urllib.parse as parse

# extract parameter
if len(sys.argv) <= 1:
	print("USAGE: download-forecast-argv <Region Number>")
	sys.exit()
regionNumber = sys.argv[1]

# URL incode the parameter
API = "http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp"

value = {
	'stnId' : regionNumber
}

params = parse.urlencode(value)

url = API + "?" + params

print("url = ",url)

#download
data = req.urlopen(url).read()
text = data.decode("utf-8")

print(text)