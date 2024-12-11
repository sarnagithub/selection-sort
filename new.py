#selection sort

list1=[50,7,45,58,32,60,25]     #creating a list
print("original list",list1)    #printing the original list

for i in range (0,len(list1)):          
    ind=i                                        #store the index of min number
    for j in range (i+1,len(list1)):             #find the min number using loop
        if list1[j]<list1[ind]:
            ind=j                               #store the index of min number
    list1[i],list1[ind]=list1[ind],list1[i]         #swapping the min number with the current number
print("sorted list",list1)            #printing the final sorted list