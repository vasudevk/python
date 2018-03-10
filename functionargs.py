import time


def banner(message, border='-'):
    line = border * len(message)
    print(line)
    print(message)
    print(line)


banner("If you can fill the unforgiving minute "
       "With sixty seconds’ worth of distance run, "
       "Yours is the Earth and everything that’s in it,"
       "And—which is more—you’ll be a Man, my son!")

banner("If you can fill the unforgiving minute "
       "With sixty seconds’ worth of distance run, "
       "Yours is the Earth and everything that’s in it,"
       "And—which is more—you’ll be a Man, my son!", "#")

banner(border=".", message="If you can fill the unforgiving minute "
                           "With sixty seconds’ worth of distance run, "
                           "Yours is the Earth and everything that’s in it,"
                           "And—which is more—you’ll be a Man, my son!")


# default args are evaluated only once when def is executed.
# This is a non-issue for immutable objects but when variables like time
# this is a confusing
def show_default(arg=time.ctime()):
    print(arg)


show_default()
show_default()
show_default()
print('\n', time.ctime())


def add_spam(menu=[]):
    menu.append("spam")
    return menu


breakfast = ["bacon", "eggs"]
print(add_spam(breakfast))

lunch = ["pasta", "wine", "cheesecake"]
print(add_spam(lunch))

# when the function is executed, an empty list is created only once
# when the list is used again, it already contains 'spam' in it
# and ad nauseam
print(add_spam())
print(add_spam())
print(add_spam())


# this can be addressed by always using immutable objects like int or string
def add_spams(menu=None):
    if menu is None:
        menu = []
    menu.append("spams")
    return menu


print(add_spams())
print(add_spams())
print(add_spams())
