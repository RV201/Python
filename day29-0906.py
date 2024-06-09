size=int(input("Enter the number of elements you want in array: "))
arr=[]
#taking input of the list
for i in range(0,size):
    elem=int(input("Please give value for index "+str(i)+": "))
    arr.append(elem)
#taking average of the elements of the list
avg=sum(arr)/size
print("Average of the array elements is ",avg)