 # To show multiplication table 2 numbers
n=[]
n.append(int(input("Enter the number1: ")))
n.append(int(input("Enter the number2: ")))
print("The table of  is as follows: ")
for y in range(2):
    for x in range(1,11):
        print(n[y]," X ",x," = ",n[y]*x)