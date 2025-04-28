import os
import re
import nltk
from collections import Counter
from nltk.corpus import stopwords
from nltk import pos_tag, word_tokenize

# Download necessary NLTK resources if not already present
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('averaged_perceptron_tagger')


def is_not_adjective(word, tag):
    """Return True if the POS tag is not an adjective."""
    return not tag.startswith('JJ')


def get_words_from_file(filepath):
    """Extract words from a text file."""
    with open(filepath, 'r', encoding='utf-8') as file:
        text = file.read()
    # Remove non-alphabetical characters and tokenize
    words = word_tokenize(re.sub(r'[^a-zA-Z\s]', '', text))
    return words


def main():
    # Prepare stop words
    stop_words = set(stopwords.words('english'))

    # Get all .txt files in current directory
    txt_files = [f for f in os.listdir('.') if f.endswith('.txt')]

    total_words = []

    for file in txt_files:
        words = get_words_from_file(file)
        # Lowercase and filter stopwords
        words = [word.lower()
                 for word in words if word.lower() not in stop_words]
        # POS tagging
        tagged_words = pos_tag(words)
        # Keep only non-adjectives
        filtered_words = [word for word,
                          tag in tagged_words if is_not_adjective(word, tag)]
        total_words.extend(filtered_words)

    # Count word frequencies
    word_counts = Counter(total_words)

    # Print the 10 most common words
    print("Most common words (excluding stop words and adjectives):")
    for word, count in word_counts.most_common(1000):
        print(f"{word}: {count}")


if __name__ == '__main__':
    main()
