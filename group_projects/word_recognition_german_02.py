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
ut = UnigramTagger(train_data)
bt = BigramTagger(train_data)
tt = TrigramTagger(train_data)
ct = combined_tagger(train_data=train_data,
                     taggers=[UnigramTagger, BigramTagger, TrigramTagger],
                     backoff=dt)

print(f"Accuracy of Default Tagger is {dt.accuracy(gold=test_data)}")
print(f"Accuracy of Unigram Tagger is {ut.accuracy(test_data)}")
print(f"Accuracy of Bigram Tagger is {bt.accuracy(test_data)}")
print(f"Accuracy of Trigram Tagger is {tt.accuracy(test_data)}")
print(f"Accuracy of Combined Tagger is {ct.accuracy(test_data)}")
