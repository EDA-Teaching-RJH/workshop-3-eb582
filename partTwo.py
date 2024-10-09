import random
secret_number = random.randint(1,10)
guess = int(input("Iv thought of a random number between 1 and 10 try and guess it! "))
if secret_number == guess: print("Well Done you guessed coreectly my number was ", secret_number )
if secret_number > guess: print("Too bad your guess was too low my number was ", secret_number)
else : print("Too bad your guess was too high my number was ", secret_number)