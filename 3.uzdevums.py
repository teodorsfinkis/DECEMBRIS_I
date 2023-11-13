'''
Izveidojiet Python programmu, kas pārbauda, vai ievadītais skaitlis ir nepāra, izmantojot if priekšrakstu.
'''

# nummura ievade
numurs = int(input("Ievadiet skaitli: "))

# pārbaudīšana
if numurs % 2 != 0:
    print("Skaitlis ir nepāra.")
else:
    print("Skaitlis nav nepāra.")
