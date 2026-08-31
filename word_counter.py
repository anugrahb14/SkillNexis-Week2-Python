
print("===== WORD COUNTER =====")
filename = "sample.txt"
with open(filename, "r") as file:
    content = file.read()
lines = content.splitlines()
words = content.split()
characters = len(content)
print("Number of lines:", len(lines))
print("Number of words:", len(words))
print("Number of characters:", characters)
