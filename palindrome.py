def reverse_list(s:list)-> list:
    """function the returns reverse of a list"""
    if len(s)==2:            
        return [s[1],s[0]]
    elif len(s)>2:
        return [s[-1]]+reverse_list(s[:-1])
def isPalindrome( head:list) -> bool:
    if len(head)<=2:
        return 'false'
    elif len(head) > 2:
        reverse= reverse_list(head)
        if head==reverse:
            return 'true'
        else:
            return 'false'
print(isPalindrome(head=[1,2,2,1]))
print(isPalindrome(head=[1,2,3,2,1,4,5,6,7,8,9,8,7,6,5,4,1,2,3,2,1]))
print(isPalindrome(head=[m for m in range(0,149)]))
print(isPalindrome(head=[1,2,5,6,5,2,1]))