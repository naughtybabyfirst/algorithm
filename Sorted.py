
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

