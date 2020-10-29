def wordfrequencies(mylist):
    mydict = {}
    for word in mylist.split():
        mydict.setdefault(word, 0)
        mydict[word] += 1
    return mydict

print(wordfrequencies("testing i am testing"))