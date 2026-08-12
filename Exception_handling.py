try:
    x = int(input("Enter a number:"))
    result = 10/x

except:
    print("Somthing wrong happend!")    

else:
    print("Result:", result)   

finally:
    print("Program Execution .....done")    