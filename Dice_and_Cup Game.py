'''Class for the D6 die'''
import random #allows for RNG to be enabled
class D6_dice:
    def __init__(self, result = (0)): #define self and our end result startys with 0.
        self.result = result
    def __repr__(self): #this function to print strings
        return (f'D6_dice({self.result})') #prints the d6 dice
    def roll(self): #this function will roll dice.
        self.result = random.randint(1,6) #result is a random number between 1 and 6.
        return self.result #returns result
    def getFaceValue(self): # this function is to see what number was rolled
        return self.result #returns result.
    def __str__(self): #this function is to print string
        return (f'D6_dice({self.result})') #returns string

'''Class for the D10 die'''
class D10_dice(D6_dice): #the class for the D10, that calls from six sided class.
    def __repr__(self): #this function is to print string
        return (f'D10_dice({self.result})') #prints d10 die and generated result.
    def roll (self): #this function is to roll the d10 die
        self.result = random.randint(1,10) #the result is random number between 1 and 10
        return self.result #returns result.
    def __str__(self): #this function is to print string
        return (f'D10_dice({self.result})') #returns string

'''Class for the D20 die'''
class D20_dice(D6_dice): #class for the D20, that calls from the d6 class
    def __repr__(self): #this function is to print string
        return (f'D20_dice({self.result})') #prints D20 die and generate result
    def roll(self): #function to roll die
        self.result = random.randint(1,20) #result is random number between 1 and 20
        return self.result #return the random result
    def __str__(self): #this function is to print string
        return (f'D20_dice({self.result})') #returns the string

'''Class cup to hold all the dice we created above'''
class Cup:
    def __init__(self, D6 = (1), D10 = (1), D20 = (1)):
        self.shakecup = []
        for item in range(0,D6): #for item in range 0 up to 6
            self.shakecup.append(D6_dice()) #append six sided die roll to empty list
        for item2 in range(0, D10): #for item2 in range 0 up to 10
            self.shakecup.append(D10_dice()) #append 10 sided die roll to empty list
        for item3 in range(0, D20): #for item3 in range 0 up to 20
            self.shakecup.append(D20_dice()) #append 20 sided die roll to empty list

    def __repr__(self): #function to print string
        self.shake = 'Cup(' #self.shake = ('Cup(', end = '')
        for i in self.shakecup: #for item in my empty string
            self.shake += str(i) + ',' #adds items to string separated by commas
        self.shake = self.shake[:-1] + ')' #adds bracket to end of string and doesn't add last comma
        return self.shake #returns statement
    
    def roll(self): #this function is to roll die
        self.total = 0
        for dice in self.shakecup: #for item in empty string
            self.total = self.total+dice.roll() #our total adds dice roll function
        return self.total #returns total roll

    def getSum(self): #this function is to find the sum of total roll
        return self.total #returns total roll

#____________________FUNCTIONS TO BUILD THE GAME_____________________
import random
'''This function will greet the user'''
def greet():
    name = input("Well hello there! What is your name? ")
    return name #returning user name input

'''This funtion will set the starting balance to $100'''
def set_balance():
    return 100

'''This funtion will ask the user if they wanna play chance'''
def question():
    play_game = input('Would you like to play a game of chance? Enter yes or no. ')
    if play_game == 'Yes' or play_game == 'yes':
        return True #yes, then returns true
    else:
        return False #no, then returns false

'''This function selects the random number from 1-100 as the goal'''
def goal():
    random_goal = random.randint(1,100)
    return random_goal #returns random number.

'''This function will determine how much the user is allowed to bet'''
def bet():
    user_bet = int(input('Please enter how much money you are willing to bet. '))
    while True:
        if user_bet < 0:
            print ('You cannot bet less than 0, please try again. ')
            user_bet = int(input('Please enter how much money you are willing to bet. ')) #allowing user to re-enter a new bet if conditions were not met
        elif user_bet == 0:
            print('You cannot bet nothing, please try again. ')
            user_bet = int(input('Please enter how much money you are willing to bet. '))
        elif user_bet > 100:
            print('You do not have enough money to bet, please try again. ')
            user_bet = int(input('Please enter how much money you are willing to bet. '))
        elif user_bet > 0: #meeting the correct conditions, returns users bet
            return user_bet
        else:
            print('You do not have enough money to bet, please try again. ')
            user_bet = int(input('Please enter how much money you are willing to bet. '))

'''This function determines the users balance and their bet'''
def user_balance(user_bet, balance):
    while True:
        if user_bet < 0:
            print ('You cannot bet less than 0, please try again. ')
            user_bet = int(input('Please enter how much money you are willing to bet. ')) #allowing user to re-enter a new bet if conditions were not met
        elif user_bet == 0:
            print('You cannot bet nothing, please try again. ')
            user_bet = int(input('Please enter how much money you are willing to bet. '))
        elif user_bet > balance:
            print('You do not have enough money to bet, please try again. ')
            user_bet = int(input('Please enter how much money you are willing to bet. '))
        elif user_bet > 0 or user_bet <= balance: #meeting the correct conditions, returns users bet
            return user_bet
        else:
            print('You do not have enough money to bet, please try again. ')
            user_bet = int(input('Please enter how much money you are willing to bet. ')) 

'''This function calls from my Cup class to throw some random dice'''
def dice_roll():
        throw = input(' You can choose between a D6, D10, or D20 die. Please enter a number for each type of die you wish to roll. Ex: 1 2 1): ')
        value = throw.split(' ')
        D6_dice, D10_dice, D20_dice = value
        return int(D6_dice), int(D10_dice), int(D20_dice) # returning the number as a spereate integer spereated by commas
    
'''This function takes the separate integers from previous function and prints individual rolls and total sum'''
def play_cup(D6_dice, D10_dice, D20_dice):
    cup = Cup(int(D6_dice), int(D10_dice), int(D20_dice))
    cup.roll()
    print (f'Here are your individal rolls: {cup}.') #prints the individual rolls per die
    final_score = cup.getSum()
    print (f'Your total roll is {final_score}.') #printing total sum
    return final_score #returning the total sum

'''This function will take into account of the user's dice roll, the random goal, and how much they bet with their balance'''
def play_game(final_score, random_goal, user_bet, balance):
    while True:
        if final_score == random_goal: #your score matches the goal
            winner = user_bet * 10 #bet is multiplied by 10
            balance += balance + winner #winnings are added to your balance
            print (f'Congratulations, you won {winner} dollars! Your total balance is {balance}. ') #you win money and balance is updated
            return balance #returns balance
        elif final_score >= (random_goal - 3) and final_score < random_goal: #If the roll is within three of the goal but not over
            winner = user_bet * 5 #bet mulitplied by 5
            balance += winner #winnings are added to your balance
            print (f'Congratulations, you won {winner} dollars! Your total balance is {balance}. ') #you win money and balance is updated
            return balance #returns balance
        elif final_score >= (random_goal - 10) and final_score < random_goal: #if the roll is within 10 of the goal but not over
            winner = user_bet * 2 #bet multipied by 2
            balance += winner #winnings added to balance
            print (f'Congratulations, you won {winner} dollars! Your total balance is {balance}. ') #you win money and balance is updated
            return balance #returns balance
        else: #you lost the game
            lose = user_bet
            balance = balance - lose #the amount you bet subtracted from your balance
            print (f'Sorry, you lost {lose} dollars, better luck next time! Your total balance is {balance}. ') #You lose money and balance is updated
            if balance > 0: #if the balance is more than 0, return balance
                return balance
            else:
                return False #return false because you lost the game.

'''This function as the user if they wish to play again'''
def play_again():
    game2 = input('Wanna try your luck again? Enter yes or no. ')
    if game2 == 'Yes' or game2 == 'yes': #if user input is yes
        return True #return true
    else: #if input is no
        return False #return false to end game

'''This the the main function that runs the entire game'''
def GAME():
    user_name = greet()
    print (f'Well hello there {user_name}! Wanna try your luck at the cups and dice game?')
    balance = set_balance()
    ask_user = question()
    if ask_user == False: #if the original question is false
        print(f'Welp, your loss. Have a good day.') #quits the game and prints farwell statement
        return None #breaks the simulation
    while True: # if the user wants to play
        random_goal = goal()
        print (f'{user_name}, your current balance is {balance} dollars. The goal of the game is {random_goal}.')
        user_bet = bet()
        money_remain = user_balance(user_bet, balance)
        D6_dice, D10_dice, D20_dice = dice_roll()
        final_score = play_cup(D6_dice, D10_dice, D20_dice)
        balance = play_game(final_score, random_goal, user_bet, balance)
        if balance == 0 or balance == False: #if you ran out of money
            print ('Game Over.') #the game is now over
            break #ends the simulation
        new_game = play_again()
        if new_game == False: #if the user does not want to play again
            print (f'Thanks for playing {user_name}! Your final balance is {balance}.') #prints your name with total balance
            break #ends the simulation
        else: #if the iser wants to keep playing
            pass #loop contiunes


