i=1
n=6
str1=""
while(i<=n):
    j=1
    while(j<=n):
        str1+=str(j)
        j=j+1
    m=n
    while(m>=i):
        str1+=str(m)
        m=m-1
    str1+="\n"
    n=n-1
print(str1)

  #python pattern program   