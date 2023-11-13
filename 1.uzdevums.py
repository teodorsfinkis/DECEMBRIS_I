'''
Izveidojiet Python programmu, kas saskaita no 1 līdz lietotāja ievadītam skaitlim, izmantojot for ciklu.
'''

# skaitīt no skaitlim 1 līdz skaitlim x
def summa(n):
    sum = 0
    for i in range(1, n + 1):
        sum += i
    return sum

# vārds
user_input = input("Ievadi skaitli līdz kuram vēlies saskaitīt: ")
user_input = int(user_input)


result = summa(user_input)

# izdrukā summu
print("Summa no 1 līdz", user_input, "ir", result)