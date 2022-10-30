def romanToInt(s: str) -> int:
    convert_key={'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
    exception_key= {'IV':4, 'IX':9, 'XL':40, 'XC':90, 'CD':400, 'CM':900}
    convert=[]
    for index, elem in enumerate(s):        
        if index+1 < len(s):            
            if elem+s[index+1] in exception_key.keys():
                convert.append(exception_key[elem+s[index+1]])
            elif s[index-1]+elem in exception_key.keys() and index!=0 :
                continue            
            else:            
                convert.append(convert_key[elem])
        elif index+1==len(s) and s[index-1]+elem not in exception_key.keys() :            
            convert.append(convert_key[elem])
    return sum(convert)
print(f'MCMIX={romanToInt("MCMIX")}')
print(f'XXVII={romanToInt("XXVII")}')
print(f'CMXLIX={romanToInt("CMXLIX")}')
