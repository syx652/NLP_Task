
# -*- coding:utf-8 -*-
from bert_serving.client import BertClient
worker=1
bc = BertClient()
li = ['中国', '美国', '澳大利亚']
vecs = bc.encode(li)
print(vecs)




