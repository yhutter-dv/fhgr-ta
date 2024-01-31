import nltk

with open('./verfassung.txt', 'r') as f:
    content = f.read()
default_wt = nltk.word_tokenize
words = default_wt(content)
print(f"Got {len(words)} words")
