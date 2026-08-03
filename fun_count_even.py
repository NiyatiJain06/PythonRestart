def count_even(n):
    count = 0
    for i in range(1,n+1):
        if i % 2 == 0:
            print("Even:",i)
            count =+1
    return count        

result = count_even(10)
print(result)