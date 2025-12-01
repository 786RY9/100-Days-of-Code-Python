

# file = open("Day 24/my_file.txt")
# contents = file.read()
# print(contents)
# file.close()

# with open("Day 24/my_file.txt") as file:
#     contents = file.read()
#     print(contents)


with open("Day 24/my_file.txt", mode="a") as file:
    file.write("\nback slash n to append in file on a new line else it will start appending at point where files last character was. appending new text")
 
with open("new_file.txt", mode="w") as file:
    file.write("Created a new file with some text in it.")