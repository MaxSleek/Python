import random


# a player has a name (string), and a score(int)
class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def get_name(self):
        return self.name

    def get_score(self):
        return self.score

    def set_name(self, name):
        self.name = name

    def set_score(self, score):
        self.score = score


# gets the puzzles in the game from a file
# returns the puzzles in a variable named wheel_puzzles
# wheel_puzzles is a list
def get_wheel_puzzles():
    global wheel_puzzles
    wheel_puzzles = []
    with open("/Users/msleek04/Desktop/Code/Python (COMP 116)/PycharmProjects/WheelOfFortune/venv/puzzles.txt", "r") as file:
        for line in file:
            line = line.strip()
            wheel_puzzles.append(line)
    return wheel_puzzles


# get the wheel values in the game from a file
# returns the wheel values in a variable named wheel_values
# wheel_puzzles is a list
def get_wheel_values():
    global wheel_values
    wheel_values = []
    with open("/Users/msleek04/Desktop/Code/Python (COMP 116)/PycharmProjects/WheelofFortune/venv/wheel_values.txt", "r") as file:
        for line in file:
            line = line.strip()
            wheel_values.append(line)
    return wheel_values


# takes wheel_puzzles as a parameter, it's type is list
# randomly chooses a puzzle and returns that puzzle - it returns a string
def choose_puzzle(wheel_puzzles):
    global random_puzzle
    random_puzzle = random.choice(wheel_puzzles)
    return random_puzzle


# takes wheel_values as a parameter, it's type is list
# randomly chooses a value and returns that value - it returns an int
def spin_wheel(wheel_values):
    number = random.randint(0, len(wheel_values) - 1)
    return wheel_values[number]



# determines who should be the current_player
# and returns the current_player
# current_player is a Player object
# player_1 is a Player object
# player_2 is a Player object
# player 3 is a Player object
def change_player(current_player, player1, player2, player3):
    if current_player == player1:
        current_player = player2
    elif current_player == player2:
        current_player = player3
    else:
        current_player = player1
    return current_player


# computes the score for the current_player
# returns the score, an int
# multiples the number_of_times_a_letter_in_word by the spin value to get the score
def compute_player_score(current_player, number_of_times_a_letter_in_word, spin_value):
    global score
    score = current_player.get_score() + (number_of_times_a_letter_in_word * int(spin_value))
    return score


# user_guess is the letter the user guessed
# puzzle is the random puzzle chosen
# This functions returns True if the user_guess is in the puzzle
# This functions returns False if the user_guess is NOT in the puzzle
def is_guess_in_puzzle(user_guess, puzzle):
    if user_guess.lower() in puzzle.lower():
        return True

    return False


# random_puzzle is a puzzle (the puzzle is a string)
# converts each letter in the random puzzle into an underscore (_)
# and returns the string (with underscores) as solved_p
def turn_puzzle_into_underscores(random_puzzle):
    global random_puzzle_with_underscores
    random_puzzle_with_underscores = list()
    for character in random_puzzle:
        if character == " ":
            random_puzzle_with_underscores.append(" ")
        else:
            random_puzzle_with_underscores.append("_")

    return ''.join(random_puzzle_with_underscores)


# for example, if this is the first time a user has guessed a letter
# letter = "H" (letter the user guessed)
# random_puzzle = "Hey there"
# solve_puzzle  = "___ _____"
# puzzle_with_characters_and_underscores = "H__ _____"
def show_letter_in_solved_puzzle(letter, solved_puzzle, random_puzzle):
    global puzzle_with_characters_and_underscores
    index = 0
    solved_puzzle = list(solved_puzzle)
    for letter_in_random_puzzle in random_puzzle:
        if letter_in_random_puzzle.lower() == letter.lower():
            solved_puzzle[index] = letter_in_random_puzzle

        index += 1
    puzzle_with_characters_and_underscores = ''.join(solved_puzzle)
    return puzzle_with_characters_and_underscores


# determines if the user's guess is in the puzzle
# user_guess is the letter the user guessed
# puzzle is the puzzle (no underscores)
# user_guess = t
# puzzle = "Cat in the Hat"
# returns 3
def count_number_of_times_in_puzzle(user_guess, puzzle):
    puzzle = puzzle.lower()
    user_guess = user_guess.lower()
    return puzzle.count(user_guess)


# solved_puzzle is the puzzle with underscores and guessed letters
# this function returns True if there are still letters to guess
# it returns False if there are no letters left to guess
# solved_puzzle = "__t __ t__ __t"
# solved_puzzle = "Cat in the hat"
def are_letters_left_to_guess(solved_puzzle):
    if "_" in solved_puzzle:
        return True

    return False

def main():
    get_wheel_puzzles()
    get_wheel_values()
    choose_puzzle(wheel_puzzles)
    player1 = Player(input("Player 1 please enter your name:"), 0)
    player2 = Player(input("Player 2 please enter your name:"), 0)
    player3 = Player(input("Player 3 please enter your name:"), 0)
    random_puzzle_with_underscores = turn_puzzle_into_underscores(random_puzzle)
    current_player = player1
    while are_letters_left_to_guess(random_puzzle_with_underscores) == True:
        print(current_player.get_name())
        print("You have", current_player.get_score(), "dollars")
        print("The puzzle is:", random_puzzle_with_underscores)
        user_input = input("Would you like to spin (input spin) or solve (input solve)? ")
        while user_input == "spin":
            spin = spin_wheel(wheel_values)
            print("Your spin is:", spin)
            user_guess = input("Please guess a vowel or consonant:")
            if is_guess_in_puzzle(user_guess, random_puzzle) == True:
                if user_guess in random_puzzle_with_underscores:
                    print("That letter has already been guessed.")
                    user_input = input("Would you like to spin (input spin) or solve (input solve)? ")
                else:
                    print("Your letter is in the puzzle!")
                    compute_player_score(current_player, count_number_of_times_in_puzzle(user_guess, random_puzzle), spin)
                    current_player.set_score(score)
                    random_puzzle_with_underscores = show_letter_in_solved_puzzle(user_guess,
                                                                                  random_puzzle_with_underscores,
                                                                                  random_puzzle)
                    if random_puzzle_with_underscores == random_puzzle:
                        print("You win!")
                        print("You won", current_player.get_score(), "dollars total!")
                        user_input = "gameover"
                    else:
                        print(current_player.get_name(), ", you now have", current_player.get_score(), "dollars")
                        print("The puzzle is now:", random_puzzle_with_underscores)
                        user_input = input("Would you like to spin (input spin) or solve (input solve)? ")
            else:
                print("Your letter is not in the puzzle.")
                current_player = change_player(current_player, player1, player2, player3)
                print(current_player.get_name())
                print("You have", current_player.get_score(), "dollars")
                print("The puzzle is:", random_puzzle_with_underscores)
                user_input = input("Would you like to spin (input spin) or solve (input solve)? ")
        if user_input == "solve":
            user_guess = input("Enter the letters of the puzzle (Case Sensitive):")
            if user_guess == random_puzzle:
                print("You win!")
                print("You won", current_player.get_score(), "dollars total!")
                random_puzzle_with_underscores = user_guess
            else:
                print("Your guess was incorrect.")
                current_player = change_player(current_player, player1, player2, player3)
        if user_input == "gameover":
            random_puzzle_with_underscores == random_puzzle
    print("The phrase was:", random_puzzle)

main()