# Text Count Analysis - Csilla Tepliczky, 17.10.2023
import string

text1 = '''Imagine a vast sheet of paper on which straight lines, triangles, squares, pentagons, 
hexagons, and other figures, instead of remaining fixed in their places, move freely about, on or 
in the surface, but without the power of rising above or sinking below it, very much like shadows 
— only hard and with lumiNous edges — and you will then have a pretty correct notion of my country and countrymen. 
alas, a few years ago, i should have said "my universe": but now my mind has been opened to higher views of things.'''

def count(text):
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

    return frequency

print(count(text1))