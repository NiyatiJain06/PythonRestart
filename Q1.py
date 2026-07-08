"""
user input = List [10-12 items]
target element = input

search, 1 by 1 element
indexing number

not found

"""
My_items = list(input("Enter the items"))
target_element = input("Enter the Tareget item:")

search_item = input("Enter the item you want to search:")
if search_item in My_items:
    print("Found")
else:
    print("Not Found!")  
print(type(My_items))      
