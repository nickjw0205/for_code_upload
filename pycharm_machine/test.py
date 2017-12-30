import urllib.request

url = "data:image/jpeg;base64,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"

savename = "test.png"

urllib.request.urlretrieve(url, savename)
print("저장되었습니다.")
