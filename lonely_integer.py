from collections import Counter

def lonelyinteger(a:list)-> int:
    """function that outputs a unique element from an array of integers"""
    b=dict(Counter(a))
    for key in b.keys():
        if b[key]==1:
            return key
        else:
            continue

print(lonelyinteger([1,2,3,4,3,2,1]))
print(lonelyinteger([1,2,3,4,3,4,1]))