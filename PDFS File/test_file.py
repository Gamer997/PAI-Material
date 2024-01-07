import random
from nltk import ngrams

# Load the Poetry list from iqbal.txt and ghalib.txt
poetry_list = []

with open('iqbal.txt', 'r', encoding='utf-8') as file:
    poetry_list += file.read().splitlines()

with open('ghalib.txt', 'r', encoding='utf-8') as file:
    poetry_list += file.read().splitlines()

# Tokenize the poetry_list into words

words = []
for line in poetry_list:
    word_list = line.split()
    for word in word_list:
        words.append(word)

# Generate Bigram words
bigram_words = {}

for word1, word2 in ngrams(words, 2):
    if word1 not in bigram_words:
        bigram_words[word1] = []
    bigram_words[word1].append(word2)

# Function to generate a ghazal verse using a model
def generate_ghazal_verse(model, length_range):
    verse = []
    length = random.randint(length_range[0], length_range[1])
    
    while length > 0:
        if not verse:
            # Start with a random word from the poetry list
            current_word = random.choice(words)
        else:
            # Choose the next word based on the bigram words
            next_words = model.get(verse[-1], [])
            if not next_words:
                break
            current_word = random.choice(next_words)
        
        verse.append(current_word)
        length -= 1
    
    return verse

# Function to check if the last word of the verses rhyme
def last_words_rhyme(verses):
    last_word = verses[0][-1]
    for verse in verses[1:]:
        if last_word[-2:] != verse[-1][-2:]:
            return False
    return True

# Generating full ghazal with rhyming stanza 
def generate_complete_ghazal(stanza_count, verses_per_stanza):
    for _ in range(stanza_count):
        while True:
            
            rhyming_verses = []
            for _ in range(verses_per_stanza):
                verse = generate_ghazal_verse(bigram_words, (7, 10))
                rhyming_verses.append(verse)
            
            if last_words_rhyme(rhyming_verses):
                break
        
        for verse in rhyming_verses:
            print(" ".join(verse))
        
        print()  

generate_complete_ghazal(3, 4)
