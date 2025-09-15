def symmetricDifference(a, b):
    e = set()
    for i in a:
        e.add(i)
    for i in b:
        if i not in a:
            e.add(i)
    return e
set1 = {0,1,2,4,5}
set2 = {4,5,7,8,9}
print(symmetricDifference(set1, set2))