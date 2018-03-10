def add(a, b):
    return a + b


print(add(3, 3))
print(add(3.1, 2.9))
print(add('news', 'paper'))
print(add([1, 2], [5, 4]))

# below statement throws an error.
# Python does not implicitly convert objects between types
print(add("Team consists of ", 11))
