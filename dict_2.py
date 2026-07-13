x = {
    "a":[1,2,3],
    "b":[10,20,30]
}
print(x)

#update
x.update({
    "Number":[90,87,76]
})
print(x)

#read - key
print(x["a"])

#keys
print(x.keys())

#keys : value
for key, value in x.items():
    print(key,":", value)
#values
print(x.values())

#delete
del x["a"]
print(x)