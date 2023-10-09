import requests
import json
#1.指定url
post_url='https://fanyi.baidu.com/sug'
#2.進行UA僞裝，後續指定網站的都需要僞裝
headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'
}
#requests.post(url=post_url)#參數中的data相當於get里的param
#3.進行參數處理（同get的請求一致）
word=input('enter a word')
data={
    'kw':word
}
#4.請求發送
  response = requests.post(url=post_url,data=data,headers=headers)
#5.獲取相應數據,.json返回的是一個對象（字典對象），如果确认响应数据时json类别，才能使用json,在网页检查的响应头可以看到
dic_obj = response.json()
print(dic_obj)

#6.持久化存储
filename=word+'.json'
fp=open(filename,'w',encoding='utf-8')
json.dump(dic_obj,fp=,ensure_ascii=false)
print('打印结束')