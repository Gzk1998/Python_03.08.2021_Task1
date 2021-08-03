# Q1. Input a list from the user, and add the elements in the list 
#     and return the largest and smallest in that list.


def Max_min(list): #function which returns maximum and minimum of the list respectively
    max=list[0]
    min=list[0]
    for element in list:
        if(element>max):
            max=element
        elif(element<min):
            min=element
    return max,min

n=int(input("Enter No of Elements in the list :"))
list=[]
print("Enter Elements of list :")
for i in range(0,n):
    list.append(int(input()))
    
print("Maximum and minimum of the list respectively are :",(Max_min(list)))
