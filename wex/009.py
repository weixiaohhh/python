import requests
import re
 
 
def find_links(website):
     html_content = requests.get(website).content
     r = re.compile('href="(.*?)"')
     result = r.findall(html_content)
     return result
 
if __name__ == '__main__':
    print(find_links('http://www.taobao.com/')) 