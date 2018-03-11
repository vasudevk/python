s = "Show how to index into sequences".split()
print(s)
print(s[4])

# indexing from the end
print(s[-5])

# slicing a list using index, negative indexing and including
gunga = "Though I’ve belted you and flayed you, " \
        "By the livin’ Gawd that made you, " \
        "You’re a better man than I am, Gunga Din!".split()
slices = gunga[0:10]
slice_din = gunga[1:-1]
slice_gunga = gunga[1:]
slice_gunga_din = gunga[:-1]
print(slices)
print(slice_din)
print(slice_gunga)
print(slice_gunga_din)

# Below snippet illustrates copying of lists
# New list full_slice[] has a distinct identity but equivalence with gunga[]
full_slice = gunga[:]
print(full_slice)
print(full_slice is gunga)
print(full_slice == gunga)

# copying lists
gunga_copy = gunga.copy()
print(gunga_copy)

gunga_me = list(gunga)
print(gunga_me)

# all these methods only make shallow copies.
# In the below example, only the object a is copied.
# If we change the value of b[0] or b[1][1],
# those changes are also made in a
a = [[10, 100], [9, 81]]
b = a[:]
print(a is b)
print(a == b)
print("Notice how only the reference to object a is copied here!", "\t", a[0] is b[0])
a[0] = [8, 9]
print(a[0])
a[1].append(5)
print("b[1] is", b[1], "a[1] is ", a[1])

# Repetition using *
c = [12, 43]
d = c * 4
print(d)

s = [[-1, 1]] * 5
print(s)

s[3].append(7)
print(s)

# Finding elements in a list
child = "The price of our loss shall be paid to our hands, not another’s hereafter. " \
        "Neither the Alien nor Priest shall decide on it. That is our right. " \
        "But who shall return us the children?".split()
print(child)
i = child.index("Alien")
print(i)
print(child[i])

# print(child.index("unicorn"))  # ValueError is thrown if the element is not found.

count = child.count("shall")
print(count)

# Removing
road = "Somewhere ages and ages hence: " \
       "Two roads diverged in a wood, and I- " \
       "I took the one less traveled by, " \
       "And that has made all the difference.".split()
print(road)

# del road[i] - remove by index
# road.remove("") - remove by value
print(road.remove('Somewhere'))
print(road)

# Insertion
sky = "There is another sky, " \
      "Ever and fair, " \
      "And there is another sunshine, " \
      "Though it be darkness there;".split()
print(sky)
sky.insert(5, "serene")  # insert(index, item)
print(sky)

print(' '.join(sky))
