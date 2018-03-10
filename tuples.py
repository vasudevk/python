# tuples are delimited by paranthesis and separated by ','
# elements are accessed using [] and 0-based index

t = ("Buffy", 1.42, 10)
print(t)
print(t[0])
print(len(t))

for item in t:
    print('\n', item)

add_t = t + (3e8, 1983.37926, "Piggy")
print(add_t)
print(add_t * 3)

# tuples can contain any type of object and
# chain indexing can be used to access inner elements
pair_tuple = (("Bacon", "Eggs"), ("Cheese", "Wine"), ("Toast", "Pancakes"))
print(pair_tuple[1][1])

act_tuple = ({2017: "Emma Stone", 2016: "Brie Larson"}, {2015: "Julianne Moore", 2014: "Cate Blanchett"})
print(act_tuple[1][2014])

# to create a single element tuple use a trailing ','
not_a_tuple = (123)
print("Not a tuple: ", not_a_tuple)
print(type(not_a_tuple))

single_tuple = (123,)
print("It's a tuple: ", single_tuple)
print(type(single_tuple))

# empty tuple is an empty ()
empty_tuple = ()
print("Empty tuple?", type(empty_tuple))

# tuples are used when returning multiple return values
multi_tuple = 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
print("Multi tuple? ", type(multi_tuple))


def minmax(items):
    return min(items), max(items)


print(minmax(multi_tuple))
print(minmax([10, 100, 38493, 390, 3298]))

# tuple unpacking allows for unpacking data structures into named references
least, highest = minmax([10, 100, 1000, 1e5, 1e-10])
print("Least value is ", least, "\nHighest value is ", highest)

# tuple(iterable) constructor is used to create
# tuples from other iterable series of objects
const = tuple([2018, 2017, 2016, 2015, 2014])
print(const, type(const))

string_tuple = tuple("Ad Infinitum")
print(string_tuple, type(string_tuple))

# in & not in can be used for membership testing for collections
in_tuple = (10, 11, 12, 13, 14, 15)
not_in_tuple = (20, 21, 22, 23, 24, 25)

print(15 in in_tuple)
print(15 not in not_in_tuple)
