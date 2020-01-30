print("Enter 10 numbers:")
a=[]
for i in range(10):
    n=int(input())
    if (n%2==0):
        a.append(n)
print("Even numbers are:",*a)
