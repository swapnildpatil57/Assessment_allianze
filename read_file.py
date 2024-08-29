
import numpy as np

file = "C:\\Users\\swapnil patil\\Desktop\\Pik vima.txt"

with open (file) as f:

    content=f.read()

    print(content)


arr=np.array([1,3,2,4,5,6,7,8])


 # does not count start position
print(arr[2:7])
print(arr[1:])
print(arr[1:5:2])

print(arr[3::-1])

