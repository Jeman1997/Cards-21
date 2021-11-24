import random
print("""
--------------------------------------------------**WELCOME TO BLACK JACK**----------------------------------
-----------------------------------------------------------***RULES***------------------------------------------------------------------
There are a deck(13 of them) of cards:[Ace[Value is 11 or 1],Joker[value is 10],Queen[value is 10],King[value is 10],2,3,4,5,6,7,8,9,10]
The Computer which is the dealer picks card and gives u a card, both of which you can see
The dealer then picks another 2 cards for both of you. Now you can only know what's your card.
If the 2 cards' values sum is more than 21 YOU LOOSE.
If 'A' is among the cards and the sum is more than 21. The 'A's value changes to 1.
If the sum of values of 2 card's of the dealer is less than 17. He has to pick another card.
If you didn't loose till now. You can choose another card until the cards are not finished or the sum doesn't exceed 21
Finally after you're done choosing,WINNER, LOSER and DRAW are decided by comparing the sums of values of your's and the dealer's cars
-----------------------------------------------------------------------------------------------------------------------------------------
""")
def blackjack():
    di={'A':11,'J':10,'Q':10,'K':10}
    cards=['A','J','Q','K',2,3,4,5,6,7,8,9,10]
    pcards=[]
    dcards=[]
    #Pick First player and dealer cards
    p1=random.choice(cards)
    cards.pop(cards.index(p1))
    d1=random.choice(cards)
    cards.pop(cards.index(d1))
    pcards.append(p1)
    dcards.append(d1)
    print(f"Your First card is {p1}\nThe Dealer's card is {d1}")
    #----------------------------------------
    #Pick Second player and dealer cards
    p2=random.choice(cards)
    cards.pop(cards.index(p2))
    d2=random.choice(cards)
    cards.pop(cards.index(d2))
    pcards.append(p2)
    dcards.append(d2)
    print(f"Your Second card is {p2}")
    #----------------------------------------
    def s(c):
        ps=0
        for x in c:
            if x in di:
                ps=ps+di[x]
            else:
                ps=ps+x
        return ps
    def worl():    
        if sofp>sofd:
            print(f"You win, Your cards:{pcards}\n and Dealer's cards:{dcards}")
        elif sofp==sofd:
            print(f"Draw, Your cards:{pcards}\n and Dealer's cards:{dcards}")
        else:
            print(f"You loose!  Your cards:{pcards}\n and Dealer's cards:{dcards}")
    sofp=s(pcards)
    sofd=s(dcards)
    while sofp>21:
        if 'A' in pcards:
            sofp=sofp-10
        else:
            print(f"You loose!  Your cards:{pcards}\n and Dealer's cards:{dcards}")
            break
            return
    while sofd<17 and len(cards)>0:
         d=random.choice(cards)
         print("Dealer's cards' sum up to less than 17 so he picked another one")
         cards.pop(cards.index(d))
         dcards.append(d)
         sofd=s(dcards)
         if sofd>21:
             dcards.pop()
             sofd=s(dcards)
    #print(pcards,dcards)
    ask=True
    while len(cards)>0 and ask:
        if input("Do you want another card?(y or n)\n").lower()=='y':
            p=random.choice(cards)
            print(f"Your another card is {p}")
            pcards.append(p)
            sofp=s(pcards)
            lca=[]
            for x in pcards:
              if x!='A':
                lca.append(x)
            if sofp>21 :
                if 'A' in pcards and not s(lca)>21:
                    sofp=sofp-10  
                else:
                    print(f"You loose! Your cards:{pcards}\n and Dealer's cards:{dcards}")
                    ask=False  
                    break                     
        else:
            ask=False
            worl()
    
blackjack()
run=True
while run:
  if input("Do your wanna play again?(y or n)/n").lower()=='y':
    blackjack()
  else:
    print("Well, Thank you!")
    run=False
