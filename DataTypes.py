import math

print('Hello Python!')

# x = 5
# print(3 * x)

for i in range(6):
    x = i * 10
    print(x)

print(math.sqrt(81))
print(math.factorial(10))  # Factorials return integer

n = 5
k = 3
print(math.factorial(n) / (math.factorial(k) * math.factorial(n - k)))  # float
print(math.factorial(n) // (math.factorial(k) * math.factorial(n - k)))  # integer

# Pick 5 winners from a lottery of 100 entries
entries = 100
winners = 5
print(math.factorial(entries) // (math.factorial(winners) * math.factorial(entries - winners)))
print(math.factorial(entries))
print(len(str(math.factorial(entries))))

print(3.125)

print('Speed of light is ' + str(3e8))
print('Planck''s constant is ' + str(1.616e-35))

print(float(7))
print(float("1.618"))
print(float("nan"))
print(float("inf"))
print(float("-inf"))

print(bool(0))
print(bool(100))
print(bool(-100))
