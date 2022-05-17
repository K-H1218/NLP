#coding: utf-8
import regex
import MeCab

f=open('torakiyo_nakiama_sentence.txt')
text=f.read()

SDIV=regex.compile(r'\n')
for string in SDIV.split(text):
    m=MeCab.Tagger('-d /usr/local/lib/mecab/dic/UniDic-kyogen_1603 -O unidic')
    mecab_list1=m.parse(string).splitlines()
    mecab_list2=mecab_list1[1:]
    for v1,v2 in zip(mecab_list1,mecab_list2):
        list1=[v1,v2]
        target='候'
        if target in list1[1]:
            list2=list1[:2]
            hozon=open('u.txt','a')
            print(list2,file=hozon)
        if target in list1[0]:
            list3=list1[:2]
            hozon2=open('v.txt','a')
            print(list3,file=hozon2)
