import nltk

with open('./verfassung.txt', 'r') as f:
    content = f.read()

default_st = nltk.sent_tokenize
sentences_default_st = default_st(text=content)
print(f"Got {len(sentences_default_st)} sentences")