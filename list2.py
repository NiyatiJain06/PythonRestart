Ages = [21,22,23,25,26,27]
print(Ages)
print(type(Ages))
"""
total = 0 # sum using loop
for x in Ages:
    total+=x
    print(total)"""
#append
Ages.append(24)
print(Ages)

#extend
a = [1,2]
a.extend([3,4])
print(a)

#insert
nums =[10,20,40]
nums.insert(2,30)
print(nums)

#remove
names = ["Deepak", "Vinita", "Niyati", "Mahi", "Sparsh"]
print("Before", names)
names.remove("Niyati")
print("After", names)

n = [1,2,3]
n.remove(2)
print(n)

#pop(index)
y = [10,20,30,40,50]
z = y.pop()
print(y)
print(z+100)