#print a even numbers

#expert
numbers = [1,2,3,4,5,6,7,8,9,10]
even = [i for i in numbers if i%2 == 0]
print(even)

"""even = ["Even" if i%2 == 0 else "Odd" for i in numbers]
print(even)
"""

#beginner
"""for i in numbers:
    if i%2 == 0:
        even.append(i)

print(even)    """    