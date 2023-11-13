'''
Izveidojiet Python programmu, kas atkarībā no pašreizējās stundas izvada atbilstošu sveicienu, izmantojot if priekšrakstu. (labrīt, labdien, labvakar)
'''

from datetime import datetime

# funkcija
def sveiciens(hour):
    if 4 <= hour < 12:
        return "Labrīt!"
    elif 12 <= hour < 18:
        return "Labdien!"
    elif 18 <= hour < 22:
        return "Labvakar!"
    else:
        return "Labsakiet!"

# Iegūstiet pašreizējo stundu
now = datetime.now()
current_hour = now.hour

# Ievada atbilstošu sveicienu
print(sveiciens(current_hour))