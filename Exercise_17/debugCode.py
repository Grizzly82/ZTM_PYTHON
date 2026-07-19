import pdb

def buggy_function(n):
    result = 0
    for i in range(n):
        result += i
    return result

pdb.set_trace()
print(buggy_function(5))