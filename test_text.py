import sys
import os.path

# Define a function to count the frequency of alphabets in a given string
def count_alphabets(data):
    frequency = {}
    for letter in data:
        if letter.isalpha():  # Check if the character is an alphabet
            lower_case_letter = letter.lower()  # Convert the character to lowercase
            if lower_case_letter in frequency:  # Check if the character is already present in the dictionary
                frequency[lower_case_letter] += 1  # Increment the count if the character is already present
            else:
                frequency[lower_case_letter] = 1  # Initialize the count to 1 if the character is not present
    frequency = dict(sorted(frequency.items(), key=lambda item: item[1], reverse=True))  # Sort the dictionary by value in descending order
    return frequency

# Define a function to count the frequency of top 5 words in a given string
def count_top5_words(data):
    # Split the string into a list of words
    words = data.split()
    # Create an empty dictionary to store the frequency count of each word
    frequency = {}
    # Iterate over each word in the list of words
    for character in words:
        # Convert the word to lowercase to avoid counting different cases separately
        lower_case_character = character.lower()
        # If the word is already in the dictionary, increment its count by 1
        if lower_case_character in frequency:
            frequency[lower_case_character] += 1
        # If the word is not in the dictionary, add it with a count of 1
        else:
            frequency[lower_case_character] = 1
    # Sort the dictionary in descending order of count and convert it to a dictionary
    frequency = dict(sorted(frequency.items(), key=lambda item: item[1], reverse=True))
    # Get the top 5 most frequent words from the dictionary and return them
    common_five = dict(list(frequency.items())[:5])
    return common_five

# Define a function to count the frequency of all words in a given file


# Define a function to extract words from a list of words and count their frequency
def extract_words(words_list):
    words_list = [word.lower() for word in words_list]  # Convert all the words to lowercase
    extra_char = ["'", '\ufeff', '\n', 'c’', ':', '’', '.', '\r', '\t', '?', '&', '#', '$', '-', ',', ']', '[', '!',
                    '&', '(', ')', '”', '%', '"', ";"]
    resultant_List = []
    words_count_list = {}
    for w in words_list:
        # Remove any extra characters from the words
        for c in extra_char:
            w = w.replace(c, "")
        # check if w is not digit
        if not w.isdigit():
            if w != "":
                resultant_List.append(w)
                if w in words_count_list:
                    words_count_list[w] += 1
                else:
                    words_count_list[w] = 1
    return words_count_list, resultant_List

# Define a function to count the frequency of words following the top 5 most frequent words in a given string
import collections

def count_following_words(my_string):
    words = my_string.lower().split() # convert string to lowercase and split into words
    word_count = collections.Counter(words) # count the frequency of each word
    most_common_words = word_count.most_common(5)

    for m_word, m_count in most_common_words:
        # Print the word and its frequency count
        print_word_and_occurrences(m_word, m_count)

        # Get a list of the words that comes after the targeted word
        following_words = get_following_words(words, m_word)

        # Count the frequency of each following word and get the 3 most common
        following_word_count = collections.Counter(following_words).most_common(3)

        # Print the following words and their occurrence counts
        print_following_word_counts(following_word_count)

def print_word_and_occurrences(word, count):
    # print the word and its occurrence count
    print(f"\n{word} ({count} occurrences)")

def get_following_words(words, target_word):
    # find the index of the current word in the list of words
    word_locations = [i for i in range(len(words)) if words[i] == target_word]
    # create a list of the words that come after the current word
    following_words = [words[i + 1] for i in word_locations if i < len(words) - 1]
    return following_words

def print_following_word_counts(word_count_tuples):
    # loop through the following words and their occurrence counts and print them
    for w, c in word_count_tuples:
        print(f"--{w} , {c}")


def make_list_of_words(input_file, count_alpha=False):
    word_list = [] # Initialize an empty list
    alpha_count = {}
    if count_alpha:     # If count_alpha is True, initialize an empty dictionary to hold counts of each alphabetic character
        alpha_count = {chr(i): 0 for i in range(97, 123)}

    # Open the input file in UTF-8 encoding with error handling
    with open(input_file, encoding='utf-8', errors='ignore') as file:

        for line in file:  # Read the file line by line
            # Split the line into words
            words = line.split()
            # Loop through each word
            for word in words:
                # Add the word to the word_list
                word_list.append(word)

                # If count_alpha is True, count each alphabetic character in the word
                if count_alpha:
                    alpha_chars = list(word)
                    for char in alpha_chars:
                        # If the character is alphabetic, convert it to lowercase and update the count in alpha_count
                        if char.isalpha():
                            char = char.lower()
                            if char in alpha_count:
                                alpha_count[char] += 1

    # If count_alpha is True, return both the word_list and the alpha_count dictionary
    if count_alpha:
        return word_list, alpha_count
    # Otherwise, just return the word_list
    else:
        return word_list

def next_following_Words(input_Word, final_list):
    # Create an empty list to store the indices of all occurrences of the input word in the final list.
    find_matching_Indexes = []
    i = 0
    # Iterate through the list and find all occurrences of the input word, and store their indices in the list.
    while i < len(final_list):
        if final_list[i] == input_Word:
            find_matching_Indexes.append(i)
        i += 1
    # Create an empty list to store the indices of the words immediately following the input word.
    find_matching_Indexes_next = []
    i = 0
    # Iterate through the list of indices of the input word, and add 1 to each index to get the index of the following word.
    while i < len(find_matching_Indexes):
        find_matching_Indexes_next.append(find_matching_Indexes[i] + 1)
        i += 1
    # Create a list of the following words by using the indices of the following words.
    next_words = [final_list[i] for i in find_matching_Indexes_next]
    # Return the list of following words.
    return next_words



def Occurrences_next_Words(follow_word_list):
    frequency = {}  # create an empty dictionary to store the frequency of words
    i = 0  # initialize a counter variable
    while i < len(follow_word_list):  # loop over the input list
        word = follow_word_list[i]  # get the current word
        if word in frequency:  # if the word is already in the dictionary
            frequency[word] += 1  # increment its frequency by 1
        else:  # if the word is not in the dictionary
            frequency[word] = 1  # add it to the dictionary with a frequency of 1
        i += 1  # increment the counter variable

    return frequency  # return the dictionary containing the frequency of words




def my_main():

    if len(sys.argv) == 2:
        file = sys.argv[1]

        try:
            with open(file, "r", encoding='utf-8') as f:
                contents = f.read()
        except FileNotFoundError:
            print(f"Error: File '{f}' does not exist.")
            sys.exit(1)

        total_characters = len(contents)
        total_words = len(contents.split())
        total_lines = contents.count("\n")
        words_list = contents.split()
        unique_words = len(set(words_list))

        print("number of characters |   number of words    |  number of lines\n")
        print(f"     {total_characters}         |      {total_words}          |      {total_lines}   \n")
        print("------------------------------------------------------------------------------\n")
        print(f"Total number of unique words are : {unique_words}")
        print("------------------------------------------------------------------------------\n")
        print("Alphabets |   Frequency\n")
        occur = count_alphabets(contents)
        for letter, count in occur.items():
            print(f"{letter}         |      {count}\n")
        print("------------------------------------------------------------------------------\n")
        print("Top 5 most frequent words:\n")
        print("Words     |   occurrences\n")
        w_occur= count_top5_words(contents)
        for word, count in w_occur.items():
            print(f"{word}      ( {count}  occurrences)\n")
        print("------------------------------------------------------------------------------")
        print(count_following_words(contents))



    elif len(sys.argv) == 3:
        read_file = sys.argv[1]
        try:
            with open(read_file, 'r', encoding='utf-8') as f:
                contents = f.read()
        except FileNotFoundError:
            print(f"Error: File '{f}' does not exist.")
            sys.exit(1)

        total_characters = len(contents)
        total_words = len(contents.split())
        total_lines = contents.count("\n")
        words_list = contents.split()
        unique_words = len(set(words_list))

        write_file = sys.argv[2]
        if not os.path.isfile(write_file):
            print(f"Error: File '{write_file}' not found.")
            sys.exit(1)
        else:
            f_open = open(write_file, 'w')
            f_open.write("number of characters |   number of words    |  number of lines\n")
            f_open.write(f"     {total_characters}         |      {total_words}          |      {total_lines}   \n")
            f_open.write("------------------------------------------------------------------------------\n")
            f_open.write(f"Total number of unique words are : {unique_words}\n")
            f_open.write("------------------------------------------------------------------------------\n")
            f_open.write("Alphabets |   Frequency\n")
            occur = count_alphabets(contents)
            for letter, count in occur.items():
                f_open.write(f"{letter}         |      {count}\n")
            f_open.write("------------------------------------------------------------------------------\n")
            f_open.write("Top 5 most frequent words:\n")
            f_open.write("Words     |   Frequency\n")
            w_occur = count_top5_words(contents)
            for word, count in w_occur.items():
                f_open.write(f"{word}      ( {count}  occurrences)\n")
            f_open.write("------------------------------------------------------------------------------\n")
            f_open.write(count_following_words(contents))
            sys.stdout = f_open
            count_following_words(contents)
            sys.stdout = sys.__stdout__
            print("Output written to file successfully\n")
            f_open.close()

    else:
        print("Please provide both file's name")
        sys.exit(1)

if __name__ == "__main__":
    my_main()