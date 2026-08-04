#old method
"""def add(a,b,c):
    return(a+b+c)

print(add(10,20,30))"""

#new method with use of *argument

def add(*numbers):
    total = 0
    for n in numbers:
        total += n 
    return total

print(add(10,20,30,40,50,60))    
