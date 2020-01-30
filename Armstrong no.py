n=int(input("Enter a number:"))
temp=n
s=0
while n>0:
    l=n%10
    s+=pow(l,3)
    n=n//10
if s==temp:
    print("It is a Armstrong Number")
else:
    print("Not Armstrong")
