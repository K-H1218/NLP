# coding: utf-8
import regex

f=open('')
text=f.read()

def location():
#１モーラ目に濁音を持つ語をtxtへ出力（X＝任意のカタカナ）
    SDIV01=regex.compile(r'\[\'X[\p{KATAKANA}ー]+')
    dakuon01=regex.findall(SDIV01,text)
    the_number01=len(dakuon01)
    f1=open('','a')
    print('1モーラ目に濁音があるのは',dakuon01,file=f1)
    print(the_number01)
    
#２モーラ目に濁音を持つ語をtxtへ出力（X＝任意のカタカナ）
    SDIV02=regex.compile(r'[\p{KATAKANA}]\X[\p{KATAKANA}ー]+')
    dakuon02=regex.findall(SDIV02,text)
    the_number02=len(dakuon02)
    print('2モーラ目に濁音があるのは',dakuon02,file=f1)
    print(the_number02)
    
#3モーラ目に濁音を持つ語をtxtへ出力（X＝任意のカタカナ）
    SDIV03=regex.compile(r'[\p{KATAKANA}]+[\p{KATAKANA}ー]+\X\b+')
    dakuon03=regex.findall(SDIV03,text)
    the_number03=len(dakuon03)
    print('',dakuon03,file=f1)
    print(the_number03)
    
location()
