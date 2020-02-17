m = list(input())
opert = []
for i in m:
    if i.isalpha():
        opert.append(i)
    else:
        a = opert.pop()
        b = opert.pop()
        k = i + b + a 
        opert.append(k)
print(*opert)

# INPUT:
# AB+CD-*
# OUTPUT:
# *+AB-CD