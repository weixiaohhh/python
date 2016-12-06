# coding:utf-8
import string
import random


def get_cdk(num=1,digit=4):

    total_cdk = []
    for i in range(num):
        a=''
        for i in range(digit):
            s=random.choice(string.letters+string.digits)
            a+=s
        if a in total_cdk:
            num+=1
            continue   #如果出现相同的CDK 跳过添加，次数加1
        total_cdk.append(a.upper())
    return total_cdk

if __name__ == '__main__':
    cdk =get_cdk()
    print cdk

