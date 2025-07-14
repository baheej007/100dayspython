import random
words=["messi","ronaldo","dimaria","martinez","neymar","mbappe","tevez"]
word=random.choice(words)
s=""
for i in range(len(word)):
    s+="_"
print(word)
guess=str(input(s+"\nGuess a letter:  ")).lower()

for p,letter in enumerate(word):
    if letter==guess:
       s.replace("_",letter,1)
print(s)









