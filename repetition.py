x=input("Please enter a string =")
def cf(str1):
    dict = {}
    for n in str1:
        keys = dict.keys()
        if n in keys:
            dict[n] += 1
        else:
            dict[n] = 1
    sdict = sorted((key,value) for (value, key) in dict.items())
    print(sdict)
print(cf(x))
