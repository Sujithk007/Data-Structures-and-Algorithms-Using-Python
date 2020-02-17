m=list(input())
optor=[]
t=''
for i in m:
    if(i.isalpha()):
        optor.append(i)
    elif(len(optor)<2):
        t=t+i+optor.pop()
    else:
        temp=optor.pop()
        t=t+optor.pop()+i+temp
print(t)

# Sample Input:
# ab+c/
# Sample Output:
# a+b/c