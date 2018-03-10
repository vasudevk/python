import math

str_length = len("If you can talk with crowds and keep your virtue,"
                 "Or walk with Kings—nor lose the common touch,")
print(str_length)

str_conc = "It was made certain I wouldn’t, that I’d inherit nothing "
str_conc1 = "except a whipping of my hindquarters as a form of correction, " \
            "in the cadence of I love you, tar baby, I love you."
print(str_conc + str_conc1)

# join() method
movie = ["The Shape of Water", "Moonlight", "Spotlight", "Birdman", "12 Years a Slave"]
print("* ".join(movie))

# split() method
director = ["Guillermo del Toro", "Damien Chazelle", "Alejandro González Iñárritu", "Alejandro González Iñárritu"]
join_director = "/".join(director)
print(director)
print(join_director)
print(join_director.split("/"))

# partition() method
forget = "Pepper&Salt"
print(forget.partition("&"), type(forget.partition("&")))

home, separator, away = "ArsenalvsChelsea".partition("vs")
print("Home: ", home, "\nAway: ", away)

# another way is to use _ which refers to a dummy variable
depart, _, arrival = "New York-Florence".partition("-")
print("Departure: ", depart, "\tArrival: ", arrival)

# format() method - used to replace fields/values delimited by {}
wine = "When a wine is stored for {0} years, then it gets a {1} rating".format("10", 99)
print(wine)

# named fields are matched with keyword arguments
latlong = "Hovering at {latitude} {longitude}".format(latitude="60N", longitude="5E")
print(latlong)

pos = (66.6, 101.1, 12.2)
position = "Galactic position is x={pos[0]} y={pos[1]} z={pos[2]}".format(pos=pos)
print(position)

constants = "Math constants: pi = {m.pi}, e = {m.pi}".format(m=math)
print(constants)

# python formatting mini-language
constants_decimal = "Math constants: pi = {m.pi:.4f}, e = {m.pi:.2f}".format(m=math)
print(constants_decimal)
