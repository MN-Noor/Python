def selctionSort(arr):
    for i in range(len(arr)-1):
        min=i
        for j in range(i+1,len(arr)):
            if arr[j]<arr[min]:
                min=j
        arr[i],arr[min]=arr[min],arr[i]
    print(arr)

# if __name__=="__main__":
arr = [64, 25, 12, 22, 11]
selctionSort(arr)



