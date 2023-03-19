import random
total_guesses = 0
rng = random.randint(1, 10000)
print(rng)
closest_lower_guess, closest_higher_guess = 0, 10000
while True:
    old_clg = closest_lower_guess
    old_chg = closest_higher_guess
    guess = int(input(f"Guess a number between {closest_lower_guess} and {closest_higher_guess}: "))
    total_guesses += 1
    if (guess < rng):
        closest_lower_guess = min(closest_lower_guess, guess, key=lambda x: abs(x - rng))
    elif (guess > rng) :
        closest_higher_guess = min(closest_higher_guess, guess, key=lambda x: abs(x - rng))
    else:
        break
    if (old_clg != closest_lower_guess or old_chg != closest_higher_guess):
        print("Getting closer! Bounds updated.")
    else:
        print("Why would you guess this")
print(f"Well done! You got it in {total_guesses} guesses")

