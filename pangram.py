from collections import Counter

def pangrams(s: str) -> str:
    """returns if s pangram or not"""
    total=0
    s_characters=dict(Counter(s))
    lower_character=[m.lower() for m in s_characters.keys()]
    alphs='abcdefghijklmnopqrstuvwxyz'
    for alphabet in alphs:
        if alphabet in lower_character:
            total+=1
    if total==26:
        return 'pangram'
    else:
        return 'not pangram'
    
print(pangrams('We promptly judged antique ivory buckles for the next prize'))
print(pangrams('We promptly judged antique ivory buckles for the prize'))