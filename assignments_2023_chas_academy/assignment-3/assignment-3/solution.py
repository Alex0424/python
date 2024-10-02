def solution(filename):
    answer = {}
    list1 = []
    lowest_word = "Pneumonoultramicroscopicsilicovolcanoconiosis0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000skibidi" #this is the worlds longest word with 45 letters + zeros we are going to shrink this word as much as possible to get smallest word
    with open(filename, "r") as file: #open file
        for line in file: # for loop each line in file
            line = line.replace(".","") #remove dots
            line = line.replace(",","") #remove commas
            words = line.split() #put each word in list
            for words in words: #loop throw list
                if len(words) < len(lowest_word): #word is smaller than current smalest word
                    lowest_word = words
                    list1.clear() 
                    list1.append(lowest_word)
                elif len(words) == len(lowest_word):
                    if words not in list1:
                        lowest_word = words
                        list1.append(lowest_word) #1

    char_list = [] #getting each different character in file and adding that to char_list
    with open(filename, "r") as file:
        for char in file.read():
            if char != " " and char not in char_list and char != "\n":
                char_list.append(char)

    list2 = []
    lowest_word = "" #same as on line 4 but now the variable lowest_word is nothing becouse we are trying to fill it as big as possible to get the longest word
    with open(filename, "r") as file: 
        for line in file:
            line = line.replace(".","")
            line = line.replace(",","")
            words = line.split()
            for words in words:
                if len(words) > len(lowest_word):
                    lowest_word = words
                    list2.clear()
                    list2.append(lowest_word)
                elif len(words) == len(lowest_word):
                    lowest_word = words
                    list2.append(lowest_word) #3    

    all_words = [] 
    with open(filename, "r") as file: #open text document add adding all words we see in it (similar to line 4)
        for line in file:
            line = line.replace(".","")
            line = line.replace(",","")
            for words in line.split():
                all_words.append(words)

    with open(filename, "r") as file: #open file
        lines = file.readlines() #reading each line
    total_lines = len(lines) # adding each line
    try:
        if lines[-1][-1] == "\n": #check if last line is invissible
            total_lines += 1
    except:
        print("nothing exists in the text file")

#-------------------------------------------------
    
    print("All different short words", end=": ") #print out all different short words (loop throw each word in list)
    for word in list1:
        print(word, end=", ")
    print(end="\n\n")

    print("All different character", end=": ") #print all characters
    char_list.sort()
    for word in char_list:
        print(word, end=", ")
    print(end="\n\n")

    print("All long words", end=": ") #print all long words
    for word in list2:
        print(word, end=", ")
    print(end="\n\n")

    print("All words", end=": ") #print all words
    for word in all_words:
        print(word, end=", ")
    print(end="\n\n")

    #print("lines: ",total_lines, "\n")

#-------------------------------------------------

    total_words = 0
    for _ in all_words:
        total_words += 1
    answer["amount_of_all_words"] = total_words #count all words and send it to dict answer

    short_words = 0
    for _ in list1:
        short_words += 1
    answer["amount_of_different_short_word"] = short_words #count all different short words and send it to dict answer

    long_words = 0
    for _ in list2:
        long_words += 1
    answer["amount_of_long_words"] = long_words #count all long words and send it to dict answer

    char = 0
    for _ in char_list:
        char += 1
    answer["amount_of_different_characters"] = char #count all characters and send it to dict answer

    answer["amount_of_lines"] = total_lines

#--------------------------------------------

    print(f"The text file located at {filename} have {total_words} words, {short_words} different shortest words, {long_words} longest words, {char} different characters and {total_lines} lines", end="") #printing out a text that human understand
    print("\n\n")

    return answer