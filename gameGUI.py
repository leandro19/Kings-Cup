'''
Leandro Ribeiro
Brian Doyle
lribeir1@binghamton.edu
bdoyle2@binghamton.edu
CS 110 B54
CAs: Nuri & Vlad
'''
'''
This GUI represents a drinking game named: Kings. This GUI imports
the various classes needed to run program. The GUI allows for the
playing of Kings, whichallows the user to select a card and then
display the official rule associated with the card. When the deck
is exhausted the GUI will terminate. 

Output to GUI:
  Back of card = gif
  Front of selected card = gif
  Select button

Input from Keyboard:
  How many players - int
  King's rules - str

Tasked Allocated to Functions:
  validatePlayer(self) - predicate to check good input and circle
  through players
  makePlayers(self,event) - Creates player list after given input
  initialPlayer(self) - starts game off with player 1
  changePlayer(self) - loops through players
  pickCard(self) - bulkly function to simulate picking cards
  newRule(self,event) - deals with King card for entering rules
  changeImage(self) - iterates though image folder for specific card
'''

from tkinter import *

from game import *



class gameGUI:
  
  def __init__(self):

#--Window and Frame Initilization---------------------------------------
    self.__window = Tk()
    self.__window.wm_title("Kings")
    
    self.__game = Game()
    self.__title = Label(text='Welcome to the game of kings.')
    self.__playerLabel = Label(text= 'How many players?')

#--Card Display and Button Design---------------------------------------
    
    self.__playerEntry = Entry(width=2)
    self.__playerEntry.bind('<Return>', self.makePlayers)
    self.__playerVal = StringVar()
    
    self.__title.grid(column=1)
    self.__playerLabel.grid(row=1,column=1)
    self.__playerEntry.grid(row=1,column=1,sticky='E')
                         

    self.__mainCanvas = Canvas(width=195, height=100)

    self.__backCard = PhotoImage(file="card-BMPs/b1fv.gif")

    self.__mainCanvas.create_image(35,50,image=self.__backCard)
    self.__mainCanvas.grid(row=2, column=1,columnspan = 3)

    self.__rule = StringVar()
    self.__rule.set(self.__game.getCardStatus())
    self.__ruleLabel = Label(textvariable = self.__rule, wraplengt=180)
    self.__ruleLabel.grid(row=3,column=1)

    self.__newRuleEntry = Entry(width = 30)
    self.__newRuleEntry.bind('<Return>', self.newRule)

    self.__myNewRule = ''
    

    self.__pickButton = Button(text='Select your card', 
                                       command=self.pickCard)

    self.__pickButton.grid(row=5,column=1)


                                  
    mainloop()

#--Event Handlers-------------------------------------------------------

  def validatePlayer(self):
    return self.__playerNumStr.isdigit() and int(self.__playerNumStr) > 1

  def makePlayers(self,event):
    self.__playerNumStr = self.__playerEntry.get()
    if self.validatePlayer():
      self.__game.setPlayerList(int(self.__playerNumStr))
      self.__playerEntry.grid_remove()
      self.__playerLabel.grid_remove()
      self.initialPlayer()
    else:
      messagebox.showwarning('Invalid input!','Please enter a valid number of players.')
    
  def initialPlayer(self):
    self.__playerVal.set(self.__game.getPlayer()+"'s Turn")
    self.__currentPlayer = Label(textvariable = self.__playerVal)
    self.__currentPlayer.grid(row=1,column=1)
    
  def changePlayer(self):
    self.__playerVal.set(self.__game.getPlayer()+"'s Turn")
    
  def pickCard(self):
    if self.__game.gameOver():
      self.__game.makeATurn()
      self.__rule.set(self.__game.getCardStatus())
      self.__mainCanvas.destroy()
      self.__pickButton.destroy()
      self.__currentPlayer.destroy()
      self.__quitButton = Button(text='Quit', command=self.__window.destroy)
      self.__quitButton.grid(row=5,column=1)
    else:
      if len(self.__game.getPlayerList()) > 1:
        if len(self.__game.getDiscardPile()) == 0 or self.__game.getCard()\
           != 13 or len(self.__myNewRule) > 0 :
          self.__game.makeATurn()
          self.__rule.set(self.__game.getCardStatus())
          self.changePlayer()
          self.changeImage()
          if self.__newRuleEntry == True:
            self.__newRuleEntry.grid_remove()
        else:
          messagebox.showwarning('Wait!','Please type in a rule, then press <Enter>.')
        if self.__game.getCard() == 13:
          self.__newRuleEntry.grid(row=4,column=1)
          self.__newRuleEntry.delete(0, END)
          self.__myNewRule = ''
          
      else:
        messagebox.showwarning('Hold on!','Please enter the number of players, then press <Enter>.')
        
  def newRule(self,event):
    if not self.__newRuleEntry.get():
      messagebox.showwarning('Wait!','Please type in a rule, then press <Enter>.')
    else:
      myRule = self.__newRuleEntry.get()
      self.__myNewRule = self.__game.makeARule(myRule)
      self.__newRuleEntry.grid_remove()
      self.__newRuleLabel = Label(text=self.__myNewRule,wraplengt=180)
      self.__newRuleLabel.grid(row=self.__game.getKingCount()+5,column=1,sticky='W')
       
  
  def changeImage(self):
    self.__card = PhotoImage(file='card-BMPs/'+self.__game.getCardImage())
    self.__mainCanvas.create_image(140,50,image=self.__card)

#--Instance of gameGUI class--------------------------------------------    
gameGUI()
