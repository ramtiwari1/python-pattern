i=4
str1=""
a=2
while(i>=1):
    j=1
    while(j<=i):
        str1+=str(j)
        j=j+1
    k=a
    while(k>2):
        str1+=" "
        k=k-1
    b=i
    while b>=1:
        str1+=str(b)
        b=b-1
    a=a+2
    str1+="\n"
    i=i-1
    
print(str1)
    #pattern program