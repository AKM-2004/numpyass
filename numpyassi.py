import numpy as np

# Question no 1
print("Start of First")
list1=["1","2","3","4","5"]
array_li=np.array(list)
print(type(list))
print(type(array_li))
print("End of 1")
print("")

#Question no 2
print(array_li.dtype)
print(type(list1[0]))
print("")

#Question no 3
array_li=np.array(list1,dtype=int)
print(array_li.dtype)
print(type(list1[0]))
print("")

#Question no 4
num_list = [ [ 1 , 2 , 3 ] , [ 4 , 5 , 6 ] ]
num_array = np.array(num_list)
print(num_array.shape)
print(num_array.size)
print("")

#Question no 5
zeros3=np.zeros((3,3))
print(zeros3)
print("")

#Question no 6
iden= np.eye(5,5)
print(iden)
print("")
print("End of assignment")
print()

