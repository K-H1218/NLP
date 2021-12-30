# coding: utf-8
from slurp_utf8_01 import slurp_utf8
import regex

#テキストを読み込んで開く。
f=open('tsiteiki.txt')
text=f.read()

def main():
#「。」をチェッカーにする。
  SDIV=regex.compile(r'。')
#テキストを「。」の部分で区切って箇条書きにする。
  for rec in SDIV.split(text):
#検索したい言葉を入力。
    match_word=r''
#区切ったテキストから検索した言葉を含む文だけ表示。
    if match_word in rec:
        print(rec)     
main()

#テキストから検索したい言葉の出現数を数える。
word_count=text.count(r'')
print(word_count)
