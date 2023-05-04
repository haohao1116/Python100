s = input()

letters = 0
digits = 0
d = {"letters":letters,"digits":digits}
for i in s:
    if i.isdigit():
        d['digits']+=1
    elif i.isalpha():
        d['letters']+=1
    else:
        pass

print(d)


