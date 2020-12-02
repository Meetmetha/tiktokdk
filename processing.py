import requests
import json

from bs4 import BeautifulSoup

def downloadurl(videourl):
    URL = 'https://ssstik.io/'
    page = requests.get(URL)
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
    pos = requests.post(api_url, data=myobj, headers = {"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8", "HX-Request":"true", "HX-Target":"target", "HX-Current-URL":"https://ssstik.io", "HX-Active-Element":"Submit"}, cookies=page.cookies)
    soup2 = BeautifulSoup(pos.text,'html.parser')
    tpurl=soup2.find(class_='pure-button pure-button-primary is-center u-bl dl-button download_link without_watermark').get('href')
    thirdpartdownloadurl=("https://ssstik.io"+tpurl)
    cdnurl=soup2.find(class_='pure-button pure-button-primary is-center u-bl dl-button download_link without_watermark_direct').get('href')
    return json.dumps({'cdnurl': cdnurl, 'thirdpartdownloadurl': thirdpartdownloadurl })