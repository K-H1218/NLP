# coding: utf-8
import regex

#テキストを読み込んで開く。
f=open('')
text=f.read()

def main():
#「。」をチェッカーにする。
  SDIV=regex.compile(r'。')
#テキストを「。」の部分で区切って箇条書きにする。
  for rec in SDIV.split(text):
#検索したい言葉を入力。
    match_word=r''
    example=open('用例.txt','a') 
#区切ったテキストから検索した言葉を含む文だけtxtに出力。
    if match_word in rec:
        #テキストから検索したい言葉の出現数を数える。
        word_count=text.count(match_word)
        print(word_count)
        print(rec,file=example)    
     
main()

