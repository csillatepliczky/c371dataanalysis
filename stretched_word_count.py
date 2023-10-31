# Stretched Text Count Analysis - Csilla Tepliczky, 17.10.2023
import string

# Prompt the user for a text input
text1 = input('Enter a text: ')
input_word = input('Which word\'s frequency would you like? ')

def count(text, word):
    # Converting text to lower case
    lowercase_text = text.lower()

    # Removing punctuation
    for punctuation in string.punctuation:
        lowercase_text = lowercase_text.replace(punctuation, '')
    lowercase_text = lowercase_text.replace('—', '')

    # Putting the words into a list
    word_list = lowercase_text.split()

    # Finding the distinct words in the list
    unique_list = []
    for word in word_list:
        if word not in unique_list:
            unique_list.append(word)

    # Calculating the frequency of words in the text
    frequency = dict()
    for item in unique_list:
        frequency[item] = word_list.count(item)

    # Sort the items in the dictionary alphabetically
    sorted_frequency = {key: value for key, value in sorted(frequency.items())}

    # Return the alphabetically sorted dictionary and the frequency of the requested word
    return f'The word frequency is: {sorted_frequency}, the requested word appears {frequency[word]} times'
    

print(count(text1, input_word))