# coding:utf-8
import re
import sys
import collections

if len(sys.argv) == 1 or sys.argv[1] in ["-h", "--help"]:
    print("usage: .py filename1")
    sys.exit()
else:
    worddict = collections.defaultdict(int) #collections.defaultdict接受一个函数作为参数来初始化
    try:
        with open(sys.argv[1], 'r') as f:
            for line in f:
                #找出所有不是单词的符号
                match = re.findall(r'[^a-zA-Z0-9]+', line)
                for i in match:
                    # they're 这种格式当做一个单词
                    if i == "'":
                        continue
                    line = line.replace(i, ' ')#符号替换成空格
                s = line.split()
                for word in s:
                   worddict[word]+=1
    except IOError as ioerr:
        print ("file error" + str(ioerr))


    with open('info1.txt', 'w') as f:
        f.write('important words :')
        for word,num in worddict.iteritems():
            if num >3:
                f.write(word+' ')


