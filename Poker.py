import random
suits = ["♠", "♥", "♦", "♣"]
ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]


class Card(object):
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def __lt__(self, other):
        return ranks.index(self.get_rank()) < ranks.index(other.get_rank())

    def __str__(self):
        return "%s%s" % (self.rank, self.suit)


class Deck(object):
    def __init__(self):
        self.cards = []
        for s in suits:
            for r in ranks:
                self.cards.append(Card(s, r))

    def shuffle(self):
        random.shuffle(self.cards)

    def __str__(self):
        deck = ""
        for i in range(0, 52):
            deck += str(self.cards[i]) + " "
        return deck

    def take_one(self):
        return self.cards.pop(0)


class Hand(object):
    def __init__(self, deck):
        self.cards = []
        for i in range(5):
            self.cards.append(deck.take_one())

    def __str__(self):
        hand = ""
        for i in range(5):
            hand += str(self.cards[i]) + " "
        return hand


    def is_flush(self):
        for i in range (1, 5):
            if self.cards[i].get_suit() != self.cards[0].get_suit():
                return False

        return True

    def is_poker(self):
        self.cards.sort()
        if self.cards[0].get_rank() == self.cards[1].get_rank() == self.cards[2].get_rank() == self.cards[3].get_rank() or \
                self.cards[1].get_rank() == self.cards[2].get_rank() == self.cards[3].get_rank() == self.cards[4].get_rank():
            return True
        return False

    def is_double_pair(self):
        self.cards.sort()
        if self.cards[0].get_rank() == self.cards[1].get_rank():
            if self.cards[2].get_rank() == self.cards[3].get_rank() or\
                self.cards[3].get_rank() == self.cards[4].get_rank():
                return True
        elif self.cards[2].get_rank() == self.cards[3].get_rank() and\
                self.cards[3].get_rank() == self.cards[4].get_rank():
            return True
        return False

    def is_full(self):
        self.cards.sort()
        if self.cards[0].get_rank() == self.cards[1].get_rank() and\
                self.cards[2].get_rank() == self.cards[3].get_rank() == self.cards[4].get_rank():
            return True
        if self.cards[3].get_rank() == self.cards[4].get_rank() and\
                self.cards[0].get_rank() == self.cards[1].get_rank() == self.cards[2].get_rank():
            return True
        return False

    def is_trio(self):
        for i in range (5):
            for j in range (i+1, 5):
                if self.cards[i].get_rank() == self.cards[j].get_rank():
                    for k in range (j+1, 5):
                        if self.cards[i].get_rank() == self.cards[k].get_rank():
                            return True
        return False

    def is_pair(self):
        for i in range(5):
            for j in range(i+1, 5):
                if self.cards[i].get_rank() == self.cards[j].get_rank():
                    return True
        return False

    def is_straight(self):
        self.cards.sort()
        if self.cards[0].get_rank() == '2' and \
                self.cards[1].get_rank() == '3' and \
                self.cards[2].get_rank() == '4' and \
                self.cards[3].get_rank() == '5' and \
                self.cards[4].get_rank() == 'A':
            return True

        for i in range(4):
            if ranks.index(self.cards[i].get_rank()) +1 != ranks.index(self.cards[i+1].get_rank()):
                return False

        return True

    def is_straight_flush(self):
        if self.is_flush() and self.is_straight():
            return True
        return False

    def is_high_card(self):
        self.cards.sort(reverse=True)
        return True, print('high card is', self.cards[0])

    def is_royal_flush(self):
        self.cards.sort()
        if self.is_straight_flush() and self.cards[0].get_rank() == '10':
            return True
        return False


royal=0
for i in range(1000000):
    new_deck = Deck()
    new_deck.shuffle()
    hand= Hand(new_deck)
    if hand.is_royal_flush():
        print(hand)
        print("is flush")
        royal+=1
    elif hand.is_straight_flush():
        print(hand)
        print("is flush")
        royal+=1
    elif hand.is_straight():
        print(hand)
        print("is flush")
        royal+=1
    elif hand.is_flush():
        print(hand)
        print("is flush")
        royal+=1
    elif hand.is_full():
        print(hand)
        print("is flush")
        royal+=1
    elif hand.is_double_pair():
        print(hand)
        print("is flush")
        royal+=1
    elif hand.is_poker():
        print(hand)
        print("is flush")
        royal += 1
    elif hand.is_trio():
        print(hand)
        print("is flush")
        royal+=1
    elif hand.is_pair():
        print(hand)
        print("is flush")
        royal+=1
    else:
        hand.is_high_card()


print(royal/10000)