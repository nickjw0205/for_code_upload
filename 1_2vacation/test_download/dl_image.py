import urllib.request

url = "https://mblogthumb-phinf.pstatic.net/MjAxNzEyMTVfMjEx/MDAxNTEzMzM4NTkxNzUx.mStA2vtHGP-aUXF7OPfzbq1uKuocqQ5Vt8NgbbKXq5og.I-kCe97aPeQNTF6hyP06zVAoyNOzujHei3P8C34qsp8g.JPEG.muczzhang/IMG_2017121520484850.JPG?type=w800"


savename = "test.png"

urllib.request.urlretrieve(url, savename)


print("저장되었습니다.")