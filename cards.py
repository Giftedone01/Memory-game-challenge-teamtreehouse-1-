class Card:
    def __init__(self, word, location):
        self.card = word
        self.location = location
        self.matched = False
        
        
    def __eq__(self, other):
        return self.card == other.card
      
    def __str__(self):
        return self.card
      
    # add a dunder main to test out our code create 3 instances below dunder main
    #make sure 2 instance is equal by having the same word passed in
if __name__ == '__main__':
    card1 = Card('egg', 'A1')
    card2 = Card('egg', 'B1')
    card3 = Card('hut', 'D4')
  
    # check the above dunder main by printing out comparisons
    print(card1 == card2)
    print(card1 == card3)
    print(card1)