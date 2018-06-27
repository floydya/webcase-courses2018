import random, sys
quantity = 5
arpr = [
    'my', 'your', 'his','her', 'its', 'our','their', 'mine', 'yours','hers', 'ours', 'the'
]

nouns = [
    'time','year','people','way','day','man','thing','woman','life','child',
    'world','school','state','family','student','group','country','problem','hand','part',
    'place','case','week','company','system','program','question','work','government',
    'number','night','point','home','water'
]

verbs = [
    'be','have','do','say','go','can','get','would','make','know',
    'will','think','take','see','come','could','want','look','use','find',
    'give','tell','work','may','should','call','try','ask','need','feel',
    'become','leave','put','mean','keep'
]

adverbs = [
    'accidentally', 'always', 'angrily', 'anxiously','awkwardly', 'badly', 'blindly', 'boastfully',
    'boldly', 'bravely', 'brightly', 'cheerfully','coyly', 'crazily', 'defiantly', 'deftly',
    'deliberately', 'devotedly', 'doubtfully', 'dramatically','dutifully', 'eagerly', 'elegantly', 'enormously',
    'evenly', 'eventually', 'exactly', 'faithfully','finally', 'foolishly', 'fortunately', 'frequently'
]
try:
    quantity = int(sys.argv[1])
except IndexError:
    print('--- Quantity sets to default(5).')
except ValueError as err:
    print('Enter number in arguments please.')
for i in range(quantity):
    print('{} {} {} {}'.format(random.choice(arpr), random.choice(nouns), random.choice(verbs), random.choice(adverbs)))
