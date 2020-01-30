print("Enter numbers:")
a=[]
b=True
while b:
    n=int(input())
    if  n==0:
        break
    else:
        if(n%2==0):
            a.append(n)
print("Even numbers are:",*a)
