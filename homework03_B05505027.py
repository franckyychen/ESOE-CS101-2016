#!/usr/bin/env python3
# -*- coding:utf-8 -*-


# 繳交日期：2016.10.17

# 作業內容：
# 1. 請閱讀 Wikipedia 維基百科 IEEE754 條目 (https://zh.wikipedia.org/wiki/IEEE_754)

# 2. 請試玩 http://armorgames.com/play/17826/logical-element

# 3. 請利用以下空白範本設計一支程式。程式可輸入一段字串，並自動計算出字串中包括空白字元出現的機率。
#    並由高排到低。
#def charFreqLister(inputSTR):
#resultLIST = [(freq, char), (freq, char), (freq, char),...]
#return resultLIST
def charFreqLister(inputSTR):
    alphabet=[]
    freq=[]
    resultlist=[]
    for i in inputSTR:
        b=False
        for j,k in enumerate(alphabet):
            if i==k:
                freq[j]+=1
                b=True
                break
        if not b:
            alphabet.append(i)
            freq.append(1)
    s=sum(freq)
    for i in freq:
        freq[freq.index(i)]/=s
    result=list(zip(freq,alphabet))
    resultlist=sorted(result,key=lambda x:x[0],reverse=True)
    print(resultlist)
    print(sum(freq))
while True:
    a=input("please type some words.")
    charFreqLister(a)

"""

# 3.1 加分題 (有做有加分，沒做不扣分)：請用課堂中提到的「霍夫曼編碼]
#     (https://zh.wikipedia.org/wiki/霍夫曼編碼) 為你之前設計的
#     程式加上轉碼壓縮的功能。
# e.g.,
#def huffmanTranslater(inputSTR):
#resultLIST = [(freq, char, code), (freq, char, code), (freq, char, code),...]

#return resultLIST

# 4 請參考以下 condNOT() 的例子，設計四個 func() 依以下條件，能算出 condition02 ~ 04 的值

#condition00 not condition01


def condNOT(inputSTR_X):
    outputSTR = ""
    for i in inputSTR_X:
        if i == "0":
            outputSTR = outputSTR + "1"
        else:
            outputSTR = outputSTR + "0"
    return outputSTR


#condition00 and condition02
def condAND(inputSTR_X, inputSTR_Y):
    
    outputSTR=""
    
    for i in range(0,len(inputSTR_X)) :      
        if inputSTR_X[i]=="1" :
            if inputSTR_Y[i]=="1" :
                outputSTR=outputSTR+"1"
            else :
                outputSTR=outputSTR+"0"   
        else:
            outputSTR=outputSTR+"0"
    
    return outputSTR



#condition00 or condition03
def condOR(inputSTR_X, inputSTR_Y):
    
    outputSTR=""
    
    for i in range(0,len(inputSTR_X)) :      
        if inputSTR_X[i]=="0" :
            if inputSTR_Y[i]=="0" :
                outputSTR=outputSTR+"0"
            else :
                outputSTR=outputSTR+"1"   
        else:
            outputSTR=outputSTR+"1"
    
    return outputSTR    


#condition00 xor condition04
def conXOR(inputSTR_X, inputSTR_Y):
    
    outputSTR=""
    for i in range(0,len(inputSTR_X)) : 
        if inputSTR_X[i]==inputSTR_Y[i] :
            outputSTR=outputSTR+"0"
        else :
            outputSTR=outputSTR+"1"
    return outputSTR


if __name__== "__main__":
    condition00X = "010111001010100001100011"
    condition00Y = "010000110001011100101001"

    condition01 = condNOT(condition00X)
    print(condition01)


    # 5 請完成以下課本習題並將答案以字串型 (str or unicode) 填入。
    print("Ans:")
    Ch3P3_20a = "0 10000001 11001100000000000000000"
    Ch3P3_20b = "1 10000010 10010100100000000000000"
    Ch3P3_20c = "0 10000010 01101101000000000000000"
    Ch3P3_20d = "1 01111101 10000000000000000000000"
    print("========")
    Ch3P3_28a = "234"
    Ch3P3_28b = "overflow"
    Ch3P3_28c = "874"
    Ch3P3_28d = "888"
    print("========")
    Ch3P3_30a = "234"
    Ch3P3_30b = "overflow"
    Ch3P3_30c = "875"
    Ch3P3_30d = "889"
    print("========")
    Ch4P4_3a = "0x99"
    Ch4P4_3b = "0x99"
    Ch4P4_3c = "0xFF"
    Ch4P4_3d = "0xFF"
    print("========")
    Ch4P4_4a = "0x66"
    Ch4P4_4b = "0xFF"
    Ch4P4_4c = "0x11"
    Ch4P4_4d = "0xBB"
    print("========")
    Ch4P4_13a = "1184"
    Ch4P4_13b = "-862"
    Ch4P4_13c = "862"
    Ch4P4_13d = "-1184"
    print("========")
    Ch4P4_15a = "overflow"
    Ch4P4_15b = "no overflow"
    Ch4P4_15c = "no overflow"
    Ch4P4_15d = "overflow"
    print("========")
    Ch4P4_16a = "0x0F51"
    Ch4P4_16b = "0x0F2A(overflow)"
    Ch4P4_16c = "0x8012"
    Ch4P4_16d = "0x7F51(overflow)"
