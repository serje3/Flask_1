
def encrypt(word, ass):
    result = ""
    for i in word:
        result += str(ass[1][ass[0].index(ord(i))])
    return result

def decrypt(wordint,ass):
    if(ass==0):
        return "{failed}"
    result=[]
    last=0
    for i in range(0,len(wordint)+1,7):
        if(i!=0):
            result.append(wordint[last:i])
        last=i
    res=""
    try:
        for i in result:
            res += chr(ass[0][ass[1].index(int(i))])
    except ValueError:
        return "Неверный файл-ключ"
    return res