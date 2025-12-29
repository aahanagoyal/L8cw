t=input(("Enter a sentence to find a prominant word: "))
t=t.split()
Bigword=0

for wrd in t:
    lenW = len(wrd)
    if lenW>Bigword:
        Bigword=lenW
for wrd in t:
    lenW = len(wrd)
    if lenW==Bigword:
        print("Largest word:",wrd)