import sys
import getopt
from CompareHands import CompareHands

class PokerHands:
    def __init__(self, ifile, ofile):
        self.inputFile = ifile
        self.outputFile = ofile    
        # Opening the input file
        file = open(self.inputFile, "r")
        # Reading all the hands
        self.hands = file.readlines()
        self.cardDict = convertCardDataToTuple()
        self.player1wins = 0
        self.player2wins = 0
        file.close()

    def findSolution(self):
        #wins = []
        #p1score = []
        #p2score = []
        # For all the hands in the list (input file)
        for hand in self.hands:
            # Create a list of single cards
            cards = hand.split()
            # Find middle point. Assumption: Since 5 cards are assumed per player, we split the list from center
            middleIndex = len(cards)//2
            # Split the list at middle index
            p1_hand = cards[:middleIndex]
            p2_hand = cards[middleIndex:]
            p1_hand = [self.cardDict[h] for h in p1_hand]
            p2_hand = [self.cardDict[h] for h in p2_hand]
            # handComparator(p1_hand, p2_hand)
            handComparator = CompareHands()
            response = handComparator.compare(p1_hand, p2_hand)
            if response == -1:
                self.player1wins += 1
            elif response == 1:
                self.player2wins += 1
            
            #wins.append(response)
            #p1score.append(handComparator.p1_score)
            #p2score.append(handComparator.p2_score)

        #self.writeOut(zip(self.hands, wins, p1score, p2score))
        self.writeOut()

    def writeOut(self):
        # Create/Open the file with the given name 
        file = open(self.outputFile, "w")
        # Content for the output file
        line1 = "Player 1: " + str(self.player1wins) + "\n"
        line2 = "Player 2: " + str(self.player2wins)
        # Write out to the file
        file.writelines([line1, line2])

        #for hand, win, p1sc, p2sc in written:
        #    file.write(hand.rstrip() + ' ' + str(win) + ' ' + str(p1sc) + ' ' + str(p2sc) + '\n')

        file.close()

# Returns a dictionary where a card (string) is a key and value is the corresponding tuple with number on the card as first value of tuple and colour/suit of the card as second value of tuple
def convertCardDataToTuple():
    dictionary = dict()

    # All single-digit integers on cards are as it is. T = 10, Jack = 11, Queen = 12, King = 13, Ace = 14
    # Since ace is high card
    numToStringDict = {10 : 'T', 11 : 'J', 12 : 'Q', 13 : 'K', 14 : 'A'}

    for i in range(2, 15):
        # Suit - 'D' = Diamonds, 'H' = Hearts, 'S' = Spades, 'C' = Clubs
        for suit in ['D', 'H', 'S', 'C']:
            key = ''
            if i < 10:
                # Converting number to string and then concat with suit
                num = str(i)
                key = num + suit
            else:
                numStr = numToStringDict[i]
                key = numStr + suit
            # Example - 4 of Spade: key = 4S -> value = (4, 'S')
            dictionary[key] = (i, suit)

    return dictionary


if __name__ == '__main__':
    arguments = sys.argv[1:]
    inputfile = ''
    outputfile = ''

    if len(arguments) != 4:
        print('Incorrect number of arguments')
        sys.exit(2)

    try:
        options, args = getopt.getopt(arguments, "i:o:", ["input-file=", "output-file="])
    except getopt.GetoptError:
        print('Error. Arguments incorrect')
        sys.exit(2)

    for opt, arg in options:
        if opt in ['-i', '--input-file']:
            inputfile = arg
        elif opt in ['-o', '--output-file']:
            outputfile = arg

    # Start poker hands analysis
    analysis = PokerHands(inputfile, outputfile)
    analysis.findSolution()