# Sum of all Odd and Even no till n 
b=0
c=0
sum=0
u=int(input("Enter the value of n for the range:"))

b=(list(range(0,u+1,2))) 
for x in range(len(b)):
    sum=sum+b[x]
print("The Sum of  even numbers is: ",sum) 
sum=0  
c=(list(range(1,u+1,2))) 
for x in range(len(c)):
    sum=sum+c[x]
print("The Sum of  odd numbers is: ",sum)  
