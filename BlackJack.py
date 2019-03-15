# Black Jack Project
# Created by Danley Nemorin


from tkinter import Label
from tkinter import Frame
from tkinter import Button
from tkinter import Toplevel
from tkinter import TOP
import tkinter.messagebox as box
import random


# The Class for the Cards
class card:
    def __init__(self, suit, number, value):
        self.suit = suit
        self.number = number
        self.value = value


# This function genenrates the cardList, it's necessary...
def generateCardList():
    listCardSuits = ["Spades", "Hearts", "Diamonds", "Clubs"]
    maxcards = 4
    wholeCardList = [[] for i in range(maxcards)]
    for x in range(0, maxcards):
        wholeCardList[x].append(card(listCardSuits[x], "Ace", 1))
        wholeCardList[x].append(card(listCardSuits[x], "2", 2))
        wholeCardList[x].append(card(listCardSuits[x], "3", 3))
        wholeCardList[x].append(card(listCardSuits[x], "4", 4))
        wholeCardList[x].append(card(listCardSuits[x], "5", 5))
        wholeCardList[x].append(card(listCardSuits[x], "6", 6))
        wholeCardList[x].append(card(listCardSuits[x], "7", 7))
        wholeCardList[x].append(card(listCardSuits[x], "8", 8))
        wholeCardList[x].append(card(listCardSuits[x], "9", 9))
        wholeCardList[x].append(card(listCardSuits[x], "10", 10))
        wholeCardList[x].append(card(listCardSuits[x], "Jack", 10))
        wholeCardList[x].append(card(listCardSuits[x], "Queen", 10))
        wholeCardList[x].append(card(listCardSuits[x], "King", 10))
    return wholeCardList


# THE MENU FRAME, WHERE IT BEGINS
class BlackJackMenu(Frame):
    funds = 1000

    def __init__(self):
        Frame.__init__(self)
        self.pack(padx=100, pady=80)
        self.master.title("Black Jack")
        self.label = Label(self, text="Black Jack!")
        self.buttonGame = Button(self, text="Play BlackJack!",
                                 width=25, command=self.playGame)
        self.buttonDisplayFunds = Button(self, text="Display Available Funds",
                                         width=25, command=self.showFunds)
        self.buttonResetFunds = Button(self, text="Reset Funds",
                                       width=25, command=self.resetFunds)
        self.buttonQuit = Button(self, text="Quit",
                                 width=25, command=self.close_window)
        self.label.pack(pady=10)
        self.buttonGame.pack()
        self.buttonDisplayFunds.pack()
        self.buttonResetFunds.pack()
        self.buttonQuit.pack()

    def playGame(self):
        blackJackGameFrame()
        print("hi, I love you may")

    def showFunds(self):
        showFundsFrame()

    def resetFunds(self):
        resetFunds()

    def close_window(self):
        self.dialog()

    def dialog(self):
        var = box.askyesno('Dun leave...', 'Are you sure you want to close?')
        if var == 1:
            box.showinfo('Yes Box', 'Closing...')
            self.quit()
        else:
            box.showwarning('No Box', 'Cancelling...')


# THE GAME FRAME
class blackJackGameFrame(Frame):
    def __init__(self):
        gameFrame = Frame.__init__(self)
        gameFrame = Toplevel(self)
        gameFrame.title("BLACK JACK!")
        self.labelCard1 = Label(gameFrame, text="Card 1")
        self.labelCard2 = Label(gameFrame, text="Card 2")
        self.labelCard3 = Label(gameFrame, text="Result")
        buttonDeal = Button(gameFrame, text="Deal!", command=self.deal)
        self.labelCard1.pack(side=TOP)
        self.labelCard2.pack(side=TOP)
        self.labelCard3.pack(pady=5)
        buttonDeal.pack(padx=86, pady=10)
        self.cardList = generateCardList()
        self.score = 0

    def giveRandomCard(self):
        element1 = random.randint(0, 3)
        element2 = random.randint(0, element1)
        card = self.cardList[element1][element2]
        self.cardList[element1].remove(card)
        return card

    def deal(self):
        card1 = self.giveRandomCard()
        card2 = self.giveRandomCard()
        self.labelCard1.config(text=card1.number + " of " + card1.suit)
        self.labelCard2.config(text=card2.number + " of " + card2.suit)
        self.score += card1.value + card2.value
        print(self.score)
        if self.score == 21:
            box.showinfo('YA WON', "CHING CHING YA WON 100$")
            self.labelCard3.config(text="You have " +
                                   str(self.score) + " points!")
            BlackJackMenu.funds += 100
        elif self.score < 21:
            self.labelCard3.config(text="You have " +
                                   str(self.score) + " points!")
            # lower value change some stuff
        elif self.score > 21:
            box.showinfo('Haha', "YA LOST, 50$ GONE")
            BlackJackMenu.funds -= 50
            self.destroy()
            if BlackJackMenu.funds < 0:
                box.showinfo('oh..', "You have no money.. you lost bye!")
                self.quit()


# show Funds Frame
class showFundsFrame(Frame):
    def __init__(self):
        sff = Frame.__init__(self)
        sff = Toplevel(self)
        sff.title("Your Funds!")
        label = Label(sff, text="Your fund is: " + str(BlackJackMenu.funds))
        buttonClose = Button(sff, text="Close", width=20,
                             command=self.close_window)
        label.pack()
        buttonClose.pack()

    def close_window(self):
        self.destroy()
    # reset funds frame


class resetFunds(Frame):
    def __init__(self):
        rsFrame = Frame.__init__(self)
        rsFrame = Toplevel(self)
        rsFrame.title("Reset Funds")
        label = Label(rsFrame, text="Your funds are: " +
                      str(BlackJackMenu.funds) +
                      "$, are you sure you want to reset it?")
        buttonYes = Button(rsFrame, text="Yes I want to delete them",
                           command=self.resetTheFunds)
        label.pack()
        buttonYes.pack()

    def resetTheFunds(self):
        BlackJackMenu.funds = 1000
        self.destroy()


#THE GAME FRAME
class blackJackGameFrame(Frame):
       def __init__(self):
               gameFrame = tk.Frame.__init__(self)
               gameFrame = Toplevel(self)
               gameFrame.title("BLACK JACK!")
               self.labelCard1 = tk.Label(gameFrame, text ="Card 1")
               self.labelCard2 = tk.Label(gameFrame, text = "Card 2")
               self.labelCard3 = tk.Label(gameFrame, text = "Result")
               buttonDeal = tk.Button(gameFrame, text = "Deal!", command = self.deal)

               self.labelCard1.pack(side = TOP)
               self.labelCard2.pack(side = TOP)
               self.labelCard3.pack(pady = 5)
               buttonDeal.pack(padx = 86, pady = 10)

               self.cardList = generateCardList()
               self.score = 0
               
       def giveRandomCard(self):
                element1 = random.randint(0,3)
                element2 = random.randint(0,element1)
                card = self.cardList[element1][element2]

                self.cardList[element1].remove(card)
                
                return card
                
        

       def deal(self):
                card1 = self.giveRandomCard()
                card2 = self.giveRandomCard()

                self.labelCard1.config(text= card1.number + " of " + card1.suit)
                self.labelCard2.config(text= card2.number + " of " + card2.suit)

                self.score += card1.value + card2.value
                print(self.score)

                if self.score == 21:
                        box.showinfo('YA WON', "CHING CHING YA WON 100$")
                        self.labelCard3.config(text= "You have " + str(self.score) + " points!")
                        BlackJackMenu.funds += 100
                elif self.score < 21:
                        self.labelCard3.config(text= "You have " + str(self.score) + " points!")
                        #lower value change some stuff
                elif self.score > 21:
                        box.showinfo('Haha', "YA LOST, 50$ GONE")
                        BlackJackMenu.funds -= 50
                        self.destroy()

                        if BlackJackMenu.funds < 0:
                                box.showinfo('oh..', "You have no money.. you lost bye!")
                                self.quit()                

                
# show Funds Frame            
class showFundsFrame(Frame):
	def __init__(self):
		sff = tk.Frame.__init__(self)
		sff = Toplevel(self)
		sff.title("Your Funds!")
		label = tk.Label(sff, text="Your fund is: " + str(BlackJackMenu.funds))
		buttonClose = tk.Button(sff, text = "Close", width = 20, command = self.close_window)

		label.pack()
		buttonClose.pack()
	

	def close_window(self):
		self.destroy()
# reset funds frame
class resetFunds(Frame):
       def __init__(self):
	       rsFrame = tk.Frame.__init__(self)
	       rsFrame = Toplevel(self)
	       rsFrame.title("Reset Funds")

	       label = tk.Label (rsFrame, text="Your funds are: " +  str(BlackJackMenu.funds) + "$, are you sure you want to reset it?")
	       buttonYes = tk.Button(rsFrame, text = "Yes I want to delete them", command = self.resetTheFunds)
	       label.pack()
	       buttonYes.pack()
	       
       def resetTheFunds(self):
                BlackJackMenu.funds = 1000
                self.destroy()
                
def main():
    BlackJackMenu().mainloop()


if __name__ == '__main__':
    main()
