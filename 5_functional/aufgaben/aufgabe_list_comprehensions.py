"""
Schreibe als List Comprehension
"""

seq = [1, 2, 3, 8, 12, 4, 89]

# 1. Aufgabe
new_seq = []
for element in seq:
    new_seq.append(element)

print(new_seq)

# 2. Aufgabe
new_seq = []
for element in seq:
    if element > 4:
        new_seq.append(element)

print(new_seq)


# 3. Aufgabe
new_seq = []
for index, element in enumerate(seq):
    new_seq.append((index, element))

print(new_seq)
