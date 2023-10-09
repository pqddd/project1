#爬取搜狗首頁頁面數據
import requests
url="https://www1.szu.edu.cn/v.asp?id=185"
response=requests.get(url=url)
page_text=response.text
print(page_text)
with open('./shenda.html','w',encoding='utf-8') as fp:
 fp.write(page_text)
 print('爬取數據結束!!!')