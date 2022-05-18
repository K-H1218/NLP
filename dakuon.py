# coding: utf-8
import regex
#濁音の文字数を数える。
def main():
    f=open('')
    text=f.read()

    ga=text.count(r'ガ')
    gi=text.count(r'ギ')
    gu=text.count(r'グ')
    ge=text.count(r'ゲ')
    go=text.count(r'ゴ')
    print(ga,gi,gu,ge,go)

    za=text.count(r'ザ')
    zi=text.count(r'ジ')
    zu=text.count(r'ズ')
    ze=text.count(r'ゼ')
    zo=text.count(r'ゾ')
    print(za,zi,zu,ze,zo)

    da=text.count(r'ダ')
    de=text.count(r'デ')
    do=text.count(r'ド')
    print(da,de,do)

    ba=text.count(r'バ')
    bi=text.count(r'ビ')
    bu=text.count(r'ブ')
    be=text.count(r'ベ')
    bo=text.count(r'ボ')
    print(ba,bi,bu,be,bo)

main()
