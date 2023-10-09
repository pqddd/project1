#UA：user agent（請求載體的身份證），
# UA僞裝：門戶網站的服務器會檢測對應請求的載體身份標識，如果監測到請求載體的身份標識是某一款瀏覽器，
#説明請求是一個正常的請求。但是，如果監測到請求的載體身份標識不是基於某一款瀏覽器，則表 示該網站不是一個正常的請求（爬蟲）
#則服務器就很可能拒絕此次請求。
#UA讓爬蟲對應的請求載體身份標識僞裝成某一款瀏覽器。
import requests
#UA僞裝：將對應的User-Agent封裝到一個字典中，此處是僞裝成谷歌，此處為一個反反查策略

headers={
 'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'
}

url='https://sogou.com/web'
#處理url携帶的參數：封裝到字典中
kw=input('enter a word：')
para={
'query':kw
}
response=requests.get(url=url,params=para,headers=headers)
page_text=response.text
filename=kw+'.html'
with open(filename,'w',encoding='utf-8') as fp:
 fp.write(page_text)
 print(filename,'保存成功！！！')
