s = input()


d = {"upper":0,"lower":0}
for i in s:
    if i.isalpha() and i.isupper():
        d['upper']+=1
    elif i.isalpha() and i.islower():
        d['lower']+=1
    else:
        pass

print(d)


