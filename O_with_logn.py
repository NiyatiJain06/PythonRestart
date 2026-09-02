def find_name(names, target):
    left = 0
    right = len(names) - 1

    while left <= right:
        middle = (left + right) // 2

        if names[middle] == target:
            return middle
        elif names[middle] < target:
            left = middle + 1
        else:
            right = middle - 1

    return -1

names = ["Aayush", "Bhavna", "Chirang", "Diya", "Shenha", "Uday", "Zara"]

target_name = "Shenha"

result = find_name(names, target_name)

if result != -1:
    print("Found at index:", result)

else:
    print("Not found")    
            