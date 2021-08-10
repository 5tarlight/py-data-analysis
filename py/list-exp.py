strings = ['a', 'as', 'bat', 'car', 'dove', 'python']
print([x.upper() for x in strings if len(x) > 2])
print({len(x) for x in strings})

all_data = [['John', 'Emily', 'Michael', 'Mary', 'Steven'],
            ['Maria', 'Jaun', 'Javier', 'Natalia', 'Pilar']]
print([name for names in all_data for name in names if name.count('e') >= 2])

some_tuples = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
print([x for tup in some_tuples for x in tup])
print([[x for x in tup] for tup in some_tuples])
