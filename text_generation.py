import sys
import random
import test_text as tt
import time

def generate_text(input_file, initial_word, no_of_words):
    # Load list of words from input file
    Words_list = tt.make_list_of_words(input_file)
    # Extract word count and total words from list of words
    word_count, total_words = tt.extract_words(Words_list)
    # Find words that follow the initial word
    found_words = tt.next_following_Words(initial_word.lower(), total_words)
    # Count the occurrences of following words
    following_words_count = tt.Occurrences_next_Words(found_words)

    # Calculate the probability of occurrence for each following word
    length_words = len(found_words)
    occurrencess = {}
    for key, value in following_words_count.items():
        probability = float(value) / length_words
        occurrencess[key] = probability

    # Sort the following words by probability of occurrence
    sort_occurencess = sorted(occurrencess.items(), key=lambda item: item[1], reverse=True)
    words = [word[0] for word in sort_occurencess]
    counting = [count[1] for count in sort_occurencess]

    # Generate the requested number of words using a weighted random choice
    generated_words = random.choices(words, counting, k=int(no_of_words))
    merge_words = " ".join(generated_words)

    return merge_words


def main():
    if len(sys.argv) ==1:
        raise NameError("Please provide inputfile, starting word and number of words.")
    elif (len(sys.argv) ==2):
        raise NameError("Please provide starting word and maximum number of words")
    elif (len(sys.argv) == 3):
        raise NameError("Please provide maximum number of words")
    elif (len(sys.argv) == 4):
        input_file = sys.argv[1]
        initial_word = sys.argv[2]
        no_of_Words = sys.argv[3]
        generated_sentense = generate_text(input_file, initial_word, no_of_Words)

        print("-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-\n*")
        print(generated_sentense)
        print("*\n-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-")
    else:
        print("You just need to provide 4 arguments: a script file, input file , starting word and max words")

if __name__ == "__main__":
    start_time = time.time()
    main()
    end_time = time.time()

    print("Runtime:", end_time - start_time, "seconds")

