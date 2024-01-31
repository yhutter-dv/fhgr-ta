import nltk

with open('./verfassung.txt', 'r') as f:
    content = f.read()
default_wt = nltk.word_tokenize
words = default_wt(content)
print(words[:10])
print(f"Got {len(words)} words with default word tokenizer")

TOKEN_PATTERN = r'\w+'        
regex_wt = nltk.RegexpTokenizer(pattern=TOKEN_PATTERN,
                                gaps=False)  # hier suchen wir nach den Wörtern
words = regex_wt.tokenize(content)
print(words[:10])
print(f"Got {len(words)} words with regex word tokenizer")
