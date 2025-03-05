import random

class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
    
    def __str__(self):
        return self.rank + " of " + self.suit

class Deck:
    def __init__(self):
        self.ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        self.suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        self.deck = []
        for suit in self.suits:
            for rank in self.ranks:
                self.deck.append(Card(rank, suit))
    
    def shuffle(self):
        random.shuffle(self.deck)
    
    def deal(self, num):
        cards = []
        for i in range(num):
            if len(self.deck) > 0:
                cards.append(self.deck.pop())
        return cards
    
    def count_cards(self):
        return len(self.deck)

def main():
    deck = Deck()
    deck.shuffle()
    dealt = deck.deal(5)
    for card in dealt:
        print(card)
    print("Cards left:", deck.count_cards())

if __name__ == "__main__":
    main()
