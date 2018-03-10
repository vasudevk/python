x = 456;

# returns unique identifier for an object
# used primarily in production for debugging
# id() deals with the object not the reference
print(id(x))

y = x
print(id(y))

print(id(x) == id(y))
print(x is y)

z = 6
print(id(z))
z += 2

# augmented assignment is not assigned a reference instead
# it is added to the original int z
# and finally z is assigned the new int value
# and the remaining int's are garbage collected.

print(id(z))
print(z)

aList = [2, 4, 6]
print(aList)

bList = aList
bList[1] = 16
print(aList)
print(bList is aList)

# Below example clearly illustrates id(). Though p and q have same values,
# both are different objects. Hence id() differentiates them as two distinct objects
# Value equality refers to equivalence of contents
# Identity refers to the same object i.e.,
# p & q are equal in values but different in identity
p = [1, 2, 3]
q = [1, 2, 3]
print(p is q)
print(id(p))
print(id(q))

# Passing arguments
m = [9, 18, 27]


def modify(k):
    k.append(36)
    print("k = ", k)


# The object m changes since k is referring to
# that object and modifying it. The changes are made in object m and k is garbage collected
modify(m)
print(m)

f = [7, 14, 21]


def replace(g):
    g = [8, 16, 24]
    print("g = ", g)


# f and g are referring to the same object when function replace() is invoked
# But g is reassigned to a different object. Hence list f is unchanged
replace(f)
print(f)


# To modify the contents of the list, we do the following
def replace_contents(g):
    g[0] = 8
    g[1] = 16
    g[2] = 24
    print("g = ", g)


replace_contents(f)
print("modified list f = ", f)


# Function arguments are transferred by Pass by Object Reference
# The value of the reference is copied but not the value of the object
def f(d):
    return d


c = [1, 2, 3]
e = f(c)
print(e is c)
