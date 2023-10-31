# Text Count Analysis - Csilla Tepliczky, 17.10.2023
import string
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer 
lemmatizer = WordNetLemmatizer() 
import json
 

# Define stop words set
stop_words = set(stopwords.words('english'))


# Reading the contents of a file into a variable
def read_text_file(file_path):
    try:
        with open (file_path, "r") as file:
            text = file.read()
            return text
    except FileNotFoundError:
        print('Config file not found')
    except Exception as e:
        print(e)


def split_text(text):
    # Converting text to lower case
    lowercase_text = text.lower()

    # Removing punctuation
    for punctuation in string.punctuation:
        lowercase_text = lowercase_text.replace(punctuation, '')
    lowercase_text = lowercase_text.replace('—', '')

    # Putting the words into a list
    word_list = lowercase_text.split()
    return word_list


# Create a function to clean the text from stop words
def remove_stop_words(words,stop_words):
    words_clean = []
    for word in words:
        if word not in stop_words:
            words_clean.append(word)
    return words_clean


# Lemmatize words to remove the inflicted versions of words
def lemmatize_words(words_clean):
    words_lemmatized_list = []
    for word in words_clean:
        word_lemmatized =  lemmatizer.lemmatize(word)
        words_lemmatized_list.append(word_lemmatized)
    return words_lemmatized_list

# Count the frequency of each word
def compute_frequency_words(words_lemmatized):
        frequency = dict()
        for item in words_lemmatized:
            frequency[item] = words_lemmatized.count(item)
        return frequency

# Save the result in a JSON file
def save_words_frequency(frequency, file_path=r"D:\Csilla\Codebase\src\sixthday\frequency.json"):
    json_data = json.dumps(frequency)
    with open(file_path, "w") as outfile:
        outfile.write(json_data)





text1 = read_text_file(r'D:\Csilla\Codebase\src\sixthday\example.txt')
word_list = split_text(text1)
words_clean = remove_stop_words(word_list,stop_words)
words_lemmatized = lemmatize_words(words_clean)
words_frequency = compute_frequency_words(words_lemmatized)
save_words_frequency(words_frequency,file_path=r"D:\Csilla\Codebase\src\sixthday\frequency.json")