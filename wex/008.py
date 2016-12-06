# coding:utf-8
import re
import requests

def get_body(url):
    html_content = requests.get(url).content
    r = re.compile('>(?:<.[^>]*>)?(.*?)</')
   
    result = r.findall(html_content)
    return result

if __name__ == '__main__':
    a=get_body('http://www.taobao.com/')
    for i in a:
        print i 
 # "'>(?:<.[^>]*>)?(.*?)<"
 # 解析：1.d'>(?:<.[^>]*)' 匹配 ><>  格式的内容 直到再次出现> ?: 表示不分为组
 #   2.？ 表示匹配0个或1个，
 # 3. （.*?） 匹配前面格式<> 的内容 直到出现<

