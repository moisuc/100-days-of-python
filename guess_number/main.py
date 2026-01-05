import art
from random import randint


def get_difficulty() -> int:
    """Get number of attempts based on difficulty."""
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    return 10 if difficulty == 'easy' else 5


def get_guess() -> int | None:
    """Get a valid numeric guess from the user."""
    try:
        return int(input("Make a guess: "))
    except ValueError:
        print("Please enter a valid number.")
        return None


def play_game() -> None:
    """Main game loop for number guessing game."""
    print(art.logo)
    print('Welcome to the Number Guessing Game')
    print("I'm thinking of a number between 1 and 100")

    answer = randint(1, 100)
    attempts = get_difficulty()

    for attempt_num in range(attempts):
        remaining = attempts - attempt_num
        print(f"You have {remaining} attempts remaining to guess the number")

        guess = get_guess()
        if guess is None:
            continue

        if guess == answer:
            print(f"You got it! The answer was {answer}")
            return
        elif guess > answer:
            print("Too high.")
        else:
            print("Too low.")

        if attempt_num < attempts - 1:
            print("Guess again")

    print(f"You lose. The answer was {answer}")


def main() -> None:
    """Entry point with replay loop."""
    should_play = True

    while should_play:
        print('\n' * 20)
        play_game()
        play_again = input("\nPlay again? Type 'y' or 'n': ").lower()
        should_play = play_again == 'y'


if __name__ == "__main__":
    main()
