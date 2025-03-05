import random

class CardDealer:
    def __init__(self):
        self.suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        self.ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
        self.deck = [f"{rank} of {suit}" for suit in self.suits for rank in self.ranks]
        random.shuffle(self.deck)

    def deal_cards(self, num_cards):
        if num_cards > len(self.deck):
            print("Not enough cards in the deck!")
            return []
        dealt_cards = self.deck[:num_cards]
        self.deck = self.deck[num_cards:]
        return dealt_cards

    def cards_left(self):
        return len(self.deck)

def main():
    dealer = CardDealer()
    print("Card Dealer\n")
    print("I have shuffled a deck of 52 cards.\n")
    
    num_cards = int(input("How many cards would you like?: "))
    dealt_cards = dealer.deal_cards(num_cards)
    
    if dealt_cards:
        print("\nHere are your cards:")
        for card in dealt_cards:
            print(card)
        print(f"\nThere are {dealer.cards_left()} cards left in the deck.\n")
    
    input("Good luck!\nPress any key to continue . . .")

if __name__ == "__main__":
    main()
