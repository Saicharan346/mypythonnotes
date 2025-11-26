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
    

