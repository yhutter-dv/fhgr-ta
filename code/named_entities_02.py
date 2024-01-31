from nltk.corpus import gutenberg
import re
from collections import Counter
import nltk

def prepare() -> list:
    bible = gutenberg.open('bible-kjv.txt')
    bible = bible.readlines()

    # Remove new lines
    bible = list(filter(None, [item.strip('\n') for item in bible]))
    tokens = [item.split() for item in bible]

    # Currently the tokens have nested lists. Merge those lists into a single one containing all the words
    words = [word for sentence in tokens for word in sentence]

    # Mark those words that follow after the end of a sentence as None
    for index, word in enumerate(words):
        if word == None:
            continue
        if word[-1] == '.':
            words[index + 1] = None

    # Only keep alpha characters and remove the rest
    words = list(filter(None, [re.sub(r'[^A-Za-z]', '', word) for word in words if word]))

    # Remove any word that is a stop word.
    stopwords = nltk.corpus.stopwords.words('english')
    words = [word for word in words if word.lower() not in stopwords]

    return words


"""
Als einfache Erweiterung sollen nun nur grossgeschriebene Wörter gefiltert werden, die nicht am Satzanfang stehen. Diese wieder speichern und zählen.

Bestehen noch weitere Probleme mit diesem Ansatz?
"""

"""
Das Problem bei diesem Ansatz ist dass 
 - Auch nach Fragen gross geschrieben wird
 - Zitate auch problematisch sind: Person A sagte: "Es werde..."
 - In dieser Bibel die Zitate mit einem ";" eingeleitet werden
"""
words = prepare()

upper_case_pattern = r'[A-Z][a-z]+'
upper_case_words = [word for word in words if re.match(upper_case_pattern, word)] 
#upper_case_words = [word for word in words if word.istitle()] 
c = Counter(upper_case_words)
print(c.most_common(10))
