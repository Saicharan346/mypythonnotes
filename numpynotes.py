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

#newarray=np.insert(array,index,value,asix=None(no need to mention for 1-D array))
'''
- array: the original array
- index: where to insert
- values: what to insert
- axis:
- None → flattens the array before inserting
- 0 → inserts as a new row vertical stacking
- 1 → inserts as a new column horizontal stacking
'''
newarray=np.insert(samplearray,2,56)
print(newarray)
smple2_d=np.array([[1,2,3],[4,5,6]])
newarray2=np.insert(smple2_d,0,[3,4,5],axis=0)
print(newarray2)
newarray2=np.insert(smple2_d,0,[3,4,5],axis=0)
print(newarray2)
newarray=np.append(samplearray,[1,4,5])#used to append the values to a array
print(newarray)
new_array=np.concatenate((samplearray,newarray))
print(new_array)
delarray=np.delete(newarray,0,axis=None)
print(delarray)
'''
vstack() horizontally stacking
hstack()vertical stacking

'''
arr1=np.array([[1,2,3],[4,5,6]])
arr2=np.array([[23,4,5],[34,56,7]])
print(np.vstack((arr1,arr2)))
print(np.hstack((arr1,arr2)))
'''
np.split()
equal
np.hsplit() horizontal split
np.vsplit() vertical split
'''
print(np.split(samplearray,2))
'''
Broadcasting is a process in which we manipulate or perform mathematical operations on the 
values of the array
'''
prices=np.array([100,200,300])
dis=10
finalprices=prices=(prices*10/100)
print(finalprices)
'''
matching dimensions[1,2,3]+[1,2,3] =[2,4,6]
expanding single elements [1,2,3]+10=[11,12,13]
Imcompatable type [1,2,3]+[1,2] =ERROR
'''
matrix=np.array([[1,2,3],[1,2,3]])
vector1=np.array([1,2,3,])#Python actually expands the the single vector so that it can be added to the two rows
print(matrix+vector1)
'''
Handling missing values
np.isnan(array)
np.nan_to_num(array,nan=value)default-0
np.isinf() used to handle infinite numbers(tending) 

'''
array1=np.array([1,2,3,np.nan,np.inf,-np.inf])
print(np.isnan(array1))
print(np.nan_to_num(array1,nan=5))
print(array1)
print(np.isinf(array1))