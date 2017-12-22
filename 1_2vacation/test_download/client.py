import urllib.request

url = "http://api.aoikujira.com/ip/ini"

#if you want to extract resource of FTP, change http:// to ftp://

# url = "ftp://api.aoikujira.com/ip/ini"

res = urllib.request.urlopen(url)  #call method

data = res.read()	#read the data which is binary data

text = data.decode("utf-8")	#change binary to character by using "decode"

print(text)	#print the data