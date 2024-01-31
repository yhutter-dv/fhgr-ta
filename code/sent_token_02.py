import nltk

with open('./verfassung.txt', 'r') as f:
    content = f.read()

# Remove new lines and other stuff
content = content.replace("  ", "").replace("\n", "")
default_st = nltk.sent_tokenize
sentences_default_st = default_st(text=content)
print(f"Got {len(sentences_default_st)} sentences with default tokenizer")
print(sentences_default_st[:5])

SENTENCE_TOKENS_PATTERN = r'[a-zA-Z]\.|\d{4}\.'
regex_st = nltk.tokenize.RegexpTokenizer(
            pattern=SENTENCE_TOKENS_PATTERN,
            discard_empty = False,
            gaps=True) 
sentences_regex_st = regex_st.tokenize(content)
print(f"Got {len(sentences_regex_st)} sentences with regex tokenizer")
print(sentences_regex_st[:5])
