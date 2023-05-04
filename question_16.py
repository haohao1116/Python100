values = input().split(",")
odds = [x for x in values if int(x) %2 != 0]
print(",".join(odds))