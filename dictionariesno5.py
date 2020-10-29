def kmercount(dna, k):
    mydict = {}
    for substring in range(0,len(dna),k):
        result = dna[substring:substring+k]
        mydict.setdefault(result,0)
        mydict[result] += 1
    return mydict

print(kmercount("acgtacgtaacg",3))
        
        