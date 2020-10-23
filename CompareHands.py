from TieBreaker import TieBreaker

# NOTE: one pair, two pair, three of a kind, four of a kind and full house can be combined into one method
class CompareHands:
    def __init__(self):
        self.p1_pairList = []
        self.p2_pairList = []
        self.p1_aKindTuple = ()
        self.p2_aKindTuple = ()
        self.p1_fullHouse = False
        self.p2_fullHouse = False
        self.p1_flushStraight = -1
        self.p2_flushStraight = -1
        self.p1_score = 0
        self.p2_score = 0

    # Compares p1 and p2 and return -1 if p1 is winner, 1 if p2 is winner and 0 if it is a tie
    def compare(self, p1, p2):
        # Initializing the score with 0, this will change when a ranked hand occurs (one pair, two pair , etc)
        self.p1_score = 0
        self.p2_score = 0

        # Sort the player 1 and player 2 hands by the value of the card
        p1.sort(key = lambda x: x[0])
        p2.sort(key = lambda x: x[0])
        
        ################### One pair or two pair hand calculation ###################
        # Find if any of the hand has a pair (one pair or two pair)
        self.p1_pairList = self._checkPair(p1)
        self.p2_pairList = self._checkPair(p2)

        # If there is a pair in player 1's hand
        if len(self.p1_pairList) > 0:
            # If one pair
            if len(self.p1_pairList) == 1:
                self.p1_score = 1
            # If two pair
            elif len(self.p1_pairList) == 2:
                self.p1_score = 2
        
        # If there is a pair in player 2's hand
        if len(self.p2_pairList) > 0:
            # If one pair
            if len(self.p2_pairList) == 1:
                self.p2_score = 1
            # If two pair
            elif len(self.p2_pairList) == 2:
                self.p2_score = 2

        ################### Three of a kind or Four of a kind hand calculation ###################
        self.p1_aKindTuple = self._check3or4OfAKind(p1)
        self.p2_aKindTuple = self._check3or4OfAKind(p2)

        # Player 1
        # If four of kind list has an element, then the hand is four of a kind and no need to check further
        if self.p1_aKindTuple[1]:
            self.p1_score = 7
        else:
            # If three of kind list has an element, then the hand is three of a kind and edit the score
            if self.p1_aKindTuple[0]:
                self.p1_score = 3
        
        # Player 2
        # If four of kind list has an element, then the hand is four of a kind and no need to check further
        if self.p2_aKindTuple[1]:
            self.p2_score = 7
        else:
            # If three of kind list has an element, then the hand is three of a kind and edit the score
            if self.p2_aKindTuple[0]:
                self.p2_score = 3

        ################### Full house hand calculation ###################
        self.p1_fullHouse = self._checkFullHouse(p1)
        self.p2_fullHouse = self._checkFullHouse(p2)

        if self.p1_fullHouse[0] and self.p1_score < 6:
            self.p1_score = 6
        
        if self.p2_fullHouse[0] and self.p2_score < 6:
            self.p2_score = 6

        ################### Straight, Flush and Straight flush hand calculation ###################
        self.p1_flushStraight = self._checkFlushStraight(p1)
        self.p2_flushStraight = self._checkFlushStraight(p2)

        # Player 1
        # Straight flush
        if self.p1_flushStraight == 2:
            self.p1_score = 8
        # Straight
        elif self.p1_flushStraight == 1:
            if self.p1_score < 4:
                self.p1_score = 4
        # Flush
        elif self.p1_flushStraight == 0:
            if self.p1_score < 5:
                self.p1_score = 5
        
        # Player 2
        # Straight flush
        if self.p2_flushStraight == 2:
            self.p2_score = 8
        # Straight
        elif self.p2_flushStraight == 1:
            if self.p2_score < 4:
                self.p2_score = 4
        # Flush
        elif self.p2_flushStraight == 0:
            if self.p2_score < 5:
                self.p2_score = 5


        # If both the players have same scored hand (a ranked hand or no ranked hand)
        if self.p1_score == self.p2_score:
            tie = TieBreaker(self.p1_pairList, self.p2_pairList, self.p1_aKindTuple, self.p2_aKindTuple)
            return tie.tieBreaker(p1, p2, self.p1_score)
        else:
            if self.p1_score > self.p2_score:
                return -1
            else:
                return 1

    # Checks the occurance of pairs. It will return a list of numbers that were a pair in the original hand
    # Example - if hand had two 4's (of any suit) then the method will return a list with one entry -> [4] 
    # NOTE: hand is a tuple of (value, suit)
    def _checkPair(self, hand):
        seen = set()
        seen_twice = set()
        
        # For all the cards in the hand
        for num, suit in hand:
            # If a number is already seen before then it has repeated and we put it in seen_twice set
            if num in seen:
                seen_twice.add(num)
            # If a number was seen for first time then it is added to the seen set
            else:
                seen.add(num)
        
        # Convert the set to list and return
        return sorted(list(seen_twice), reverse=True)

    # Checks the occurance of (three or four) of a kind. 
    # It will return a tuple of list of numbers that occured thrice and four times in the original hand
    # If no card occur thrice or four times in a hand then tuple will have empty lists
    # Example - if hand had three 4's (of any suit) then the method will return a tuple of lists -> ([4], [])
    # If hand had four 4's, then the method will return a tuple of lists -> ([4], [4]) 
    # NOTE: hand is a tuple of (value, suit)
    def _check3or4OfAKind(self, hand):
        seen = set()
        seen_twice = set()
        seen_thrice = set()
        seen_four = set()

        # For all the cards in the hand
        for num, suit in hand:
            # If a number is seen thrice before then it should be added to seen_four set (four of a kind)
            if num in seen_thrice:
                seen_four.add(num)
            # If a number is seen twice before then it should be added to seen_thrice set (three of a kind)
            elif num in seen_twice:
                seen_thrice.add(num)
            # If a number is already seen before then it has repeated and we put it in seen_twice set
            elif num in seen:
                seen_twice.add(num)
            # If a number was seen for first time then it is added to the seen set
            else:
                seen.add(num)

        # Convert the set to list and return
        return (list(seen_thrice), list(seen_four))

    # Checks if its a full house. Return True if it is, else False
    # Uses already built method for checking pairs and three of a kind
    def _checkFullHouse(self, hand):
        pair_list = self._checkPair(hand)
        aKindTuple = self._check3or4OfAKind(hand)
        # If there is a pair and a three of kind then it is full house
        # We check if there are 2 pairs because three of a kind in itself is a pair, 
        # so there should be 2 pairs and there should be one value that has repeated thrice
        if len(pair_list) == 2 and aKindTuple[0]:
            return (True, aKindTuple, pair_list)
        else:
            return (False, aKindTuple, pair_list)

    # Checks if the hand is a flush, a straight or straight flush
    def _checkFlushStraight(self, hand):
        # Check straight
        straight = True
        for i in range(len(hand)):
            if i > 0:
                if hand[i][0] != (hand[i-1][0] - 1):
                    straight = False
                    break
        
        # Check flush
        flush = False
        seen_suit = set(suit for num, suit in hand)
        if len(list(seen_suit)) == 1:
            flush = True
        else:
            flush = False

        # Check straight flush
        straight_flush = False
        if straight and flush:
            straight_flush = True
        else:
            straight_flush = False

        # If the hand is a straight flush, then return 2.
        # If the hand is a straight, then return 1
        # If the hand is a flush, then return 0
        # If the hand is none of the above three, then return -1
        if straight_flush:
            return 2
        elif straight:
            return 1
        elif flush:
            return 0
        else:
            return -1
