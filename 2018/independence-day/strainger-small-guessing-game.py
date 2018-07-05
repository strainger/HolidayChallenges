# Python 2 small guessing game, strainger
import random;
max=random.randint(10,20);
guess_game = lambda guess, number, attempt, attempts, message, max, validate: guess_game(validate(raw_input(message(guess, number) + "Please guess a number between 1 and " + str(max) + " (attempt " + str(attempt) + "/" + str(attempts) + "): ")), number, attempt+1, attempts, message, max, validate) if guess != number and attempt <= attempts else "The number was: " + str(number)
print guess_game(0, random.randint(1,max), 1, random.randint(7,max), lambda x,y: "" if x == 0 else "Too high. " if x > y else "Too low. ", max,lambda a: int(a) if a.isdigit() else 0)
