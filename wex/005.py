# coding:utf-8
from __future__ import division
from PIL import Image

def get_right_size(img):

    im = Image.open(img)
    height,width=im.size
    h_div = height/1136
    print h_div
    w_div = width/640
    print w_div
    if h_div>1 or w_div>1:
        div=max(h_div,w_div)
        print div
        height = int(height/div)
        width = int(width/div)
        new_im = im.resize((height,width))# resize 参数必须是整数
    new_im.save('test.jpg','jpeg')


if __name__ == "__main__":
    get_right_size("Path.png")


# 批量创建了当前目录下所有以 .jpg 结尾的图片的缩略图
# from PIL import Image
# import glob, os
#
# size = 128, 128
# for infile in glob.glob("*.jpg"):
#     file, ext = os.path.splitext(infile)# file=c:\123\456\test  exc=.txt
#     im = Image.open(infile)
#     im.thumbnail(size, Image.ANTIALIAS)
#     im.save(file + ".thumbnail", "JPEG")