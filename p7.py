a="ABCDE"
b=len(a)
i=0
str1=''
while(i<=b-1):
    m=b-1
    while(m>=0):
        str1+=str(a[m])
        m=m-1
    str1+="\n"
    b=b-1
print(str1)
#pattern program