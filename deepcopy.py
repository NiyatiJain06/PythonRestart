#deepcopy
import copy

a = [10,20,[30,40]]
b = copy.deepcopy(a)

b[2].append(50)
print(a)
print(b)