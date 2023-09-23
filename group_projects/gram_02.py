import nltk


grammar = nltk.CFG.fromstring("""
	S -> NP | NP VP
	NP -> DET ADJ N PP | DET N | DET ADJ N
	VP -> V
	PP -> PREP NP
	N -> 'fox' | 'dog' | 'cat' | 'box'
	DET -> 'the' | 'a'
	ADJ -> 'quick' | 'brown' | 'lazy' | 'tall'
	V -> 'is' | 'jumping' | 'running'
	PREP -> 'in'
""")

sentences = ["the brown fox in a box", "a lazy cat", "the box"]
for sentence in sentences:
	print(f"Sentence is '{sentence}'")
	words = sentence.split()
	my_parser = nltk.RecursiveDescentParser(grammar) # (grammar, trace=2) falls keine Ausgabe kommt...
	for tree in my_parser.parse(words):
		print(tree)