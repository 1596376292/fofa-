import requests
import base64
from lxml import etree
import time
import sys
def fofa_search(search_data,page):
    page+=1
    for page in range(1, page):
        url = 'https://fofa.so/result?page=' +str(page)+ '&qbase64='
        hearders = {

            'cookie':'Hm_lvt_9490413c5eebdadf757c2be2c816aedf=1614741458,1614827253,1615164313,1615252561; Hm_lvt_eaa57ca47dacb4ad4f5a257001a3457c=1614741459,1614827255,1615164314,1615252562; search_history=port%3D%2222%22; _fofapro_ars_session=16a696391a212b1ca669a97c1b2a95d0; Hm_lpvt_9490413c5eebdadf757c2be2c816aedf=1615252567; Hm_lpvt_eaa57ca47dacb4ad4f5a257001a3457c=1615252568; referer_url=%2Fresult%3Fq%3Dport%253D%252222%2522%26qbase64%3DcG9ydD0iMjIi'
        }

        # search_data_bs = str(base64.b64encode(search_data.encode("utf-8")), "utf-8")
        urls = url + search_data
        print('资产:'+target+'正在获取fofa第' + str(page) + '页的网页地址')
        print(urls)
        try:
            response = requests.get(url=urls, headers=hearders,timeout=5).content
            soup = etree.HTML(response)
            # print(soup)
            ip_data = soup.xpath('//div[@class="re-domain"]/a[@target="_blank"]/@href')
            print(ip_data)
            page += 1
            ipdata = '\n'.join(ip_data)

            with open(r'url.txt', 'a+') as f:
                f.write(ipdata + '\n')
                f.close()
            time.sleep(3)


        except Exception as e:
            pass
# search_data='"glassfish" && port="4848" && country="CN"'

if __name__ == '__main__':
    for i in open('1.txt'):
        print(i)
        target=i.replace('\n','')
        page=50
        fofa_search(target, int(page))

    # fofa_search(search_data,int(page))
