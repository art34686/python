import random
import sys
import time

def print_slow(text, delay=0.03):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def welcome():
    print("="*50)
    print("   Welcome to the Number Guessing Game!")
    print("="*50)
    print()
    print("Choose your difficulty level:")
    print("1. Easy (Number 1-20, 10 attempts)")
    print("2. Medium (Number 1-50, 7 attempts)")
    print("3. Hard (Number 1-100, 5 attempts)")
    print()

def get_difficulty():
    while True:
        choice = input("Enter difficulty (1, 2, or 3): ").strip()
        if choice == '1':
            return 'Easy', 1, 20, 10
        elif choice == '2':
            return 'Medium', 1, 50, 7
        elif choice == '3':
            return 'Hard', 1, 100, 5
        else:
            print("Invalid input. Please enter 1, 2 or 3.")

def get_user_guess(attempt, max_attempts):
    while True:
        try:
            guess = int(input(f"Attempt {attempt}/{max_attempts} - Enter your guess: "))
            return guess
        except ValueError:
            print("Please enter a valid integer.")

def play_again():
    while True:
        again = input("Would you like to play again? (y/n): ").strip().lower()
        if again in ['y','yes']:
            return True
        elif again in ['n','no']:
            return False
        else:
            print("Please enter y or n.")

def main():
    welcome()
    while True:
        level, low, high, max_attempts = get_difficulty()
        target = random.randint(low, high)
        print()
        print_slow(f"You chose {level}! I have selected a number between {low} and {high}.")
        print(f"You have {max_attempts} attempts to guess it. Good luck!\n")

        for attempt in range(1, max_attempts + 1):
            guess = get_user_guess(attempt, max_attempts)
            if guess == target:
                print_slow(f"\n🎉 Congratulations! You guessed the number {target} correctly in {attempt} attempts!")
                score = max_attempts - attempt + 1
                print(f"Your score: {score} points\n")
                break
            elif guess < target:
                print("Your guess is too low.")
            else:
                print("Your guess is too high.")

            # Give a subtle hint at half attempts
            if attempt == max_attempts // 2:
                hint_range_low = max(low, target - 5)
                hint_range_high = min(high, target + 5)
                print_slow(f"Hint: The number is between {hint_range_low} and {hint_range_high}")

        else:
            print_slow(f"\n😞 You've used all your attempts. The number was {target}. Better luck next time!")
            print("Score: 0 points\n")

        if not play_again():
            print_slow("\nThanks for playing the Number Guessing Game! Goodbye! 👋")
            break

if __name__ == "__main__":
    main()


