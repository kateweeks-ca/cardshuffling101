#code to make the deck
values = ['2','3','4','5','6','7','8','9','10','Jack','Queen','King','Ace']
suites = ['Hearts', 'Clubs', 'Diamonds', 'Spades']
deck = [[s,v] for s in suites for v in values]

#check length of deck
len(deck)

#calculate total number of shuffles in a deck
import numpy as np
np.math.factorial(52)

#choose a random integer to divide the packets
import random
k = random.randint(16,36)
k


#example of a perfect shuffle
h1 = [1, 2, 3]
h2 = [4, 5, 6]
h3 = [h1[0], h2[0], h1[1], h2[1], h1[2], h2[2]]
h3

#create the function to shuffle the deck
def riffle(deck):
    from random import randint
    import random
    k = random.randint(16,36)
    first_deck, second_deck = deck[:k], deck[k:]
    n =  randint(0,1)
    for i in range(0, len(second_deck)):
        first_deck.insert(n, second_deck[i])
        n =  n + (randint(0,2))
        
    return first_deck

# Riffle the deck 7 times
def seven_riffles(deck)
	shuffled = deck.copy()
	for i in range(0,7):
		shuffled = riffle(shuffled)
		

#calculate the probability of guessing correct cards in a deck
n = 52
corr_prob = 0
for i in range(0, 52):
    corr_prob = corr_prob + (1/n)
    n = n - 1
corr_prob 


#create a card guessing function
def card_guesser(seventh_riffle, deck):
    deckp = deck.copy()
    correct = 0 
    for i in range(0, len(seventh_riffle)):
        
        top_card = seventh_riffle[i]
        from random import randint
        guess = randint(0, len(deckp)-1)
        if seventh_riffle[i] == deckp[guess]:
            correct = correct + 1
            del(deckp[guess])
        else:
            
            deckp.remove(top_card)
    return correct
    

#guess the cards
correct_guesses = card_guesser(seventh_riffle, deck)

#test the card guesser on our riffled deck
def correct_avg(seventh_riffle, deck):
    c_avg = np.zeros(10000)
    for i in range(0,10000):
        c_avg[i] = card_guesser(seventh_riffle, deck)
    return np.mean(c_avg)


#perfect shuffle function
def perfect_riffle(deck):
    import random
    k =26
    first_deck, second_deck = deck[:k], deck[k:]
    n = 1
    for i in range(0, 26):
        
        first_deck.insert(n, second_deck[i])
        n = 2 + n
    return first_deck

#shuffle a deck perfect eight times
deck eight_perfect_riffle(deck):
	shuffled = deck.copy()
	for i in range(0,8):
		shuffled = perfect_riffle(deck)

#check it matches 
deck8 = eight_perfect_riffle
deck8 === deck

