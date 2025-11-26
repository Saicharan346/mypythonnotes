list1=[]
n=int(input("Enter how many elements in the list"))
for i in range(n):
    inputu=int(input(f"Enter the {i+1} element of the list"))
    list1.append(inputu)
key=int(input("Enter the key to check in the list"))
for j in range(n):
    if(list1[j]==key):
        print("Element Found!!!")
        break
'''Sample Output:
   Enter how many elements in the list5
   Enter the 1 element of the list1 
   Enter the 2 element of the list2
   Enter the 3 element of the list3
   Enter the 4 element of the list4
   Enter the 5 element of the list5
   Enter the key to check in the list3
   Element Found!!!
   '''

