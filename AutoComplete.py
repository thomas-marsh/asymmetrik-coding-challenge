# -*- coding: utf-8 -*-

# Mobile Device Keyboard  Autocomplete #
# Developed for Asymmetrik's Programming Challenge #
# Thomas Marsh May 18th, 2017 #

word_freq = dict() #Dictionary that stores the words trained with their frequencies

char_to_ignore = ",.';:" #Place all punctuation that should be ignored here

def train_autocomplete(passage):
    parsed_passage = passage.lower() #Converts passage to all lowercase
    for ind in range(0, len(char_to_ignore)): #Removes all the characters in string char_to_ignore
        parsed_passage = parsed_passage.replace(char_to_ignore[ind],"")
    words = parsed_passage.split() #Splits passage into a list of words
    for cur_word in words:
        if cur_word in word_freq:
            word_freq[cur_word] += 1; #If the word is already in the dictionary
        else:
            word_freq[cur_word] = 1; #If not in dictionary, adds the word
                     
def get_possible_words(prefix):
    sorted_words = sorted(word_freq, key=word_freq.__getitem__, reverse = True) #Sorts word_freq by decending freq
    possibilities = []
    for cur_word in sorted_words:
        if cur_word.startswith(prefix.lower()): #Appends formatted word and frequency to list of possibilities
            possibilities.append('"'+cur_word+'" ('+str(word_freq[cur_word])+")") 
    return possibilities

def interpret_user_command(user_input):
    if user_input.startswith("Train:"): #If command starts with 'Train:'
        passage_start = user_input.find('"')+1 #Index of start of passage
        if passage_start == 0: #If user enters non-standard syntax for train
            print("Invalid Syntax for Train.  Please use the format 'Train: \"enter passage here\"'")
        else:
            passage_end = user_input.find('"', passage_start) #Index of end of passsage
            training_passage = user_input[passage_start:passage_end] #Extracts the training passage from input
            train_autocomplete(training_passage) #Trains the dictionary using train method
    elif user_input.startswith("Input:"): #If command starts with 'Input:'
        prefix_start = user_input.find('"')+1 #Index of start of prefix
        if prefix_start == 0: #If user enters non-standard syntax for input
            print("Invalid Syntax for Input.  Please use the format 'Input: \"enter prefix here\"'")
        else:
            prefix_end = user_input.find('"', prefix_start) #Index of end of prefix
            prefix = user_input[prefix_start:prefix_end] #Extracts the prefix from input
            suggestions = get_possible_words(prefix) #Gets formatted list of possible suggestions
            print(user_input+" --> ", end = '') #Reprints user input and adds an arrow
            for ind in range(0, len(suggestions)): #Prints out the contents of the suggestions separated with commas
                print(suggestions[ind], end = '')
                if ind < len(suggestions)-1: #If not the last entry
                    print(", ", end = '')
    elif user_input.startswith("Help"): #If command starts with 'Help'
        print("Commands:\n") #Displays the help prompt with a list of the commands
        print("Train: \"enter passage here\"\nUsed to input training passages into the database.\n")
        print("Input: \"enter prefix here\"\nUsed to get suggestions for an inputted prefix.\n")
        print("Quit\nExits the program.\n")
    else:
        print("Invalid Command. For a list of possible commands, enter 'Help'") #If command is invalid
        

print("Enter a command ('Help' for list of commands'):\n") #User prompt with help info

user_input = ""
while(user_input != "Quit"): #Program continues accepting input until user enters the quit command
    user_input = input()   
    interpret_user_command(user_input) 
    
print("Exiting Program.") #Signals that the program has ended
