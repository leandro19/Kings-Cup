'''
Leandro Ribeiro
Brian Doyle
lribeir1@binghamton.edu
bdoyle2@binghamton.edu
CS 110 B54
CAs: Nuri & Vlad
'''
import random

'''
This class represents a drinking game named: Kings. This class makes
use of several different constants defined within the class, along
with the use of different constructors, accessors, mutators
and tostrings. The class Game allows for the playing of Kings, which
allows the user to select a card and then display the official rule
associated with the card. When the deck is exhausted the Game class
will terminate. 

Output to GUI:
  Back of card = gif
  Front of selected card = gif
  Select button

Input from Keyboard:
  How many players - int
  King's rules - str

Tasked Allocated to Functions:
  getPlayer() - returns player
  getCard() - returns card
  getCardStatus() - returns the rule associated with card
  getKingCount() - checks how many kings have been in play
  getPlayerList() - returns the list of players
  getDiscardPile() - returns the list of cards that already been used
  sameImage() - checks whether or not that image has been displayed
  gameOver() - ends game at the point when all cards have been played
  makeARule() - allows user to input rule for drawn king(s)
  getCardImage() - displays card image associated with code
  isPlayable() - predicate to check if that cards has/hasnt been used
  setPlayerList() - sets how many players are playing
  makeATurn() - bulky definition that allows for the playing of the game
  nextPlayer() - runs to next player after user clicks for the next card
'''

class Game:

#-- Class Variables ---------------------------------------------------- 
  ZERO = 0
  ONE = 1
  FOUR = 4
  THIRTEEN = 13
  FIFTY_TWO = 52
  SUITS = 'cdhs'
  SUIT_NUMBER = 4
  ACE = 1
  HIGH_CARD = 14
  GAME_OVER = 13
  PLAYER = 'Player '

  # Rule associated with the selected card, used via Indexing
  RULE_LIST = ['Waterfall: Drink until the person to your left stops.',
               'Make two people drink or make one person drink twice.',
               'Take a drink',
               'Everyone point to the floor, last one pointing drinks.',
               'All of the guys drink',
               'All of the ladies drink',
               'Everyone point to the ceiling, last one pointing drinks',
               'Pick a "date", every time you drink they will drink with you',
               'Pick a word, the person to your right must say a word that rhymes, otherwise drink',
               'Pick a category,the person to your right must come up with something related to that category, otherwise drink',
               'Place your thumb on the table, last one to place their thumb drinks',
               "Queen's Cup: The person who draws the final queen must finish their cup.",
               'Make a rule, everyone must follow this rule for the duration of the game',
               "You've exhausted the deck, game over!"]

#-- Constructor --------------------------------------------------------
  def __init__(self):
    self.__playerList = []
    self.__discardPile = []
    self.__discardImages = []
    self.__currentPlayer = 'Player 1'
    self.__cardCount = self.FIFTY_TWO
    self.__cardStatus = ''
    self.__card = None
    self.__maxPlayers = self.ZERO
    self.__kingsCount = self.ZERO

#-- Accessors ----------------------------------------------------------
  def getPlayer(self):
    return self.__currentPlayer

  def getCard(self):
    return self.__card

  def getCardStatus(self):
    return self.__cardStatus

  def getKingCount(self):
    return self.__kingsCount

  def getPlayerList(self):
    return self.__playerList

  def getDiscardPile(self):
    return self.__discardPile
    
  def sameImage(self,image):
    return image in self.__discardImages

  def gameOver(self):
    return self.__cardCount == self.ZERO

  def makeARule(self,rule):
    newRule = 'Rule '+str(self.__kingsCount)+': '+ rule
    return newRule

  def getCardImage(self):
    image = self.SUITS[random.randrange(self.SUIT_NUMBER)] + str(self.__card)+'.gif'
    while self.sameImage(image):
      image = self.SUITS[random.randrange(self.SUIT_NUMBER)] + str(self.__card)+'.gif'
    self.__discardImages += [image]
    return image
  
#-- Predicates ---------------------------------------------------------

  def isPlayable(self):
    return self.__discardPile.count(self.__card) < self.FOUR

#-- Mutators -----------------------------------------------------------

  def setPlayerList(self,playerNum):
    for i in range(self.ONE,playerNum+self.ONE):
      myPlayer = self.PLAYER + str(i)
      self.__playerList += [myPlayer]
      myPlayer = ''
    self.__maxPlayers = len(self.__playerList)
      
  def makeATurn(self):
    if self.gameOver():
      self.__cardStatus = self.RULE_LIST[self.GAME_OVER]
    else:
      self.__card = random.randrange(self.ACE,self.HIGH_CARD)
      while not self.isPlayable():
        self.__card = random.randrange(self.ACE,self.HIGH_CARD)
      self.__cardStatus = self.RULE_LIST[self.__card - self.ONE]
      self.__discardPile += [self.__card]
      if self.__card == self.THIRTEEN:
        self.__kingsCount += self.ONE
      if self.__cardCount < self.FIFTY_TWO:
        self.nextPlayer()
      self.__cardCount -= self.ONE
  
  def nextPlayer(self):
    if self.__currentPlayer == self.__playerList[self.__maxPlayers-self.ONE]:
      self.__currentPlayer = self.PLAYER+'1'
    else:
      self.__currentPlayer = self.__playerList[self.__playerList.index(\
        self.__currentPlayer)+self.ONE]
    

  
      
    

  
