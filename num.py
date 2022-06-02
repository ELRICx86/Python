import numpy as np
# a=np.array([1,2,3,4])
# print(a)
# print(a.shape)
# print(a.ndim)
# print(a.dtype)
# print(a.itemsize)
# print(a.size)

# b = a * np.array([3,0,3,0])
# print(b)

# #List vs numpy

# l= [1,2,3]
# n=np.array([1,2,3])

# #l.append(4)

# l = l +[4] # same as l.append(4)
# n = n + np.array([4]) # same as np.array([4,4,4])

# n = np.sqrt(n)
# n = np.log(n)
# print(l)
# print(n)

#np array operations

# l1 = [1,2,3]
# l2 = [4,5,6]

# n1 = np.array([1,2,3])

# dot=0

# for i in range(len(l1)):
#     dot += l1[i] * l2[i]

# print(dot)
# dot =0
# dot = np.sum(np.array(l1)*np.array(l2))
# print(dot)

# a1 = np.array(l1)
# a2 = np.array(l2)

# print(np.dot(a1,a2))

# dot = 0

# dot = a1 @ a2
# print(dot)


#### nd  array

# a = np.array([[1,2,3],
#             [4,5,6],
#             [7,8,10]])

# print(a.shape) #prints on row and colomn basis
# print(np.sum(a))
# print (a)
# print(a.T) #prints the transpose

# print(np.linalg.inv(a))

# c=np.diag(a)
# print(np.diag(c))


###### array slicing 

# a= np.array([[1,2,3,4],
#             [4,5,6,8]])

# b= a[0,:] #prints the 0th row and all coulmn values
# b= a[0,1:3]# prints the 0th row and 1 to 3-1 coulmn...always ignores the last column
# b= a[:2,0]  #prints the 0th column and all row values

# print(b)



# aa = np.array([[1,2,3],
#                 [4,5,6],
#                 [7,8,9]])

# bool_idx = aa>2
# print(bool_idx)
# print(aa[aa>2]) #prints the values in 1d array which fulfills the condition

# print(np.where(aa>2,aa,-1)) #prints the values in Original array which fulfills the condition and replace the flase values with -1 



#### fancy indexing 

# ab = np.array([34,43,32,65,56,86,34])
# print(ab)
# l3 = [1,3,5]
# print(ab[l3]) # here it prints the mentioned indexes of l3 from the ab numpy array

# even = np.argwhere(ab%2==0).flatten() #prints out all the indexes whcih are even and flatten is used to show in row format

# print(ab[even])

# ax = np.arange(1,7)
# print(ax)

# bb = ax.reshape(2,3) #reshape the np array in row and colomn format. Raiser error if returned 2,4
# print(bb)

# nx = ax[np.newaxis,:]
# print( ax[np.newaxis,:]) #makes a list of lists in row order 
# print( ax[:,np.newaxis]) #same in colomn order


# ax = np.array([[1,2],
#                 [3,4]])

# bx = np.array([[5,6]])

# #concatanate needs tuple input 

# print(np.concatenate((ax,bx),axis=0)) #axis =0 in default format....In this type the colomn index has to be same to concatanate 
# print(np.concatenate((ax,bx),axis=None))# It will return a flat list 
# print(np.concatenate((ax,bx.T),axis=1)) #IN this case bx has to have te same numbers as the row else error


# #hstack and vstack needs tuple input 
# a= np.array([1,2,3,4])
# b= np.array([5,6,7,8])


# print(np.hstack((a,b))) #stack the array horizontally
# print(np.vstack((a,b))) # stack the array vertically

###Broadcasting

a = np.array([[1,2,3,4],[1,2,3,4],[1,2,3,4],[1,2,3,4]])
b= np.array([1,0,0,1])

print(a+b) #it added the values with the matched index.....doesnt need to repeat the values