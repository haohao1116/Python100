import math
def operation(D):
    C = 50
    H = 30
    res =int(round(math.sqrt(2 * C * float(D) / H)))
    return res

D = input().split(",")
res = []
for d in D:
    res.append(str(operation(d)))


print(",".join(res))


