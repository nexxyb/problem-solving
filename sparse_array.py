from collections import Counter

def matchingStrings(strings:list, queries:list) -> list:
    """function that checks the number of collection of input queries in collection of strings"""
    results=[]
    string_counter=dict(Counter(strings))
    for query in queries:
        if query in string_counter.keys():
            results.append(string_counter[query])
        else:
            results.append(0)
    return results

print(matchingStrings(strings=['ab', 'ab', 'abc', 'ab'], queries=['ab','abc','bc']))