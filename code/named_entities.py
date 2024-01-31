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

    # Only keep alpha characters and remove the rest
    words = list(filter(None, [re.sub(r'[^A-Za-z]', '', word) for word in words]))

    # Remove any word that is a stop word.
    stopwords = nltk.corpus.stopwords.words('english')
    words = [word for word in words if word.lower() not in stopwords]

    return words


"""
Eine wichtige Aufgabe im NLP ist die Erkennung von sogenannten "Named Entities". Wir kommen später im Semester noch ausführlicher dazu, wollen uns aber schon einmal an einer einfachen Variante probieren.

Im Englischen werden Namen gross geschrieben. Suchen sie deshalb im Korpus nach grossgeschriebenen Wörtern. Zählen sie diese wie im Beispiel und geben sie die häufigsten Wörter aus.

Welche Probleme ergeben sich mit diesem Ansatz?
"""

"""
Das Problem bei diesem Ansatz ist dass 
 - Nach einem Punkt (Satzende) grossgeschrieben wird
 - Zitate auch problematisch sind: Person A sagte: "Es werde..."
"""
words = prepare()

upper_case_pattern = r'[A-Z][a-z]+'
upper_case_words = [word for word in words if re.match(upper_case_pattern, word)] 
#upper_case_words = [word for word in words if word.istitle()] 
c = Counter(upper_case_words)
print(c.most_common(10))
