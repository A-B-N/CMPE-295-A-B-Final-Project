# How can we use a formal grammar to describe the structure of an unlimited set of sentences?
# How do we represent the structure of sentences using syntax trees?
# How do parsers analyze a sentence and automatically build a syntax tree?

# Natural Language Toolkit:
import nltk as nltk
# grammar1 = nltk.data.load('file:mygrammar.cfg')

# writing my own grammar
grammar = nltk.CFG.fromstring("""
 S -> NP VP
 PP -> P NP
 NP -> Det N | Det N PP | 'I' | 'Mary' | 'Bob'
 VP -> V NP | VP PP

 Det -> 'an' | 'my' | 'the'
 N -> 'elephant' | 'pajamas' | 'house' | 'juice'
 V -> 'shot' | 'likes'
 P -> 'in'
 """)

# sample of sentences
sent = ['I', 'shot', 'an', 'elephant', 'in', 'my', 'pajamas']
sent2 = "I killed a dragon in her costume".split()
sent3 = "Mary likes the juice in the house".split()

# parsing the sentences

# parser = nltk.ChartParser(grammar)
# for tree in parser.parse(sent2):
#     print(tree)

rd_parser = nltk.RecursiveDescentParser(grammar)
for tree in rd_parser.parse(sent3):
    print(tree)

# for p in grammar.productions(): print(p)