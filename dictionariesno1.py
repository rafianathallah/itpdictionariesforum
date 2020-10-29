def removekeys(mydict,keylist):
    for keys in keylist:
        mydict.pop(keys)
        
testing = {'a':1,'b':2,'c':3}        
removekeys(testing,'b')
print(testing)