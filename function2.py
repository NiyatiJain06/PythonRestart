"""
check student record pass yah fail accouding to there marks.
create funtion()
-> 40>= pass
-> 40<= fail 
"""
def check_result(marks):
    if marks >= 40:
        return "Pass"
    else:
        return "Fail"

marks = int(input("Enter the number:"))
result = check_result(marks)
print(result)    

