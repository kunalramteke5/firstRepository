# Python program to sort words in a sentence in 
# decreasing order of their length
# Display the sorted words along with their length
x=input().split(" ")
print(x)
b=[]
c=[]
for y in range(len(x)):
    a=[len(x[y]),x[y]]
    b.append(a)
b.sort(reverse=True)
for z in range(len(x)):
    a=[b[z][1],b[z][0]]
    c.append(a)
print(c)
    
    
