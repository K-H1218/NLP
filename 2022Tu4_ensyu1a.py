# coding: utf-8
import regex
import MeCab

f = open('.txt')
text = f.read()

m = MeCab.Tagger("-d /usr/local/lib/mecab/dic/UniDic-kindai_1603 -O unidic")

SDIV = regex.compile(r'/')
sentences = SDIV.split(text)
for sentence in sentences:
    for v in m.parse(sentence).splitlines():
        gokan_part = v.split()[:5]
        hozon = open('ver3.txt','a')
        if '名詞-普通名詞-一般' in gokan_part[-1]:
            Noun = gokan_part[3:5]
            print(Noun,file=hozon)
        if '動詞-一般' in gokan_part[-1]:
            Verb = gokan_part[3:5]
            print(Verb,file=hozon)
            
f = open('.txt')
text = f.read()
 
SDIV = regex.compile(r'\n')
sentence = SDIV.split(text)
print(sentence.pop())
for S in sentence:
    target = '人文\''
    a = S.find(target)
    b = S[a+len(target):6]
    hozon = open('.txt','a')
    print(b,file=hozon)
