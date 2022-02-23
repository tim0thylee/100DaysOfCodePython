#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
file_names = open("./Input/Names/invited_names.txt", "r")
names_array = file_names.readlines()
file_names.close()
for i in range(len(names_array)):
    file_letter = open("./Input/Letters/starting_letter.txt")
    letter = file_letter.read()
    replaced = letter.replace("[name]", names_array[i].strip("\n"))
    with open(f"./Output/ReadyToSend/letter{i}.txt", mode="w") as data:
        data.write(replaced)
    file_letter.close()

