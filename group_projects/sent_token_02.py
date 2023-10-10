import nltk

with open('./verfassung.txt', 'r') as f:
    content = f.read()

# Remove new lines and other stuff
content.replace("\r\n", "").replace("\n", "")
content.replace("  ", "")
default_st = nltk.sent_tokenize
sentences_default_st = default_st(text=content)
print(f"Got {len(sentences_default_st)} sentences with default tokenizer")

SENTENCE_TOKENS_PATTERN = r'w\.'
regex_st = nltk.tokenize.RegexpTokenizer(
            pattern=SENTENCE_TOKENS_PATTERN,
            gaps=True) 
sample_sentences = regex_st.tokenize(content)
print(f"Got {len(sentences_default_st)} sentences with regex tokenizer")
