set1={"Apple","Mango","Pineapple","Custardapple"}
set2={'Mango','Cherry','Pineapple','Apple'}

print("Set of ME=\n",set1)
print("Set of FRIEND=\n",set2)

print("UNION")
print(set1.union(set2))
print('\n')

print("INTERSECTION")
print(set1.intersection(set2))
print('\n')

print("DIFFERENCE")
print(set1.difference(set2))
print('\n')

set1.add("Strawberry")
set1.remove("Custardapple")

print("Set of ME after update=\n",set1)
