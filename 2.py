import requests as re
from bs4 import BeautifulSoup as bs
url="https://zhidao.baidu.com/question/138562215.html"
zhongshuijiao=re.get(url)
soup=bs(zhongshuijiao.text,"html.parser")
arr=soup.select('img')
i=0
for a in arr:
    pic_url=a['src']
    picture=re.get(pic_url,stream=True)
    names=pic_url.split('/')
    name=names[names.__len__()-1]
    try:
        f=open("D:\\zhongshuijiao\\"+name,"wb")
        f.write(picture.content)
        f.close()
    except:
        print("报错")
    i+=1