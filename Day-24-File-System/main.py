#way to open file that autocloses
# with open("my_file.txt") as file:
#     contents = file.read()
#     print(contents)

#bottom is to write to file
#we need mode = "w" to write, but it will replace
#mode = "a" is append, and will add to file instead of appending
with open("my_file.txt", mode="w") as file:
    file.write("New text.")
