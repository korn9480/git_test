import codecs
print("tinkon")
name=input("enter your name :")
age = int(input("enter your age :"))
print("%s age %d".format(name,age))

with codecs.open("./test.txt","r",encoding="utf-8")as f :
    text = f.read()
print(text)