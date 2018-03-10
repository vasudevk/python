# python name scopes - LEGB
# Local - inside the funtion
# Enclosing - within all the enclosing functions
# Global - within the module
# Built-in - provided by builtins module

count = 0


def show_count():
    print("count = ", count)


def set_count(c):
    count = c  # new local binding of count


# to resolve this scoping we do this
def set_count_global(c):
    global count
    count = c


# In python, everything is an object