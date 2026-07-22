with open("learning_log.txt", "w") as file:
    file.write("Day 9: Python Files")

print("File saved")

with open("learning_log.txt", "a") as file:
    file.write("\nPracticed write and read modes.")


with open("learning_log.txt", "r") as file:
    content = file.read()

print("Saved content:", content)

with open("career_progress.txt", "w") as file:
    file.write("AI Engineer Journey")

print("File saved")

with open("career_progress.txt", "a") as file:
    file.write("\nPython fundamentals in progress")

with open("career_progress.txt", "r") as file:
    content = file.read()

print("Saved content:", content)

try:
    with open("missing_file.txt", "r") as file:
        content = file.read()
    print("Missing file content:", content)

except FileNotFoundError:
    print("File not found. Check the filename.")


try:
    age = int(input("Enter your age:"))
    print("your age is:", age)

except ValueError:
    print("Please enter a valid number.")


try:
    score = int(input("Enter your Score:"))

except ValueError:
    print("Score must be a number.")

else:
    print("Score saved:", score)



try:
    with open("career_progress.txt", "r") as file:
        content = file.read()

except FileNotFoundError:
    print("Career file not found.")

else:
    print("Career progress:", content)