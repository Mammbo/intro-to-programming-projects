# Section1: Create the Blackjack program
# Daniel Alvarez
# 3/7/24

import time 
import random
import locale
from datetime import timedelta
from timeit import default_timer as timer


# define dictionary for all cards and their values
cards = {
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10": 10,
    "K": 10,
    "Q": 10,
    "J": 10,
    "A": [1, 11],
}
#define directory for all suites
suites = {"♦": "diamonds", "♣": "clubs", "♥": "hearts", "♠": "spades"}

#calculates the total number of points if a player has an ace
def player_ace(Ppoints):

    total_Ppoints = 0
    ace_count = 0
    # Iterate through the sublists in Ppoints
    for card in Ppoints:
        if isinstance(card, list):
            total_Ppoints += max(card)
            ace_count += 1
        else:
            total_Ppoints += card
    #will take away 10 from the ace cards till they are below 21 or they are stll over and bust 
    while total_Ppoints > 21 and ace_count > 0:
        total_Ppoints -= 10
        ace_count -= 1
    return total_Ppoints


def dealer_ace(Dpoints):

    total_Dpoints = 0
    ace_count = 0
    # Iterate through the sublists in Dpoints
    for card in Dpoints:
        if isinstance(card, list):
            total_Dpoints += max(card)
            ace_count += 1
        else:
            total_Dpoints += card
    #will take away 10 from the ace cards till they are below 21 or they are stll over and bust 
    while total_Dpoints > 21 and ace_count > 0:
        total_Dpoints -= 10
        ace_count -= 1
    return total_Dpoints


def dealer():
    # pulls random card from the cards dictionary and random suite from the suites dictionary appending the card to players_total_cards and the points to players_card_value
    dealers_total_cards = []
    dealers_card_value = []
    dealer_card1 = random.choice(list(cards.keys()))
    dealer_card2 = random.choice(list(cards.keys()))
    suite1 = random.choice(list(suites.keys()))
    suite2 = random.choice(list(suites.keys()))
    #combines the card and the suite so they can be appeneded to a singular list 
    new_dealer_card1 = dealer_card1 + suite1
    new_dealer_card2 = dealer_card2 + suite2
    #pulls the value coressponding with the pulled card into a list and appends it 
    point1 = cards[dealer_card1]
    point2 = cards[dealer_card2]
    dealers_card_value.append(point1)
    dealers_card_value.append(point2)
    #appends the shown cards to a list 
    dealers_total_cards.append(new_dealer_card1)
    dealers_total_cards.append(new_dealer_card2)
    #shows only the dealers first card
    print(f"DEALER'S SHOW CARD:\n{new_dealer_card1}\n")
    #returns these values for the next turn 
    return dealers_total_cards, dealers_card_value


def player():
    # pulls random cards from the cards dictionary and random suite from suites directory appending the card to players_total_cards and the points to players_card_value
    players_total_cards = []
    players_card_value = []
    player_card1 = random.choice(list(cards.keys()))
    player_card2 = random.choice(list(cards.keys()))
    player_suite1 = random.choice(list(suites.keys()))
    player_suite2 = random.choice(list(suites.keys()))
    #combines the card and the suite so they can be appeneded to a singular list 
    new_player_card1 = player_card1 + player_suite1
    new_player_card2 = player_card2 + player_suite2
     #pulls the value coressponding with the pulled card into a list and appends it 
    point1 = cards[player_card1]
    point2 = cards[player_card2]
    players_card_value.append(point1)
    players_card_value.append(point2)
    #appends the shown cards to a list 
    players_total_cards.append(new_player_card1)
    players_total_cards.append(new_player_card2)
    #gets rid of brackets from the card list to then be printed out 
    temp_players_total_cards = ", ".join(map(str, players_total_cards))
    #shows the list of the two cards to the player 
    print(f"YOUR CARDS:\n{temp_players_total_cards}\n")
    #returns these values for the next turn 
    return players_total_cards, players_card_value


def dealers_turn(Dcards, Dpoints):
    #keeps this in a while loop for until the certain conditions of the dealer are met 
    while True:
        #checks if dealer has an ace card in any of the lists within Dpoints
        has_soft_ace = any(
            1 in sublist or 11 in sublist
            for sublist in Dpoints
            if isinstance(sublist, list)
        )
        #if yes we will preform the dealer_ace function that was described above to get the maximum number of points 
        if has_soft_ace:
            total_Dpoints = dealer_ace(Dpoints)
            #if the total of that dealers function is between 17 and 21 we wont pull another card and convert our output into a list and return the values 
            if 21 > total_Dpoints and total_Dpoints >= 17:
                Dpoints = [total_Dpoints]
                return Dcards, Dpoints
            #if the output is equal to 21, the output will be converteed to a list, print a message saying that the dealer has black jack, and then return the values.
            elif 21 == total_Dpoints:
                Dpoints = [total_Dpoints]
                print("DEALER HAS BLACKJACK!")
                return Dcards, Dpoints
            #if the total of Dpoints is over 21 a messaged saying that the Dealer has busted will be printed out, the output will be converted to a list, and then the values will be returned. 
            elif total_Dpoints > 21:
                print("Dealer has a bust.\n")
                Dpoints = [total_Dpoints]
                return Dcards, Dpoints
            #if the value of players ace is belwo 17 we will pull another card and repeat the check all over again 
            else:
                pull_card = random.choice(list(cards.keys()))
                pull_suite = random.choice(list(suites.keys()))

                new_card = pull_card + pull_suite

                point = cards[pull_card]

                Dpoints.append(point)
                Dcards.append(new_card)
                continue
        # if there is no ace within the deck we mmove on to the next check 
        else:
            #if the total sum of the ints in the list are equal to a number less than 17 we will pull another card
            if sum(Dpoints) < 17:

                while sum(Dpoints) < 17:
                    pull_card = random.choice(list(cards.keys()))
                    pull_suite = random.choice(list(suites.keys()))

                    new_card = pull_card + pull_suite

                    point = cards[pull_card]

                    Dpoints.append(point)
                    Dcards.append(new_card)
                    #check for if the pulled card is an ace, 
                    has_soft_ace = any(
                        1 in sublist or 11 in sublist
                        for sublist in Dpoints
                        if isinstance(sublist, list)
                    )
                    #if yes we will calculate and then do checks for bust, target amount, and blackjack. if none of those are met we will restart from the first while loop. 
                    if has_soft_ace:
                        total_Dpoints = dealer_ace(Dpoints)

                        if 21 > total_Dpoints and total_Dpoints >= 17:
                            Dpoints = [total_Dpoints]
                            return Dcards, total_Dpoints
                        elif 21 == total_Dpoints:
                            print("DEALER HAS BLACKJACK!\n")
                            return Dcards, total_Dpoints
                        elif total_Dpoints > 21:
                            print("Dealer has a bust.\n")
                            Dpoints = [total_Dpoints]
                            return Dcards, Dpoints

                        else:
                            break
            # if the deck is more than 17, the checks for the target amount, blackjack, bust, and if none are met we will loop. 
            else:
                if 21 > sum(Dpoints) and sum(Dpoints) >= 17:
                    return Dcards, Dpoints
                elif 21 == sum(Dpoints):
                    print("DEALER HAS BLACKJACK")
                    return Dcards, Dpoints
                elif sum(Dpoints) > 21:
                    print("Dealer has a bust.\n")
                    return Dcards, Dpoints
                else:
                    continue


def players_turn(Pcards, Ppoints, Dcards, Dpoints):
    #loops for players hit or stand decision. 
    while True:
        #check for if the intial roll is a black jack, if so we will go into the dealers function and then convert the ace output into a list and than print out both the dealers and players cards. After than we will return the points to the programs output. 
        if player_ace(Ppoints) == 21:
            Ppoints = player_ace(Ppoints)
            Dcards, Dpoints = dealers_turn(Dcards, Dpoints)
            Ppoints = [Ppoints]

            temp_Pcards = ", ".join(map(str, Pcards))
            temp_Dcards = ", ".join(map(str, Dcards))

            print("YOU HAVE BlACKJACK!")
            print(
                f"\nYOUR CARDS:          {temp_Pcards}\nDEALER'S CARDS:      {temp_Dcards}\n"
            )

            return Ppoints, Dpoints

        else:
            # asks for user input of hit or stand 
            turn = input("Hit or stand? (h/s): ")

            new_turn = turn.lower()
            #calculates if we have a soft ace. 
            has_soft_ace = any(
                1 in sublist or 11 in sublist
                for sublist in Ppoints
                if isinstance(sublist, list)
            )
            #if yes
            if has_soft_ace:
                # and if the output is h, we will pull a card ( the intital card takes care of the blackjack pull from a king and ace.)
                if new_turn == "h":
                    pull_card = random.choice(list(cards.keys()))
                    pull_suite = random.choice(list(suites.keys()))

                    new_card = pull_card + pull_suite

                    point = cards[pull_card]

                    Ppoints.append(point)
                    Pcards.append(new_card)

                    temp_Pcards = ", ".join(map(str, Pcards))

                    print(f"YOUR CARDS:\n{temp_Pcards}")
                    #checks again for another ace 
                    has_soft_ace = any(
                        1 in sublist or 11 in sublist
                        for sublist in Ppoints
                        if isinstance(sublist, list)
                    )
                    #if yes, we will total the amount using the player ace function. 
                    if has_soft_ace:

                        total_Ppoints = player_ace(Ppoints)
                        # if the total amount is over 21 prints out bust, uses dealers function, and then prints of the cards. After that, we will turn the player_ace output into a list and return the points 
                        if total_Ppoints > 21:

                            print("You have a bust, you lose :< ")
                            Dcards, Dpoints = dealers_turn(Dcards, Dpoints)

                            temp_Pcards = ", ".join(map(str, Pcards))
                            temp_Dcards = ", ".join(map(str, Dcards))

                            print(
                                f"\nYOUR CARDS:          {temp_Pcards}\nDEALER'S CARDS:      {temp_Dcards}\n"
                            )

                            Ppoints = [total_Ppoints]
                            return Ppoints, Dpoints
                        # if the total amount is equal to blackjack, use deales function, print out blackjack, convert player_ace output into a list, and return the points 
                        elif total_Ppoints == 21:
                            print("BLACKJACK")
                            Dcards, Dpoints = dealers_turn(Dcards, Dpoints)
                            Ppoints = [total_Ppoints]

                            return Ppoints, Dpoints
                        #else we will continue and ask again for h or s 
                        else:
                            continue
                # if has ace and wants to stand, we will use player_ace functiona and conert the points to a list while calling the dealers-turn function, prints both cards and returns both the points for the dealer and the player. 
                elif new_turn == "s":
                    points = player_ace(Ppoints)
                    Dcards, Dpoints = dealers_turn(Dcards, Dpoints)

                    temp_Pcards = ", ".join(map(str, Pcards))
                    temp_Dcards = ", ".join(map(str, Dcards))

                    print(f"\nDEALER'S CARDS:\n{temp_Dcards}\n")
                    print(f"YOUR CARDS:\n{temp_Pcards}\n")

                    Ppoints = [points]
                    return Ppoints, Dpoints
                # if neither, asks to repeat the input for h or s.
                else:
                    print("Please type in either h(it) or s(tand). ")
            # if does not contain ace but still hit, pulls another card and prints out the total cards 
            else:
                if new_turn == "h":
                    pull_card = random.choice(list(cards.keys()))
                    pull_suite = random.choice(list(suites.keys()))

                    new_card = pull_card + pull_suite

                    point = cards[pull_card]

                    Ppoints.append(point)
                    Pcards.append(new_card)

                    temp_Pcards = ", ".join(map(str, Pcards))

                    print(f"YOUR CARDS:\n{temp_Pcards}\n")
                    # checks for if the card is another ace 
                    has_soft_ace = any(
                        1 in sublist or 11 in sublist
                        for sublist in Ppoints
                        if isinstance(sublist, list)
                    )
                    #if yea runs player_ace function 
                    if has_soft_ace:
                        total_Ppoints = player_ace(Ppoints)
                         # if the total amount is over 21 prints out bust, uses dealers function, and then prints of the cards. After that, we will turn the player_ace output into a list and return the points 
                        if total_Ppoints > 21:
                            print("You have a bust.")
                            Dcards, Dpoints = dealers_turn(Dcards, Dpoints)

                            temp_Pcards = ", ".join(map(str, Pcards))
                            temp_Dcards = ", ".join(map(str, Dcards))

                            print(
                                f"\nYOUR CARDS:        {temp_Pcards}\nDEALER'S CARDS:      {temp_Dcards}\n"
                            )

                            points = [total_Ppoints]
                            return points, Dpoints
                        # if the total amount is equal to blackjack, use deales function, print out blackjack, convert player_ace output into a list, and return the points 
                        elif total_Ppoints == 21:
                            Dcards, Dpoints = dealers_turn(Dcards, Dpoints)

                            temp_Pcards = ", ".join(map(str, Pcards))
                            temp_Dcards = ", ".join(map(str, Dcards))

                            print("YOU HAVE BLACK JACK!")
                            print(
                                f"\nYOUR CARDS:        {temp_Pcards}\nDEALER'S CARDS:      {temp_Dcards}\n"
                            )

                            Ppoints = [total_Ppoints]
                            return Ppoints, Dpoints
                        # if neither it will loop and ask for h or s again. 
                        else:
                            continue
                    # if the ace is not there 
                    elif has_soft_ace == False:
                        # calculates the sum of the points, and if it is over 21, message that will say the player has busted, run the dealer_turn function and then print the cards of the player and dealer. After all that the points will be returned 
                        if sum(Ppoints) > 21:
                            print("You have a bust.")
                            Dcards, Dpoints = dealers_turn(Dcards, Dpoints)

                            temp_Pcards = ", ".join(map(str, Pcards))
                            temp_Dcards = ", ".join(map(str, Dcards))

                            print(
                                f"\nYOUR CARDS:        {temp_Pcards}\nDEALER'S CARDS:    {temp_Dcards}\n"
                            )
                            return Ppoints, Dpoints
                          # calculates the sum of the points, and if it is equal to 21 , message that will say the player has blackjack, run the dealer_turn function and then print the cards of the player and dealer. After all that the points will be returned 
                        elif sum(Ppoints) == 21:
                            Dcards, Dpoints = dealers_turn(Dcards, Dpoints)
                    
                            temp_Pcards = ", ".join(map(str, Pcards))
                            temp_Dcards = ", ".join(map(str, Dcards))

                            print("YOU HAVE BLACKJACK!")
                            print(
                                f"\nYOUR CARDS:        {temp_Pcards}\nDEALER'S CARDS:      {temp_Dcards}\n"
                            )

                            return Ppoints, Dpoints
                        #if none of these cycle repeats from the first while loop.
                        else:
                            continue
                #if the choice was stand and no ace, dealers function will be run, cards will be printed and then the points will be returned
                elif new_turn == "s":
                    Dcards, Dpoints = dealers_turn(Dcards, Dpoints)

                    temp_Pcards = ", ".join(map(str, Pcards))
                    temp_Dcards = ", ".join(map(str, Dcards))

                    print(f"\nDEALER'S CARDS:\n{temp_Dcards}\n")
                    print(f"YOUR CARDS:\n{temp_Pcards}\n")

                    return Ppoints, Dpoints
                #if none of these, user will be prompted to correctly type h or s 
                else:
                    print("Please type in either h(it) or s(tand). ")


# intro to the game
print("BLACKJACK!")
print("Blackjack Payout is 3:2\n")

now = time.localtime()
formatted_time = time.strftime("%H:%M:%S %p", now)
print(f"Start Time: {formatted_time}\n")
start = round(timer(),0)

#establishing locale for US currency 
locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')  

#asks for the amount of money the user would like to input and then round that input to 2 decimal places 
money = round(float(input("Money: ")), 2)

#loops the game 
while True:
    
    #places the bet from the money bank and rounds the input to 2 decimal places. 
    bet = round(float(input("\nBet amount: ")), 2)

    #if the bet is over the money amount, the user will be asked to put in a valid amount equal to or less than the bet 
    if bet > money and bet < 0:
        print("You dont have enough money for that, try again.")
        continue
    else:
        money -= bet 
        # run the dealers program and then yours
        Dcards, Dpoints = dealer()
        Pcards, Ppoints = player()
        #runs the player_turn function 
        Ppoints, Dpoints = players_turn(Pcards, Ppoints, Dcards, Dpoints)

    # compare dealers and players cards for the out put of a win or loss  for black jacks or busts 
    if 21 == sum(Ppoints) and 21 == sum(Dpoints):

        bet = round(bet, 2)
        money += bet 
        money = round(money, 2)

        formatted_money = locale.currency(money, grouping=True)
        formatted_bet = locale.currency(bet, grouping=True)

        print(f"Player's Points: {sum(Ppoints)}\nDealer's Points: {sum(Dpoints)}\n")
        print(
            f"Tie, No One Wins, Total Amount Betted: {formatted_bet}\nTotal Amount You Have: {formatted_money} "
        )

    elif 21 == sum(Ppoints):

        bet *= 1.5
        bet = round(bet, 2)
        money += round(bet, 2)
        money = round(money, 2)

        formatted_money = locale.currency(money, grouping=True)
        formatted_bet = locale.currency(bet, grouping=True)

        print(f"Player's Points: {sum(Ppoints)}\nDealer's Points: {sum(Dpoints)}\n")
        print(
            f"Player wins, Total Amount Won: {formatted_bet}\nTotal Amount You Now Have: {formatted_money} "
        )

    elif 21 == sum(Dpoints):

        bet = round(bet, 2)
        money = round(money, 2)

        formatted_money = locale.currency(money, grouping=True)
        formatted_bet = locale.currency(bet, grouping=True)

        print(f"Player's Points: {sum(Ppoints)}\nDealer's Points: {sum(Dpoints)}\n")
        print(
            f"Dealer wins, Total Amount Lost: {formatted_bet}\nTotal Amount You Now Have: {formatted_money} "
        )

    elif sum(Ppoints) > 21 and sum(Dpoints) > 21:

        bet = round(bet, 2)
        money += bet
        money = round(money, 2)

        formatted_money = locale.currency(money, grouping=True)
        formatted_bet = locale.currency(bet, grouping=True)

        print("Both Players Bust. Draw!")
        print(f"Player's Points: {sum(Ppoints)}\nDealer's Points: {sum(Dpoints)}\n")
        print(
            f"Both players had more than 21, No One Wins, Total Amount Betted: {formatted_bet}\nTotal Amount You Have: {formatted_money} "
        )

    elif sum(Ppoints) > 21:
        # Player busts
        bet = round(bet, 2)
        money = round(money, 2)

        formatted_money = locale.currency(money, grouping=True)
        formatted_bet = locale.currency(bet, grouping=True)

        print("Player busts. Dealer wins!")
        print(f"Player's Points: {sum(Ppoints)}\nDealer's Points: {sum(Dpoints)}\n")
        print(f"Total Amount Lost: {formatted_bet}\nTotal Amount You Now Have: {formatted_money} ")
    elif sum(Dpoints) > 21:
        # Dealer busts
        bet *= 1.5
        bet = round(bet, 2)
        money += round(bet, 2)
        money = round(money, 2)

        formatted_money = locale.currency(money, grouping=True)
        formatted_bet = locale.currency(bet, grouping=True)

        print("Dealer busts. Player wins!")
        print(f"Player's Points: {sum(Ppoints)}\nDealer's Points: {sum(Dpoints)}\n")
        print(f"Total Amount Won: {formatted_bet}\nTotal Amount You Now Have: {formatted_money} ")
    # if no blackjacks or busts we will then run the same checks but for items less than 21 
    else:
        if sum(Ppoints) > sum(Dpoints):

            bet *= 1.5
            bet = round(bet, 2)
            money += round(bet, 2)
            money = round(money, 2)

            formatted_money = locale.currency(money, grouping=True)
            formatted_bet = locale.currency(bet, grouping=True)

            print(f"Player's Points: {sum(Ppoints)}\nDealer's Points: {sum(Dpoints)}\n")
            print(f"Total Amount Won: {formatted_bet}\nTotal Amount You Now Have: {formatted_money} ")
        elif sum(Ppoints) < sum(Dpoints):

            bet = round(bet, 2)
            money = round(money, 2)
            
            formatted_money = locale.currency(money, grouping=True)
            formatted_bet = locale.currency(bet, grouping=True)

            print(f"Player's Points: {sum(Ppoints)}\nDealer's Points: {sum(Dpoints)}\n")
            print(
                f"Dealer wins, Total Amount Lost: {formatted_bet}\nTotal Amount You Now Have: {formatted_money} "
            )

        elif sum(Ppoints) == sum(Dpoints):

            bet = round(bet, 2)
            money += bet 
            money = round(money, 2)
            
            formatted_money = locale.currency(money, grouping=True)
            formatted_bet = locale.currency(bet, grouping=True)

            print(f"Player's Points: {sum(Ppoints)}\nDealer's Points: {sum(Dpoints)}\n")
            print(
                f"Tie, No One Wins, Total Amount Betted: {formatted_bet}\nTotal Amount You Have: {formatted_money} "
            )
    #while loop for the choices to stop or continue 
    while True:
        #checks if you have no money after losing it all lolif you do break
        if money <= 0:
            print("\nNOOO YOU LOST ALL YOUR MONEY :(.\n ")
            break
        else:
            #chekcs if you want to stop or not 
            choice = input("Do you want to play another round? (y/n): ").lower()
            if choice == "n":
                break
            elif choice != "y":
                print("Invalid option. Please enter 'y' or 'n'.")
            else:
                break
    if money <= 0:
        print(f"End Time: {formatted_time}")
        end = round(timer(),0)
        print(f"Elapsed Time: {timedelta(seconds=end-start)}")
        break
    elif choice == "n":
        print("NOOOOOOO :<\n ")
        print(f"End Time: {formatted_time}")
        end = round(timer(),0)
        print(f"Elapsed Time: {timedelta(seconds=end-start)}")
        break
#
