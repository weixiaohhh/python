from bs4 import BeautifulSoup
import requests
import  re


DstDir ="imgfile\\"

def getlinks(url,pagenum=3):
    links =[]
    for i in range(1,pagenum+1):
        new_url = re.sub(r'see_lz=\d','see_lz='+str(i),url)

        links.append(new_url)
    return links

def get_imgURL(url):
    img_urls=[]
    content = requests.get(url).content
    bsobj = BeautifulSoup(content)
    img_url = bsobj.findAll("img", {"class": "BDE_Image"})
    for link in img_url:
        img_urls.append(link.attrs['src'])
    return img_urls

def save_img(url,name):
    with open(DstDir + '%s.jpg' % name, 'wb') as f:
        data = requests.get(img).content

        f.write(data)


if __name__ == '__main__':
    imgs =[]
    url = 'http://tieba.baidu.com/p/2166231880?see_lz=1'
    links = getlinks(url,pagenum=1)

    for link in links:
        img_urls= get_imgURL(link)
        for img_url in img_urls:
            imgs.append(img_url)
    s=0

    for img in imgs:

        save_img(img,s)
        s+=1






