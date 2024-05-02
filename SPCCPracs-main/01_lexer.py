KEYWORDS = ["int", "return"]
OPERATORS = ["+", "-", "*", "/", "="]
PUNCTUATORS = ["(", ")", "{", "}", ",", ";"]

tokens = []
tokensFound = []
numbersFound = []
keywordsFound = []
punctuationsFound = []
operatorsFound = []
identifiersFound = []

def lexer(fileName):
  with open(fileName) as f:
    lines = f.readlines()
    for line in lines:
      tokens.extend(line.split())
    for token in tokens:
      tokensFound.append(token)
    for token in tokens.copy():
      if token in KEYWORDS:
        keywordsFound.append(token)
        tokens.remove(token)
      elif token in PUNCTUATORS:
        punctuationsFound.append(token)
        tokens.remove(token)
      elif token in OPERATORS:
        operatorsFound.append(token)
        tokens.remove(token)
      else:
        identifiersFound.append(token)
        tokens.remove(token)
    print(f"\nTokens found: {len(set(tokensFound))}, Tokens: {set(tokensFound)}")
    print(f"\nKeywords found: {len(set(keywordsFound))}, Keywords: {set(keywordsFound)}")
    print(f"\nPunctuators found: {len(set(punctuationsFound))}, Punctuators: {set(punctuationsFound)}")
    print(f"\nOperators found: {len(set(operatorsFound))}, Operators: {set(operatorsFound)}")
    print(f"\nIdentifiers found: {len(set(identifiersFound))}, Identifiers: {set(identifiersFound)}")

fileName = input("Enter the name of the file to perform lexical analysis on: ")
lexer(fileName)