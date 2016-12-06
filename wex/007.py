# coding:utf-8
import glob,re

code = 0
note = 0
flag = -1

for infile in glob.glob("*.py"):

    with open(infile,'r') as f:

        for i in f:

            if i is None:
                continue
            elif flag == 1:
                note += 1
                continue
            elif i[0]=="#" :
                note +=1
                continue
            elif " ''' " in i :
                matchObj = re.search(r'(.*) \'''(.*?) .*', i)

                if matchObj.group(1) is None:
                    note+=1
                    flag = -flag  # 当出现 ''' 这个符号时候，下面的句子都是注释，知道再次出现
                    continue
                else:
                    code +=1
            else:
                code+=1
                if "#" in i:
                    note+=1   # 如果注释出现在 代码后面,,如果代码print（） 出现先''' 或者# 怎么办？
                                # 解决方法 就是匹配''' 前面的内容， 如果为空，肯定是注释
if __name__ == '__main__':
    print "note total number is:%d"%note
    print "\ncode total number is :%d"%code

