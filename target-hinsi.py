#正規表現とMecabのインポート
import regex
import MeCab

#ファイルを開いて読み込む（定型）
f = open('.txt')
text = f.read()

#改行を一文の終わりとしてまとめる（コンパイル）チェッカーを作る
SDIV = regex.compile('\n')

#改行で各センテンスを箇条書きにする
for v in SDIV.split(text):
  
#ローカルのディレクトリ（フォルダ）から辞書を指定してMeCabを起動
    m = MeCab.Tagger('-d /usr/local/lib/mecab/dic/UniDic-kyogen_1603 -O unidic')
#MeCabでテキスト全体を形態素解析して1つずつリストに入れて並べる
    for u in m.parse(v).splitlines():
#リストの情報を5番目まで表示
        hinsi = u.split()[:5]
#抜き出したい品詞を指定
        target='動詞-一般'
#もし指定した品詞がリストの最後にあれば。。。
        if target in hinsi[-1]:
#リストの3番目と4番目（語彙素読みと語彙素）を表示
            out=hinsi[2:4]
            print(out)
