# coding: utf-8
import regex

file=open('phonology2_test01.txt')
text=file.read()

def main():
#カナ表記・漢字表記・モーラ数をチェッカーにする。
    kana_kanji_mora=regex.compile(r'[\p{KATAKANA}ー]+[^\d]+\b\d\s')
#テキストからチェッカーにマッチした部分をリスト化する。
    result=regex.findall(kana_kanji_mora,text)
#リスト内の「,」に結合。
    kana_kanji_mora_str=','.join(result)
#「,」をチェッカーにする。
    SDIV=regex.compile(r',')
#チェッカーをもとに行ごとに分割して表示。
    for rec in SDIV.split(kana_kanji_mora_str):
        f=open('PHM1_test05.txt','a')
        print(rec,file=f)
main()
