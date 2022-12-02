# Examples based on list methods
list1=["ONE",345,"789",4]
print("Origional list")
print(list1)
list1.append("Five")
print("Appended list with item (Five)")
print(list1)
list2=["SEVEN","EIGHT"]
print("Extension list")
print(list2)
list1.extend(list2)
print("Updated list")
print(list1)
list1.insert(1, "Ten")
print("List with updated Ten")
print(list1)
print("The index of SEVEN IS",list1.index("SEVEN"))
print("Sorted list")
list3=["ONE","TWO","THREE"]
print(list3)
list3.sort()
print("Sorted list")
print(list3)
