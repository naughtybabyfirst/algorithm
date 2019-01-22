
# 冒泡算法

def bubble_sorted(arr):
    for i in range(len(arr)):
        for j in range(i+1):
            if arr[j]>arr[i]:
                arr[j],arr[i] = arr[i],arr[j]
    return arr

# 快排

def quick_sorted(arr):
    if len(arr)==0 or len(arr)==1:
        return arr
    left = [x for x in arr if x < arr[0]]
    right = [x for x in arr if x > arr[0]]
    return quick_sorted(left) + [arr[0]] + quick_sorted(right)

# 归并排序

def mergeSort(arr):
    if len(arr)<=1:
        return arr
    middle=int(len(arr)/2)
    left=mergeSort(arr[:middle])
    right=mergeSort(arr[middle:])
    merged=[]
    while left and right:
        merged.append(left.pop(0) if left[0]<right[0] else right.pop(0))
    merged.extend(right if right else left)
    return merged
