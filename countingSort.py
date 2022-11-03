def countingSort(arr:list) -> list:
    """function that return a 100 length frequency array of elements in arr"""
    max_arr=max(arr)
    f_arr=[0]*100
    for i in arr:
        f_arr[i]+=1
    return f_arr
