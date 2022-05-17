# coding: utf-8
import regex
from collections import Counter
#ファイルを読み込む。
f=open('')
list=f.readlines()
#空リストの作成。
wordlist=[]
for i in list:
#ファイルをリストに追加する。
    word=i.split()
    wordlist.append(word)
#リスト内の「モーラ」を指定して並び替え。
from operator import itemgetter
def sort_mora():
    sort=sorted(wordlist,key=itemgetter(2))
#結果をファイルへ。
    f01=open('','a')
sort_mora()

#並び替えた結果を読み込んで箇条書きに。
f02=open('')
text=f02.read()
SDIV=regex.compile(r"],")
def main():
    for rec in SDIV.split(text):
        f=open('','a')
        print(rec,file=f)
main()
