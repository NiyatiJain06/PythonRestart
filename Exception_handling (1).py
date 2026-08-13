try:
    x = int(input("Enter a number:"))
    result = 10/x

except ZeroDivisionError:
    print("You cannot divided with zero")    

except ValueError:
    print("Provide Right value")    
   

else:
    print("Result:", result)   

finally:
    print("Program Execution .....done")    