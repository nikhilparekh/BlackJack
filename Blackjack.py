import random
try:
    import tkinter
except ImportError:
    import Tkinter as tkinter

mainWindow = tkinter.Tk()
mainWindow.configure(background='green')
def load_images(card_images):
    suits=['heart', 'spade', 'club', 'diamond' ]
    face_cards = ['king','queen','jack']
    
    if tkinter.TkVersion >= 8.6:
        extension = 'png'
    else:
        extension = 'ppm'

    for suit in suits:
        for card in range(1,11):
            name = 'cards/{}_{}.{}'.format(str(card), suit, extension)
            image = tkinter.PhotoImage(file=name)
            card_images.append((card,image,))


        for card in face_cards:
            name = 'cards/{}_{}.{}'.format(str(card), suit, extension)
            image = tkinter.PhotoImage(file=name)
            card_images.append((10,image,))

def deal_card(frame):
    next_card = deck.pop(0)
    tkinter.Label(frame, image=next_card[1], relief='raised').pack(side='left')
    return next_card


def score_hand(hand):
    score = 0
    ace = False
    for next_card in hand:
        card_value = next_card[0]
        
        if card_value == 1 and not ace:
            ace = True
            card_value = 11
        score +=card_value 
        if score >21 and ace:
            score-=10
            ace = False
    return score


def deal_dealer():
    dealer_hand.append(deal_card(dealer_card_frame))
    dealer_score = score_hand(dealer_hand)
    dealer_score_label.set(dealer_score)

    player_score = score_hand(player_hand)
    if player_score > 21:
        result_text.set("Dealer Wins")
    elif dealer_score > 21 or dealer_score < player_score:
        result_text.set("Player Wins")
    elif dealer_score > player_score:
        result_text.set("Dealer Wins")
    else: 
        result_text.set("Its a draw!!")

def deal_player():
    player_hand.append(deal_card(player_card_frame))
    player_score = score_hand(player_hand)

    player_score_label.set(player_score)
    if player_score > 21:
        result_text.set("Dealer Win")
    # global player_score 
    # global player_ace
    # card_value = deal_card(player_card_frame)[0]
    # if card_value == 1 and not player_ace:
    #     player_ace  = True
    #     card_value = 11
    # player_score +=card_value
    # if player_score > 21 and player_ace:
    #     player_ace = False
    #     player_score -=10
    # player_score_label.set(player_score)
    # if player_score > 21:
    #     result_text("Dealer Wins...")
        


mainWindow.title("Black Jack")
mainWindow.geometry("640x480")

result_text = tkinter.StringVar()
result = tkinter.Label(mainWindow, textvariable=result_text)
result.grid(row=0, column=0, columnspan=3)

card_frame = tkinter.Frame(mainWindow, relief="sunken", borderwidth=1, background="green")
card_frame.grid(row=1, column=0, sticky="ew", columnspan=3, rowspan=2)

dealer_score_label = tkinter.IntVar()
tkinter.Label(card_frame, text="Dealer", background="green", fg="white").grid(row=0, column=0)
tkinter.Label(card_frame, textvariable=dealer_score_label, background="green", fg="white").grid(row=1, column=0)

dealer_card_frame = tkinter.Frame(card_frame, background="green")
dealer_card_frame.grid(row=0, column=1, sticky="ew", rowspan=2)

player_score_label = tkinter.IntVar()

tkinter.Label(card_frame, text="Player", background="green", fg="white").grid(row=2, column=0)
tkinter.Label(card_frame, textvariable=player_score_label, background="green", fg="white").grid(row=3,column=0)

player_card_frame = tkinter.Frame(card_frame, background="green")
player_card_frame.grid(row=2, column=1, sticky="ew", rowspan=2)

button_frame = tkinter.Frame(mainWindow)
button_frame.grid(row=3, column=0, columnspan=3, sticky="w")

dealer_button = tkinter.Button(button_frame, text="Dealer", command=deal_dealer)
dealer_button.grid(row=0, column=0)

player_button = tkinter.Button(button_frame, text="Player", command=deal_player)
player_button.grid(row=0,column=1)

cards = []
load_images(cards)
print(cards)
deck = list(cards)
random.shuffle(deck)

player_hand = []
dealer_hand = []

deal_player()
dealer_hand.append(deal_card(dealer_card_frame))
deal_player()

mainWindow.mainloop()