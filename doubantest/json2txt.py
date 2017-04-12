#!/usr/bin/env python
#coding=utf-8
import  json
data = []
with open('/Users/xuejl/Desktop/python/doubantest/items.jl') as f:
    for line in f:
        data.append(json.loads(line))
f.close()
with open('/Users/xuejl/Desktop/python/doubantest/items.txt','a+') as f1:
    for line in data:
        name = line['name']
        director_and_player = line['director_and_player'][0].lstrip()

        # print line['name']
        # print line['director_and_player']
        f1.write(name.encode('utf-8'))
        f1.write('    '+director_and_player.encode('utf-8')+'\n')
f1.close()