i=1
s=1
str1=""
while(i<=5):
    j=5
    while(j>=i):
        str1+=" "
        j=j-1
    n=1
    while(n<=i):
        str1+=str(n)
        n=n+1
    k=i+1
    while k<=s:
        str1+=str(k)
        k=k+1
    s=s+2
    str1+="\n"
    i=i+1
print(str1)
#pattern program