# def mergeSort(list):
#     if len(list)<=1:return
#     mid =(len(list)+1)//2
#     left=list[:mid]
#     right=list[mid:]
#     mergeSort(left)
#     mergeSort(right)
#     merge(list,left,right)

# def merge(list,left,right):
#     list=[]
#     l,r=0,0
#     while l<len(left) and r<len(right):
#         if left[l]<right[r]:
#             list.append(left[l])
#             l+=1
#         else:
#             list.append(right[r])
#             r+=1
#     if l<len(left):
#         list.extend(left[l:])
#     if r<len(right):
#         list.extend(right[r:])
    
# arr = [12, 11, 13, 5, 6, 7]
# print("Given array is:")
# print(arr)

# mergeSort(arr)

# print("\nSorted array is:")
# print(arr)


def mergeSort(arr):
    if len(arr) <= 1:
        return  

    mid = (len(arr)) // 2  
    left = arr[:mid]
    right = arr[mid:]

   
    mergeSort(left)
    mergeSort(right)

   
    merge(arr, left, right)

def merge(arr, left, right):
    i = j = k = 0 

   
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

   
    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1

   
    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1


arr = [12, 11, 13, 5, 6, 7]
print("Given array is:")
print(arr)

mergeSort(arr)

print("\nSorted array is:")
print(arr)
