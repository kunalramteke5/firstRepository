# Promt a Grade for various given range
x=float(input("Enter the Score : "))
if(x<0.6)and(x>0):
    print("F")
elif(x>=0.6)and(x<0.7):
    print("D")
elif(x>=0.7)and(x<0.8):
    print("C")
elif(x>=0.8)and(x<0.9):
    print("B")
elif(x>=0.9)and(x<1):
    print("A")
else:
    print("Score is out of range.")