
num=int(input("Enter a Number: "))
sum=0
while num>0:
    digit=num%10
    sum+=digit
    num=num//10
print("Sum of digits:",sum)