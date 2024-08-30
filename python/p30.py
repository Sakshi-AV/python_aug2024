def partition_array(array,low,high):
    pivot = array[high]
    j = low
    for i in range(low,high):
        if array[i] < pivot:
           array[j],array[i] = array[i],array[j]
           j+=1
    array[j],array[high] =array[high],array[j]
    return j
def quick_sort(array,low,high):
    if low<high:
        pivot_index = partition_array(array,low,high)
        quick_sort(array, low, pivot_index-1)
        quick_sort(array , pivot_index+1,high)

array = [4,3,8,6,1,1,9,5]
n = len(array)
print("Input array",array)
quick_sort(array, 0 ,n-1)
print("Sorted array",array)
