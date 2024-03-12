
#read questio again, IF THE WORD nt in the sentence
def checkDuplicate(sen):
    sentence = sen
    sentenceSP = sentence.lower()
    print(sentenceSP)
    sentenceSP2 = []
    letterList = []
    flag = False

    for i in sentenceSP:
        for j in i:
            sentenceSP2.append(j)

    print(sentenceSP2)
    for m in range(len(sentenceSP2)):
        if sentenceSP2[m] not in letterList:
            letterList.append(sentenceSP2[m])
            # print(sentenceSP2[m],letterList)
        else:
            flag = True

    print(letterList)
    return flag
sentenceINP = str(input("Input sentence: "))
print(checkDuplicate(sentenceINP))



