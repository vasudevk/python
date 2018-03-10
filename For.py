from urllib.request import urlopen

epl = ["Arsenal", "Liverpool", "Chelsea", "Everton", "Spurs"]

for league in epl:
    print(league)

act = {2017: "Emma Stone", 2016: "Brie Larson", 2015: "Julianne Moore", 2014: "Cate Blanchett", }
for actress in act:
    print(actress, act[actress])

# Using with statement with objects which use external resources avoids resource leaks
with urlopen("http://sixty-north.com/c/t.txt") as story:
    story_words = []
    for line in story:
        line_words = line.decode("utf-8").split()
        for word in line_words:
            story_words.append(word)

print(story_words)


def square(x):
    return x * x


print(square(6))


def ready_player_one():
    print("Releasing on March 28th")


ready_player_one()


def even_odd(n):
    if n % 2 == 0:
        print("It is an even number!")
    else:
        print("It is an odd number!")


even_odd(17)
