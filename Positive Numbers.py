list1 = [12, -7, 5, 64, -14]
list2 = [12, 14, -95, 3]
p0 = [num for num in list1 if num >= 0] 
p1 = [num for num in list2 if num >= 0]
print("List1 =",list1) 
print([*p0])
print("List2 =",list2) 
print([*p1]) 
