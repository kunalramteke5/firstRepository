# to count the occurence of each word 
# To count th total number of words
a=input("Enter the text").split(" ")
for x in range(len(a)):
    print("The word ",a[x]," occurs ",a.count(a[x]),"ntime")
print("The total number of words in the text is:", len(a))