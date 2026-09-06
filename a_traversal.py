marks = [88, 76, 34, 55, 23, 97]

for mark in reversed(marks):
    print(mark)

for mark in marks[::-1]:
    print(mark)    

for i in range (len(marks)-1, -1, -1):
    print(marks[i])    

"""for mark in marks:
    print(mark)

for i in range(len(marks)):
    print(marks[i])    """