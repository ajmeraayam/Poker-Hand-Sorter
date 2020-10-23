class TieBreaker:
    def __init__(self, p1_pair, p2_pair, p1_aKind, p2_aKind):
        self.p1_pairList = p1_pair
        self.p2_pairList = p2_pair
        self.p1_aKindTuple = p1_aKind
        self.p2_aKindTuple = p2_aKind

    def tieBreaker(self, p1, p2, p1_score):
        # If no ranked hand for both players, then find the high card
        if p1_score == 0:
           return self._findHighCard(p1, p2)
            
        # If ranked hand for both players, then find compare the value of ranked cards.
        else:
            # If both players have one pair
            if p1_score == 1:
                return self._pairTieBreaker(p1, p2)
            
            # If both players have two pair
            elif p1_score == 2:
                return self._twoPairTieBreaker(p1, p2)
                
            # If both players have three of a kind
            elif p1_score == 3:
                return self._threeKindTieBreaker(p1, p2)

            # If both players have straight
            elif p1_score == 4:
                return self._straightTieBreaker(p1, p2)                

            # If both players have flush, then find the high card
            elif p1_score == 5:
                return self._findHighCard(p1, p2)

            # If both players have full house
            elif p1_score == 6:
                return self._fullHouseTieBreaker(p1, p2)

            # If both players have four of a kind
            elif p1_score == 7:
                return self._fourKindTieBreaker(p1, p2)
                
            # If both players have straight flush
            else:
                return self._straightTieBreaker(p1, p2)
    

    def _findHighCard(self, p1, p2):
        # Sort the player 1 and player 2 hands by the decreasing value of the card
        p1.sort(key = lambda x: x[0], reverse=True)
        p2.sort(key = lambda x: x[0], reverse=True)
        for card1, card2 in zip(p1, p2):
            # If player 1 has a higher card
            if card1[0] > card2[0]:
                return -1
            # If player 2 has a higher card
            elif card1[0] < card2[0]:
                return 1
            # If both have same high card, then check next card
            else:
                continue

        # If all cards are same
        return 0

    def _pairTieBreaker(self, p1, p2):
        # Check value of pair cards for both players
        p1_highPair = self.p1_pairList[0]
        p2_highPair = self.p2_pairList[0]

        # If player 1 has higher value in pair
        if p1_highPair > p2_highPair:
            return -1
        # If player 2 has higher value in pair
        elif p1_highPair < p2_highPair:
            return 1
        # If both players have same valued pair
        else:
            p1_copy = [(num, suit) for num, suit in p1 if num != p1_highPair]
            p2_copy = [(num, suit) for num, suit in p2 if num != p2_highPair]
            return self._findHighCard(p1_copy, p2_copy)


    def _twoPairTieBreaker(self, p1, p2):
        p1_highPair = self.p1_pairList[0]
        p2_highPair = self.p2_pairList[0]

        # If player 1 has higher value in pair
        if p1_highPair > p2_highPair:
            return -1
        # If player 2 has higher value in pair
        elif p1_highPair < p2_highPair:
            return 1
        # If both players have same valued first pair
        else:
            p1_secondHighPair = self.p1_pairList[1]
            p2_secondHighPair = self.p2_pairList[1]

            # If player 1 has higher value in second pair
            if p1_secondHighPair > p2_secondHighPair:
                return -1
            # If player 2 has higher value in second pair
            elif p1_secondHighPair < p2_secondHighPair:
                return 1
            else:
                p1_copy = [(num, suit) for num, suit in p1 if (num != p1_highPair and num != p1_secondHighPair)]
                p2_copy = [(num, suit) for num, suit in p2 if (num != p2_highPair and num != p2_secondHighPair)]
                return self._findHighCard(p1_copy, p2_copy)

    
    def _threeKindTieBreaker(self, p1, p2):
        p1_highKind = self.p1_aKindTuple[0][0]
        p2_highKind = self.p2_aKindTuple[0][0]

        # If player 1 has higher value in three of a kind cards
        if p1_highKind > p2_highKind:
            return -1
        # If player 2 has higher value in three of a kind cards
        elif p1_highKind < p2_highKind:
            return 1
        # If both players have same valued card in three of a kind
        else:
            p1_copy = [(num, suit) for num, suit in p1 if num != p1_highKind]
            p2_copy = [(num, suit) for num, suit in p2 if num != p2_highKind]
            return self._findHighCard(p1_copy, p2_copy)

    def _fourKindTieBreaker(self, p1, p2):
        p1_highKind = self.p1_aKindTuple[1][0]
        p2_highKind = self.p2_aKindTuple[1][0]

        # If player 1 has higher value in three of a kind in full house
        if p1_highKind > p2_highKind:
            return -1
        # If player 2 has higher value in three of a kind in full house
        elif p1_highKind < p2_highKind:
            return 1
        # If both players have same valued card in three of a kind in full house
        else:
            p1_copy = [(num, suit) for num, suit in p1 if num != p1_highKind]
            p2_copy = [(num, suit) for num, suit in p2 if num != p2_highKind]
            return self._findHighCard(p1_copy, p2_copy)

    def _straightTieBreaker(self, p1, p2):
        # Sort the player 1 and player 2 hands by the decreasing value of the card
        p1.sort(key = lambda x: x[0], reversed=True)
        p2.sort(key = lambda x: x[0], reversed=True)

        # If the highest card in straight for player 1 has higher value than player 2 highest straight card
        if p1[0][0] > p2[0][0]:
            return -1
        # If the highest card in straight for player 2 has higher value than player 1 highest straight card
        elif p1[0][0] < p2[0][0]:
            return 1
        # If both players have same valued card in three of a kind
        else:
            return 0

    def _fullHouseTieBreaker(self, p1, p2):
        p1_highKind = self.p1_aKindTuple[0][0]
        p2_highKind = self.p2_aKindTuple[0][0]

        # If player 1 has higher value in three of a kind in full house
        if p1_highKind > p2_highKind:
            return -1
        # If player 2 has higher value in three of a kind in full house
        elif p1_highKind < p2_highKind:
            return 1
        # If both players have same valued card in three of a kind in full house
        else:
            # Check value of pair cards for both players
            p1_highPair = self.p1_pairList[0]
            p2_highPair = self.p2_pairList[0]

            # If player 1 has higher value in pair in full house
            if p1_highPair > p2_highPair:
                return -1
            # If player 2 has higher value in pair in full house
            elif p1_highPair < p2_highPair:
                return 1
            # If both players have same valued pair in full house
            else:
                return 0

    