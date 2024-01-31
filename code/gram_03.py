import nltk


grammar = nltk.CFG.fromstring("""
	S -> NP | NP VP | NP VP NP | NP VP PP
	NP -> DET ADJ N PP | DET N | DET ADJ N 
	VP -> V
	PP -> PREP NP
	N -> 'fox' | 'dog' | 'cat' | 'box' | 'frog' | 'fly' | 'car'
	DET -> 'the' | 'a' | 'which'
	ADJ -> 'quick' | 'brown' | 'lazy' | 'tall' | 'slow' | 'big' | 'peacefully' | 'warm'
	V -> 'is' | 'jumping' | 'running' | 'eats' | 'jumps' | 'sleeps'
	PREP -> 'in' | 'over' | 'on'
""")

sentences = ["the brown fox in a box", "a lazy cat", "the box", "the slow frog eats a big fly", "the brown fox jumps over the lazy cat"]
for sentence in sentences:
	print(f"Sentence is '{sentence}'")
	words = sentence.split()
	my_parser = nltk.RecursiveDescentParser(grammar) # (grammar, trace=2) falls keine Ausgabe kommt...
	for tree in my_parser.parse(words):
		print(tree)