def main():
    total_sticks = 21
    print(f"{total_sticks} sticks in the pile.")
    while total_sticks > 0:
        while True:
            try:
                player_1 = int(input("Player 1 takes: "))
                if player_1 > 1 and player_1 > 3:
                    print("Invalid Input. Enter number between 1-3.")
                    continue
                else:
                    total_sticks -= player_1
                    print(f"{total_sticks} sticks in the pile.")
                    break
            except ValueError:
                print("Invalid Input. Enter numeric value 1-3")

        if total_sticks <= 0:
            print("Player 1 won!")
            break

        while True:
            try:
                player_2 = int(input("Player 2 takes: "))
                if player_2 > 1 and player_2 > 3:
                    print("Invalid Input. Enter number between 1-3.")
                    continue
                else:
                    total_sticks -= player_1
                    print(f"{total_sticks} sticks in the pile.")
                    break
            except ValueError:
                print("Invalid Input. Enter numeric value 1-3")

        if total_sticks <= 0:
            print("Player 2 won!")
            break


if __name__ == "__main__":
    main()





