import numpy as np

temperatures=np.array([1,2,3,4,5,6,7,8,9])
print(np.mean(temperatures))
zeros_array= np.zeros(3)
print(zeros_array)
ones_array=np.ones((3,3))
print(ones_array)
fill=np.full((2,2),5)#used to fill the 2*2 matrix all elements by 7
print(fill)
arrange=np.arange(1,10,2)#used to give values from 1 to 10 with step 2
print(arrange)
print(np.eye(3))#used to create an identity matrix of order n
print(fill.shape)  
print(fill.size)
print(fill.ndim)
print(fill.dtype)
floatarray=np.array([1.23,1,23.456])
intarray=floatarray.astype(int)
print(intarray)
samplearray=np.array([1,2,3,4,5,6])
print(samplearray+5)
print(samplearray**2)
'''
function        what it does
np.sum(array)   sum of all elements
np.mean(array)  mean of all the elements
np.min(array)   min
np.max(array)   max
np.std(array)   standard deviation
np.var(array)   variance
'''
samplearray=np.array([1,2,3,4,5,6])
print(samplearray[0])#indexing
print(samplearray[1:5])#slicing
print(samplearray[[1,2,3]])#fancy indexing
print(samplearray[samplearray>3])#boolean masking
newarray=samplearray.reshape(2,3)#reshaping arrays without changing the elements
print(newarray)
print(samplearray)
'''
ravel=view
flatten=copy
'''
multiarray=np.array([[1,2,3],[4,5,6]])
print(multiarray.ravel())#used to change or view directly in the original array
print(multiarray.flatten())#returns to copy of the new array converting multi-dim array to 1-dim array

