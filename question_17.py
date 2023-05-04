netAmount = 0
while True:
    s = input().split()
    if s:
        d_w = s[0]
        money = int(s[1])
        if d_w == 'D':
            netAmount += money
        elif d_w == 'W':
            netAmount -= money
    else:
        break

print(netAmount)
