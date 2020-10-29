def findvalue(mydict, val):
    keys = []
    for key in mydict.keys():
        if val == mydict[key]:
            keys.append(key)
    return keys

print(findvalue({'a':1,'b':2,'c':3},2))