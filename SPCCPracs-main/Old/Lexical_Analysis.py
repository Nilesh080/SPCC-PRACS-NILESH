KEYWORDS = ['int', 'return']
PUNCTUATORS = ["(", ")", "{", "}", ";"]
OPERATORS = ["+", "="]

keywordsFound = []
punctuatorsFound = []
operatorsFound = []
allTokens = []
tokens = []
identifiersFound = []

def lexer(fileName):
	with open(fileName) as f:
		lines = f.readlines()
		for line in lines:
			tokens.extend(line.split())
	for token in tokens.copy():
		allTokens.append(token)
		if token in KEYWORDS:
			keywordsFound.append(token)
			tokens.remove(token)
		elif token in PUNCTUATORS:
			punctuatorsFound.append(token)
			tokens.remove(token)
		elif token in OPERATORS:
			operatorsFound.append(token)
			tokens.remove(token)
		else:
			identifiersFound.append(token)
			tokens.remove(token)
	print(f"No. of tokens found: {len(allTokens)}, Tokens: {set(allTokens)}")
	print(f"No. of Keywords found: {len(set(keywordsFound))}, Keywords: {set(keywordsFound)}")
	print(f"No. of Punctuations found: {len(set(punctuatorsFound))}, Punctuations: {set(punctuatorsFound)}")
	print(f"No. of Identifiers found: {len(set(identifiersFound))}, Identifiers: {set(identifiersFound)}")


fileName = input("Enter the name of the file: ")
lexer(fileName)