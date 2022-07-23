import googletrans
from googletrans import Translator

trans = Translator()
file1 = open("Others/sample.txt", "r", encoding="utf8")
file2 = open("Others/result.txt", "w", encoding="utf8")

print("\nWant to see all available languages (y/n)?: ")
ans = input()
if ans == "y":
    print("\n")
    print("LANG CODE : LANG NAME")
    for i in googletrans.LANGUAGES:
        print(str(i)+" : "+str(googletrans.LANGUAGES[i]))

print("\nEnter language of text: ")
lang1 = str(input())

print("\nEnter language of translated text: ")
lang2 = str(input())

txt = file1.read()
translated = trans.translate(txt, src=lang1, dest=lang2)
file2.write(translated.text)
