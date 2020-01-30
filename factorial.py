n=int(input("Enter a number:"))
s=1

if n==1or n==0:
    print(1)
else:
    for i in range(n):
        s=s*n
        n=n-1
print(s)
