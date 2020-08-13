#python 3.6
#!/usr/bin/env python

# -*- coding:utf-8 -*-

#把.txt转换成elasticsearch可以识别的json文件
__author__ = 'BH8ANK'

'''读取文件
'''
a = open(r"D:\BaiduNetdiskDownload\raw_chat_corpus\txt文件\base1.txt", "r",encoding='utf-8')
out = a.read()
#print(out)
TypeList = out.split('\n')
#print(TypeList)

lenth = len(TypeList)
print(lenth)

number = 1
ju_1 = '{"index":{"_index":"newbase","_id":'
ju_2 = '{"text_entry":"'

# print(ju_1)
for x in TypeList:

    res_1 = ju_1 + str(number) + '}}'+'\n'
    print(res_1)
    a = open(r"D:\BaiduNetdiskDownload\raw_chat_corpus\json文件\OutBase1.json", "a", encoding='UTF-8')
    a.write(res_1)


    res_2 = ju_2 + x + '"}'+'\n'
    print(res_2)
    a = open(r"D:\BaiduNetdiskDownload\raw_chat_corpus\json文件\OutBase1.json", "a", encoding='UTF-8')
    a.write(res_2)


    a.close()
    number+=1