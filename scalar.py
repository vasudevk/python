# Adjacent literal strings are concatenated
print("first" "second")

# For Strings with Newlines use Multiline strings or Escape sequences
print("""This is a multiline string""")
print('''So this is possible!''')

space = "For tomorrow is the \nbeginning of a \nnew dawn"
print(space)

print("Let\'s strive to write a clean code!")
print("Why always use \" to print something??")

# Strings are sequence types in Python
bird = 'peacock'
print("Letter at index 5 is " + bird[5])
print(bird.capitalize())

# Lists
angle = [0, 45, 90, 180, 360]
football = ["Coach", "Captain", "Striker", "Gooalkeeper", "Defender", "Midfielder"]
print(angle[3])
print(football[1])

# Mutable property of lists
football[1] = "Bergkamp"
print(football)

start = []
start.append(1.414)
start.append(1.616)
start.append(1.2134)
print(start)

# list constructor  - creates list from other collections.
# below statement prints a list of strings
print(list("Arsenal"))

# Dictionary - maps key to value
contact = {"John": "210-210-2110", "Doe": "210-210-2001", "Mona": "210-210-2010", "Lisa": "210-210-0021"}
print(contact["Mona"])

contact["Mona"] = "210-201-0201"
print(contact["Mona"])

# {} are used to create empty dicts
