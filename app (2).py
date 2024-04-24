  
import nltk
nltk.download('punkt')
from nltk.corpus import stopwords
from collections import Counter

# Read the file
with open('random_paragraphs.txt', 'r') as file:
    text = file.read()

# Tokenize the text into individual words
words = nltk.word_tokenize(text)

# Remove stop words
stop_words = set(stopwords.words('english'))
filtered_words = [word for word in words if word.lower() not in stop_words]

# Count the frequency of each word
word_freq = Counter(filtered_words)

# Display word frequency count
for word, freq in word_freq.items():
    print(f'{word}: {freq}')