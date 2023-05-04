lines = input().split(",")
values=[]
for s in lines:
    intp = int(s,2)
    if not intp % 5:
        values.append(s)

print(",".join(values))

