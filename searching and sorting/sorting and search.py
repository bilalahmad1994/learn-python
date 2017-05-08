def sequentialsearch(arr,ele):
    position=0
    found=False
    while position<len(arr)and not found:
        if arr[position]==ele:
            found=True
        else:
            position=position+1
    return found
arr=[1,9,24,8,6]
print(sequentialsearch(arr,8))



# bubble sorting
# def bubble_sort(arr):
#     # For every element (arranged backwards)
#     for n in range(len(arr)-1,0,-1):
#         #
#         for k in range(n):
#             # If we come to a point to switch
#             if arr[k]>arr[k+1]:
#                 temp = arr[k]
#                 arr[k] = arr[k+1]
#                 arr[k+1] = temp
# arr = [3,2,13,4,6,5,7,8,1,20]
# bubble_sort(arr)
# print(arr)
#
#


# selectons sort
# def selection_sort(arr):
#
#     # For every slot in array
#     for fillslot in range(len(arr)-1,0,-1):
#         positionOfMax=0
#
#         # For every set of 0 to fillslot+1
#         for location in range(1,fillslot+1):
#             # Set maximum's location
#             if arr[location]>arr[positionOfMax]:
#                 positionOfMax = location
#         temp = arr[fillslot]
#         arr[fillslot] = arr[positionOfMax]
#         arr[positionOfMax] = temp
# arr = [3,5,2,7,6,8,12,40,21]
# selection_sort(arr)
# print(arr)


# def len(arr):
#     return (len(arr)-1,0,-1)
# arr = [3,2,13,4,6,5,7,8,1,20]
# len(arr)
# print(arr)
# print(arr.length)




# a=[1,2,3,4,5]
# a.insert(2,3)
# print(a)


#
# def function(arr):
#     for n in range(len(arr)-1,0,-1):
#         print(n)
# arr=[2,12,13,15,1,7]
# function(arr)

# insertion sort



#
# def insertion_sort(arr):
#
#     # For every index in array
#     for i in range(1,len(arr)):
#
#         # Set current values and position
#         currentvalue = arr[i]
#         position = i
#
#         # Sorted Sublist
#         while position>0 and arr[position-1]>currentvalue:
#
#             arr[position]=arr[position-1]
#             position = position-1
#         arr[ position]=currentvalue
# arr =[3,5,4,6,8,1,2,12,41,25]
# insertion_sort(arr)
# print(arr)






# merge sort
# def merge_sort(arr):
#
#     if len(arr)>1:
#         mid = len(arr)//2
#         lefthalf = arr[:int(mid)]
#         righthalf = arr[int(mid):]
#
#         merge_sort(lefthalf)
#         merge_sort(righthalf)
#
#         i=0
#         j=0
#         k=0
#         while i < len(lefthalf) and j < len(righthalf):
#             if lefthalf[i] < righthalf[j]:
#                 arr[k]=lefthalf[i]
#                 i=i+1
#             else:
#                 arr[k]=righthalf[j]
#                 j=j+1
#             k=k+1
#
#         while i < len(lefthalf):
#             arr[k]=lefthalf[i]
#             i=i+1
#             k=k+1
#
#         while j < len(righthalf):
#             arr[k]=righthalf[j]
#             j=j+1
#             k=k+1
# arr = [11,2,5,4,7,6,8,1,23]
# merge_sort(arr)
# print(arr)







def quick_sort(arr):

    quick_sort_help(arr,0,len(arr)-1)

def quick_sort_help(arr,first,last):

    if first<last:


        splitpoint = partition(arr,first,last)

        quick_sort_help(arr,first,splitpoint-1)
        quick_sort_help(arr,splitpoint+1,last)

#
# def partition(arr,first,last):
#
#     pivotvalue = arr[first]
#
#     leftmark = first+1
#     rightmark = last
#
#     done = False
#     while not done:
#
#         while leftmark <= rightmark and arr[leftmark] <= pivotvalue:
#             leftmark = leftmark + 1
#
#         while arr[rightmark] >= pivotvalue and rightmark >= leftmark:
#             rightmark = rightmark -1
#
#         if rightmark < leftmark:
#             done = True
#         else:
#             temp = arr[leftmark]
#             arr[leftmark] = arr[rightmark]
#             arr[rightmark] = temp
#
#     temp = arr[first]
#     arr[first] = arr[rightmark]
#     arr[rightmark] = temp
#
#
#     return rightmark
#
# arr = [2,5,4,6,7,3,1,4,12,11]
# quick_sort(arr)
# print(arr)
