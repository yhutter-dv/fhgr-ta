import nltk


grammar = nltk.CFG.fromstring("""
S -> PS | PS CONJ PS
PS -> NP | NP VP | NP PP | NP PREP NP | NP VP PREP NP
NP -> DET ADJ N PP | DET N | DET ADJ | DET ADJ N | PRON VP
VP -> V | V ADJ | V V
PP -> PREP NP
N -> 'fox' | 'dog' | 'cat' | 'box'
DET -> 'the' | 'a'
ADJ -> 'quick' | 'brown' | 'lazy' | 'tall'
PRON -> 'he'
CONJ -> 'and'
V -> 'is' | 'jumping' | 'running' | jumps
PREP -> 'in' | 'over'
""")

sentences = ["the brown fox in a box", "the brown fox is quick and he is jumping over the lazy dog"]
for sentence in sentences:
	print(f"Sentence is '{sentence}'")
	words = sentence.split()
	my_parser = nltk.RecursiveDescentParser(grammar) # (grammar, trace=2) falls keine Ausgabe kommt...
	for tree in my_parser.parse(words):
		print(tree)