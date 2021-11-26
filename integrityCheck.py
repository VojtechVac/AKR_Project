from chceckSum import CheckSum
from hashSelectsql import hashSelectsql

chSum = CheckSum()
hashTab = hashSelectsql()
p = "chacha"

# v pe je uložené chacha a v hashTab.selectMail je uložené chacha z SQL tabulky -->
# --> pozri hashSelectsql tam je na to kod
# chceckSum jeten ček je funkčný a nám bude nahradene hashTab.select mail


if p == hashTab.selectMail:
    print("INTEGRITY IS OK")
else:
    print("WARNING - FILE WAS CHANGED!!!")