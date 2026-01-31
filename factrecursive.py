
def factorial(n):
    if n==0 or n==1: # base case
        return 1
    else:
        return n*factorial(n-1) # recursive case
n=int(input("Enter a number: "))
print("Factorial of",n,"is",factorial(n))