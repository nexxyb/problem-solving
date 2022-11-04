def countingSort(arr:list) -> list:
    """function that return sorted array of elements in arr"""
    sorted_list=[]
    max_arr=max(arr) 
    f_arr=[0]*(max_arr+1)    
    for i in arr:
        f_arr[i]+=1
    num_arr= [m for m in range(0,max_arr+1)]
    num_zip = dict(zip(num_arr, f_arr))
    #res = {num_arr[i]: f_arr[i] for i in range(len(num_arr))if f_arr[i] != 0}
    for k,v in num_zip.items():
        if v != 0:
            sorted_list+=[k]*v
    return sorted_list

print(countingSort(arr=[1,3,2,1,2,5,4]))
print(countingSort(arr=[1,3,2,12,2,5,4,72,88]))
print(countingSort(arr=[0,41,3,2,12,2,5,4,72,88,322,99,203,144,220,184,300]))