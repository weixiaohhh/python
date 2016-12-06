# coding: utf-8
from PIL import Image,ImageDraw, ImageFont

def add_num(img):

    info_1 = img.split('.')[1]  #获取图像后缀
    im = Image.open(img)
    info_2= im.format    #获取图像信息
    new_im=im.resize((120,120))
    draw = ImageDraw.Draw(new_im)
    fillcolor =  "#ff0000"
    draw.text((90,0),'99',fill=fillcolor)

    new_im.save('t.'+info_1, info_2)



if __name__ == '__main__':

    add_num('Path.png')