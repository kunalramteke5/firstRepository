#longest word in a sentence
def myFun(b):
    return len(b)
a=input("Enter the text:").split(" ")
a.sort(reverse=True, key=myFun)
print("The longest word in the text is:",a[0])
