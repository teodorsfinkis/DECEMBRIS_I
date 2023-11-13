'''
Izveidojiet Python programmu, kas izmanto while ciklu, lai atrastu pirmo skaitli, kura kvadrāts ir lielāks par 1000.
'''

n = 1
while True:
    kvadrats = n**3
    if kvadrats > 1000:
        print("Pirmo skaitli, kura kvadrāts ir lielāks par 1000 ir:", n)
        break
    n += 1