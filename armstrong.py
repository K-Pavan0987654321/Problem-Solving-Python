
n=int(input("enter a number"))
temp=n
sum=0
while temp>0:
    digit=temp%10
    sum+=digit**3
    temp//=10
if sum==n:
    print(n,"is an armstrong number")
else:
    print(n,"is not an armstrong number")