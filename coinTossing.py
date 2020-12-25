import random



coin = ["heads","tails"]

toss = random.choice(coin)

selection =input("heads or tails : ")

if selection == toss:
    print("yout win! the coin landed on " + toss)

else:
    print("you lose! the coin landed on " + toss)
