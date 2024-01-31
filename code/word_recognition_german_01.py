import nltk
import random

path = "./"
file = "tiger_release_aug07.corrected.16012013.conll09"
corp = nltk.corpus.ConllCorpusReader(path, file, ['ignore', 'words', 'ignore', 'ignore', 'pos'], encoding='utf-8')


tagged_sents = list(corp.tagged_sents())
random.shuffle(tagged_sents)
# set a split size: use 90% for training, 10% for testing
split_perc = 0.1
split_size = int(len(tagged_sents) * split_perc)
train_data, test_data = tagged_sents[split_size:], tagged_sents[:split_size]
print(train_data[0])