# coding: utf-8
import regex

def main():
#モーラ順に並び替えたファイルを読み込む。
    f=open('')
    text=f.read()
#漢字表記をチェッカーにして取り出す。
    SDIV=regex.compile(r'\s\'[\p{Han}]+|\s\'[\p{KATAKANA}ー]+\b')
    result=regex.sub(SDIV,'',text)
#カナ表記・モーラだけをファイルへ。
    f02=open('','a')
    print(result,file=f02)
main()
