full = {'grenadier': 'infantry', 'spearman': 'infantry'}
full['hussar'] = 'cavalry'
print(full)
print(' ')
print(full['hussar'])
del full['spearman']
full['brass-cannon'] = 'artillery'
print(full)
print(full['brass-cannon'])
print(' ')
print(list(full))
print(' ')
print(sorted(full))
print('grenadier' in full)
print('marine' in full)
