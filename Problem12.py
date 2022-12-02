# Find the sum of first n numbers
n=int(input("Enter the nth number: "))
sum=0
for x in range(n+1):
    sum+=x
print("The sum of first ",n," numbers is: ",sum)  