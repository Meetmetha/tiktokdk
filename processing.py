import requests
import json

from bs4 import BeautifulSoup

def downloadurl(videourl):
    page = requests.get("https://ssstik.io/", headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:86.0) Gecko/20100101 Firefox/86.0","Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8","Accept-Language":"en-US,en;q=0.5","Accept-Encoding":"gzip, deflate","Connection":"close","Upgrade-Insecure-Requests":"1"})
    soup = BeautifulSoup(page.text,'html.parser')
    endpoint=soup.find('form', class_ ='pure-form pure-g hide-after-request').get('data-hx-post')
    values=soup.find('form', class_ ='pure-form pure-g hide-after-request').get('include-vals')
    api_url=('https://ssstik.io'+endpoint)
    tt=values.split(",")[0]
    temp=tt.replace('tt:','')
    ttvalue=temp.replace("'",'')
    ts=values.split(",")[1]
    tsvalue=ts.replace(' ts:','')
    myobj = {'id': videourl,'locale':'en','tt':ttvalue,'ts':tsvalue}
    pos = requests.post(api_url, data=myobj, headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:86.0) Gecko/20100101 Firefox/86.0","Accept":"*/*","Accept-Language":"en-US,en;q=0.5","Accept-Encoding":"gzip, deflate","HX-Request":"true","HX-Target":"target","HX-Current-URL":"https://ssstik.io/","HX-Active-Element":"submit","Content-Type":"application/x-www-form-urlencoded; charset=UTF-8","Origin":"https://ssstik.io","Connection":"close"}, cookies=page.cookies)
    soup2 = BeautifulSoup(pos.text)
    cdnurl=soup2.find(class_='pure-button pure-button-primary is-center u-bl dl-button download_link without_watermark_direct').get('href')
    print(cdnurl)
    return json.dumps({'cdnurl': cdnurl})