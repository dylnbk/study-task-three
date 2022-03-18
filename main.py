from collections import Counter
import random

"""
    first create a dict for each hero, nest the winning / losing messages
    into their own dict and then make a list for the player names.

    next create a function that takes the number of rounds the user wants
    to play and ensures it's an odd number and a minimum of 3 rounds.

    third, a function to take the input of the user and computer and return
    a hero. these values can be used to match with the entries in the dict

    next a stat function that takes how many times a hero wins/loses and
    sorts then outputs the results

    the game module function takes arguments and creates a print statement
    to be used at the end of each round

    lastly the main body of the code. it takes various user input and has
    all of the required loops, calls and outputs
"""

# create a dictionary that contains each hero and their winning messages
battle = {
    "Spiderman": {
        1:
            {"Storm": "\nSpiderman entangles Storm in a web!",
             "Green Lantern": "\nSpiderman steals Green Lanterns ring!",
             "Batman": "\nSpiderman outmaneuvers Batman and traps him in a web!"},
        2:
            {"Wonder Woman": "\nWonder Woman crushes Spiderman!",
             "Hulk": "\nHulk smashes Spiderman!",
             "Iron Man": "\nIron Man overpowers Spiderman"}},
    "Wonder Woman": {
        1:
            {"Spiderman": "\nWonder Woman crushes Spiderman!",
             "Hulk": "\nWonder Woman smacks Hulk into last week!",
             "Batman": "\nWonder Woman destroys Batman"},
        2:
            {"Storm": "\nStorm projects a tornado against Wonder Woman!",
             "Green Lantern": "\nGreen Lantern traps Wonder Woman in a pocket dimension!",
             "Iron Man": "\nIron Man engineers a new weapon and tests it on Wonder Woman"}},
    "Storm": {
        1:
            {"Wonder Woman": "\nStorm projects a tornado against Wonder Woman!",
             "Hulk": "\nStorm beats Hulk in a fair fight!",
             "Iron Man": "\nStorm engulfs Iron Man in a barrage of lighting"},
        2:
            {"Spiderman": "\nSpiderman entangles Storm in a web!",
             "Green Lantern": "\nGreen Lantern removes Storms Gauntlet and beats her with it!",
             "Batman": "\nBatman seduces Storm and traps her in his bat cave"}},
    "Green Lantern": {
        1:
            {"Wonder Woman": "\nGreen Lantern traps Wonder Woman in a pocket dimension!",
             "Storm": "\nGreen Lantern removes Storms Gauntlet and beats her with it!",
             "Batman": "\nGreen Lantern quickly disables Batman"},
        2:
            {"Spiderman": "\nSpiderman steals Green Lanterns ring!",
             "Hulk": "\nHulk sucker punches Green Lantern!",
             "Iron Man": "\nIron Man outsmarts Green Lantern"}},
    "Hulk": {
        1:
            {"Spiderman": "\nHulk smashes Spiderman!",
             "Green Lantern": "\nHulk sucker punches Green Lantern!",
             "Iron Man": "\nHulk rips apart Iron Man in a rage"},
        2:
            {"Wonder Woman": "\nWonder Woman smacks Hulk into last week!",
             "Storm": "\nStorm beats Hulk in a fair fight!",
             "Batman": "\nBatman radiates Hulk with a calming frequency"}},
    "Iron Man": {
        1:
            {"Spiderman": "\nIron Man overpowers Spiderman",
             "Wonder Woman": "\nIron Man engineers a new weapon and tests it on Wonder Woman",
             "Green Lantern": "\nIron Man outsmarts Green Lantern"},
        2:
            {"Hulk": "\nHulk rips apart Iron Man in a rage",
             "Storm": "\nStorm engulfs Iron Man in a barrage of lighting",
             "Batman": "\nBatman steals Iron Man technology and uses it against him"}},
    "Batman": {
        1:
            {"Iron Man": "\nBatman steals Iron Man technology and uses it against him",
             "Hulk": "\nBatman radiates Hulk with a calming frequency",
             "Storm": "\nBatman seduces Storm and traps her in his bat cave"},
        2:
            {"Green Lantern": "\nGreen Lantern quickly disables Batman",
             "Spiderman": "\nSpiderman outmaneuvers Batman and traps him in a web!",
             "Wonder Woman": "\nWonder Woman destroys Batman"}}}


# create lists for player names and stat counting
c_list = ["Jan", "Clay", "Lukel", "Andy", "Adam", "Ayshea", "Paul", "Chris"]
p_list = ["Jack", "Richard", "Pheobe", "Peter", "Renee", "Dominic", "Josie"]
w_stats = []
l_stats = []


# a function that makes sure the correct number of rounds are used
def rounds():

    # request the desired number of rounds from the player
    round_choice = input("\nHow many rounds do you wish to play?\n")

    # if the user does not enter a value, force the number of rounds to 3
    if round_choice.isdigit() is not True:
        round_choice = 3

    else:
        # cast the input to an integer
        round_choice = int(round_choice)

        # if less than 3 rounds selected force number of rounds to 3
        if round_choice < 3:
            round_choice = 3

        # if number of rounds divided by 2 leaves 0 remaining, add 1 to ensure odd number
        elif round_choice % 2 == 0:
            round_choice += 1

    # return the result
    return round_choice


# this takes user/computer selection and returns a hero, if none selected returns false
def char_select(char_choice):

    if char_choice == "1" or char_choice == "spiderman":
        return "Spiderman"

    elif char_choice == "2" or char_choice == "wonder woman":
        return "Wonder Woman"

    elif char_choice == "3" or char_choice == "storm":
        return "Storm"

    elif char_choice == "4" or char_choice == "green lantern":
        return "Green Lantern"

    elif char_choice == "5" or char_choice == "hulk":
        return "Hulk"

    elif char_choice == "6" or char_choice == "iron man":
        return "Iron Man"

    elif char_choice == "7" or char_choice == "batman":
        return "Batman"

    else:
        return False


# provide game statistics
def stats(win, lose):

    # create dicts from list, hero as key and win / loss amount as value
    winners = Counter(win)
    losers = Counter(lose)

    # use dict comprehension to sort the entries
    win_s = {key: val for key, val in sorted(winners.items(), key=lambda sort: sort[1], reverse=True)}
    lose_s = {key: val for key, val in sorted(losers.items(), key=lambda sort: sort[1], reverse=True)}

    # output stats using for loops to iterate over the sorted dicts
    print("\nWinning hero stats:")

    for hero, total in win_s.items():
        print(f"{hero} wins: {total}")

    print("\nLosing hero stats:")

    for hero, total in lose_s.items():
        print(f"{hero} loses: {total}")


# takes a number of arguments and uses the data to print a statement
def game_module(char, comp, p_score, c_score, msg, name_a, name_b):

    print(f"\n{name_a} chooses: {char}\
            \n{name_b} chooses: {comp}\
            \n{msg}\
            \n\n{name_a} has scored: {p_score}\
            \n{name_b} has scored: {c_score}")


# main body of code
def main():

    # create a variable for main while loop condition
    play_again = "y"

    # player and computer total number of won games
    p_total, c_total, = 0, 0

    # global rounds won, lost, tied
    pr_total, cr_total, d_total = 0, 0, 0

    # global total number of rounds played
    gr_total = 0

    # welcome message and take player name input
    p_name = input("\nWelcome to the Hero Battle game!\
                   \n\nPlease enter your name:\n").title()

    # randomize the computers name from the list created earlier
    c_name = c_list[random.randint(0, 6)]

    # if the user does not enter a name, one is randomly chosen for them
    if "" == p_name:
        p_name = p_list[random.randint(0, 6)]

    # while the player has responded yes to 'play again', the loop will execute
    while play_again[0] == "y":

        # create variables for round total, round counter, player and computer scores
        r_total, r_count = rounds(), 0
        p_score, c_score = 0, 0

        # if the player score is less than the total rounds divided by 2
        # the game is not over and loop will continue to execute
        while p_score < r_total / 2 and c_score < r_total / 2:

            # store the computer and players hero selection
            c_choice = char_select(str(random.randint(1, 5)))
            p_choice = char_select(input("\nPlease choose your hero:\
            \n1. Spiderman\n2. Wonder Woman\n3. Storm\n4. Green Lantern\
            \n5. Hulk\n6. Iron Man\n7. Batman\n\n").lower())

            # if player enters an invalid selection, char_select will return
            # False and error message displayed, no points/rounds are added
            if not p_choice:
                print("\nError, please choose a valid character")

            else:

                # add 1 to the global number of rounds played
                gr_total += 1

                # if the player choice is the same as the computer the round will
                # be a draw, no points/rounds are added
                if p_choice == c_choice:
                    d_total += 1
                    print(f"\n{p_choice} fights... {c_choice}, it ends in a draw.")

                else:

                    # as the below are valid scoring outcomes we can add 1 to round counter
                    # create variable that contains the dict paired to the players hero choice
                    r_count += 1
                    fight = battle[p_choice]

                    # loop through the dictionary and then check the player choice vs computer
                    for x, y in fight.items():
                        if x == 1:

                            # if computer hero is found here the round is won by the player
                            for key, value in y.items():
                                if key == c_choice:

                                    # add 1 to player score, output round results and stats
                                    w_stats.append(p_choice)
                                    l_stats.append(c_choice)
                                    p_score += 1
                                    pr_total += 1
                                    game_module(p_choice, c_choice, p_score,
                                                c_score, value, p_name, c_name)
                                    print(f"\n{p_choice} wins, you gain a point!")

                        elif x == 2:

                            # if computer hero is found here the round is won by the computer
                            for key, value in y.items():
                                if key == c_choice:

                                    # add 1 to computer score, output round results and stats
                                    w_stats.append(c_choice)
                                    l_stats.append(p_choice)
                                    c_score += 1
                                    cr_total += 1
                                    game_module(p_choice, c_choice, p_score,
                                                c_score, value, p_name, c_name)
                                    print(f"\n{c_choice} wins, {c_name} gains a point!")

        # compare player / computer score and print a message
        if p_score > c_score:
            p_total += 1
            print(f"\n--- Game Over ---\
            \n\nCongratulations {p_name}, you win!")

        else:
            c_total += 1
            print("\n--- Game Over ---\
            \n\nUnlucky, you lose!")

        # ask if the player would like another game and overwrite 'play again' variable
        play_again = input("\nWould you like to play again?\n").lower()

    # output final game statistics
    print("\n------------------------------\n\nGame breakdown:")
    stats(w_stats, l_stats)
    print(f"\nRound stats:\nTotal number of rounds played: {gr_total}\
            \n{p_name} won: {pr_total}\n{c_name} won: {cr_total}\nDraw: {d_total}\
            \n\nGame stats:\nTotal number of games played: {p_total + c_total}\
            \n{p_name} won: {p_total}\n{c_name} won: {c_total}\
            \n\nThanks for playing!")


# initiate the game by calling the main function
main()
