#HW1-1

c=open("sample.txt",encoding='utf8')
d=c.read()
sampleWordList = []

#為sampleWordList建立一個集合

d=d.replace("?"," ")
d=d.replace("-"," ")
d=d.replace("."," ")
d=d.replace(","," ")
d=d.replace("\n"," ")  

#將標點符號移掉避免其算入字數中

c=d.split(" ")

#將此檔案轉為列表

for a in c:
    if len(a) > 5:
        sampleWordList.append(a)

#把字數大於五的字加入sampleWordList

print(sampleWordList)

#HW1-2
while True: 
    text = input("a word more than five letters: ") 
    
    if text in sampleWordList: 
        print("這個字有在列表裡") 
    else: 
        print("這個字沒在列表裡")