def diagonalDifference(arr:list) -> int:
    """function to calculate the absolute difference between
    the sums of diagonals of square matrix"""
    n=len(arr)
    s1=0
    s2=0
    for i in range(n):
        s1=s1+arr[i][i]
        s2=s2+arr[i][n-i-1]
    return abs(s1-s2)

arr=[[6, 1, 5], [7, 4, 2], [7, 1, 2]]
print(diagonalDifference(arr))