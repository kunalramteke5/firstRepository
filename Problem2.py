# Repeatedly check for largest no until "done" is detected.
while(1):
    b=[]
    n1=input()
    if(n1=="done"):
        break 
    n2=input()
    if(n2=="done"):
        break
    a=int(n1)
    b=int(n2)   
    if(a<b)or(a==b):
        print("The largest no is: ",b)
    else:
        print("The largest no is: ",a)
    