import re

def main():
    word_counter = {} #creates an empty dictionary

    #opens the file
    with open('01 - The Fellowship Of The Ring.txt', encoding = 'UTF-8') as f:
        read_data = f.read()

    # Remove special characters (keep only letters and spaces)
    cleaned_data = re.sub(r'[^A-Za-z\s]', '', read_data)

    word_list = cleaned_data.split()  #creates a list of words

    #loops through a list and adds the words to the dictionary
    for word in word_list:
        word = word.lower() #Convert each word to lowercase

        if word in word_counter:
            word_counter[word] += 1 #increments
        else:
            word_counter[word] = 1 #Add word to dictionary with a count of 1


    for key in word_counter.keys():
        print(key, ":", word_counter[key])


if __name__ == "__main__":
    main()

