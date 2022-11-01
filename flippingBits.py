
def flippingBits(n:int) -> int :
    """function that converts integers to 32bits integer"""
    flipped=''
    b=str(bin(n))
    b_32=f'{b[2:]}'
    while len(b_32) < 32:
        b_32='0'+b_32
    for num in b_32:
        if num=='0':
            flipped=flipped+'1'
        else:
            flipped=flipped+'0'
    return int(flipped,base=2)
print(flippingBits(10))
    
    