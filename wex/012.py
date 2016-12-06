# coding:utf-8
import re
spirit = ['sb','你妈','逼','江泽民']
content = raw_input(u'你喜欢我吗?:')
for i in spirit:
    s=re.sub(r'%s'%i, 'xxx', content)
print s
