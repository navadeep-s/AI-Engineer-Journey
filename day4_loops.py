# Day 4 - Python Loops

print("Numbers from 1 to 5:")

for number in range(1, 6):
    print(number)


print("\nEven numbers from 2 to 10:")

for number in range(2, 11, 2):
    print(number)


print("\nLetters in Navi:")

name = "Navi"

for letter in name:
    print(letter)


print("\nLearning plan:")

languages = ["Python", "SQL", "Java"]

for language in languages:
    if language == "Python":
        print(language, "is learning now")
    else:
        print(language, "is learning later")


print("\nCountdown:")

count = 3

while count >= 1:
    print(count)
    count = count - 1

print("Start")