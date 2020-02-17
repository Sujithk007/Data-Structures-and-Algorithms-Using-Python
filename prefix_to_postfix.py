# WORK UNDER PROCESS
m = list(input())
opert = []
for i in m:
    if i.isalpha():
        opert.append(i)
    else:
        a = opert.pop()
        b = opert.pop()
        k = b + a + i  
        opert.append(k)
print(*opert)
