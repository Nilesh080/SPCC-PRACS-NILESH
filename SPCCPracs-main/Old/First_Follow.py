def first_and_follow(rules, is_nonterminal):
    def union(first, begins):
        n = len(first)
        first |= begins
        return len(first) != n
    def update_set(target_set, source_set):
        for symbol in source_set:
            if is_nonterminal(symbol):
                target_set.add(symbol)
    nonterminals = set(nt for nt, _ in rules)
    terminals = set(
        symbol
        for _, expression in rules
        for symbol in expression
        if not is_nonterminal(symbol)
    )
    start_symbol = rules[0][0]
    first = {i: set() for i in nonterminals}
    first.update((i, {i}) for i in terminals)
    follow = {i: set() for i in nonterminals}
    epsilon = set()
    while True:
        updated = False
        for nt, expression in rules:
            for symbol in expression:
                updated |= union(first[nt], first[symbol])
                if symbol not in epsilon:
                    break
            else:
                updated |= union(epsilon, {nt})
            aux = follow[nt]
            for symbol in reversed(expression):
                if symbol in follow:
                    updated |= union(follow[symbol], aux)
                if symbol in epsilon:
                    update_set(aux, first[symbol])
                else:
                    aux = first[symbol]
        if not updated:
            break
    follow[start_symbol].add('$')
    return first, follow, epsilon

grammar_rules = [
    ('^', ['a', 'A', 'd']),
    ('A', ['c', 'd'])
]
def is_nonterminal(symbol):
    return symbol.isalpha() and symbol.isupper()
first, follow, epsilon = first_and_follow(grammar_rules, is_nonterminal)
print("First Sets:")
for non_terminal, first_set in first.items():
    print(f"FIRST({non_terminal}) = {first_set}")
print("\nFollow Sets:")
for non_terminal, follow_set in follow.items():
    print(f"FOLLOW({non_terminal}) = {follow_set}")