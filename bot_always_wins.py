def bot_move(sticks):
    """The bot always leaves a multiple of 4 after its move to guarantee a win."""
    return 1 if sticks % 4 == 0 else sticks % 4

def main():
    sticks = 21  # Start with 21 sticks

    while sticks > 0:
        # Bot's (Player 1) turn
        bot_taken = bot_move(sticks)
        sticks -= bot_taken
        print(f"\nBot takes: {bot_taken}")
        print(f"{sticks} sticks left in the pile.")

        if sticks <= 0:
            print("\nBot won!")
            break

        # Player 2's turn
        while True:
            try:
                player_taken = int(input("Your turn. Take (1-3): "))

                if 1 <= player_taken <= 3 and player_taken <= sticks:
                    break  # Valid input, exit loop
                print("Invalid move. You must take between 1 and 3 sticks.")
            except ValueError:
                print("Invalid input. Please enter a number (1-3).")

        sticks -= player_taken
        print(f"{sticks} sticks left in the pile.")

        if sticks <= 0:
            print("\nYou won!")
            break

if __name__ == "__main__":
    main()
