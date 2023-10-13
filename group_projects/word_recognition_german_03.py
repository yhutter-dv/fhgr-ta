import spacy
import nltk
import random
from nltk.tag import DefaultTagger
from nltk.tag import UnigramTagger
from nltk.tag import BigramTagger
from nltk.tag import TrigramTagger

def combined_tagger(train_data, taggers, backoff=None):
    for tagger in taggers:
        backoff = tagger(train_data, backoff=backoff)
    return backoff


path = "./"
file = "tiger_release_aug07.corrected.16012013.conll09"
corp = nltk.corpus.ConllCorpusReader(path, file, ['ignore', 'words', 'ignore', 'ignore', 'pos'], encoding='utf-8')

tagged_sents = list(corp.tagged_sents())
random.shuffle(tagged_sents)

# use 90% for training, 10% for testing
split_perc = 0.1
split_size = int(len(tagged_sents) * split_perc)
train_data, test_data = tagged_sents[split_size:], tagged_sents[:split_size]

dt = DefaultTagger('NN')
t = UnigramTagger(train_data)
bt = BigramTagger(train_data)
tt = TrigramTagger(train_data)
ct = combined_tagger(train_data=train_data,
                     taggers=[UnigramTagger, BigramTagger, TrigramTagger],
                     backoff=dt)

sentence = "Der braune Fuchs springt über den faulen Hund."
nlp = spacy.load("de_dep_news_trf")
sentence_nlp = nlp(sentence)
spacy_pos_tagged = [(word, word.tag_, word.pos_) for word in sentence_nlp]

print("Spacy POS Tagging Result")
print("=" * len("Spacy POS Tagging Result"))
print(spacy_pos_tagged)
print("Combined POS Taggin Result")
print("=" * len("Combined POS Tagging Result"))
print(ct.tag(nltk.word_tokenize(sentence)))
