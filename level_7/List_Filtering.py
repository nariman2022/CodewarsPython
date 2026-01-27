# In this kata you will create a function that takes a list of non-negative integers and strings and
# returns a new list with the strings filtered out.

# Example
# filter_list([1,2,'aasf','1','123',123]) == [1,2,123]

def filter_list(l):
    #return [int(x) for x in l if isinstance(x, int)]

    res = []
    for x in l:
        if isinstance(x, int):
            res.append(int(x))
    return res
