#!/usr/bin/env python3

# Created by: Chris Di Bert
# Date: Dec.23 2022
# This program takes a list of numbers
# and prints the numbers that are perfect squares


def find_perfect_squares(numbers):
    # Empty list to store the perfect squares
    perfect_squares = []

    # Iterates through each number in the user's list of numbers
    for number in numbers:
        # Checks if the number is a perfect square
        multiplier = 0
        while multiplier * multiplier <= number:
            if multiplier * multiplier == number:
                # If it is, add it to the list of perfect squares
                perfect_squares.append(number)
                break
            multiplier += 1

    # Returns all perfect squares after the list has
    # been iterated through
    return perfect_squares


def main():

    while True:

        # Asks the user if they would like to read from a file
        input_choice = input(
            "Would you like to read data from a .txt file? (y/n): "
        ).lower()

        # If the user wants to read from a .txt file
        if input_choice == "y":
            # Gets the directory of the .txt file
            print("Enter the directory of the text file")
            user_dir = input(">> ").replace("\\", "/")

            # Reads the file at the specified directory
            try:
                with open(user_dir, "r") as f:
                    numbers_str = list(
                        f.read().split()
                    )  # Reads the contents of the .txt file
                    user_numbers_float = [
                        float(x) for x in numbers_str
                    ]  # Casts contents from str to int

            # If the user entered an invalid directory
            except:
                print(
                    "You did not enter a valid directory.\nYou may have also entered a non-numeric value in the text file."
                )
                input("Enter any key to try again: ")

        # If the user does not want to read from a file
        else:
            # Asks the user to enter a list of numbers
            user_numbers_str = input(
                "Enter a list of numbers separated by spaces: "
            ).split()

            try:
                user_numbers_float = [float(number) for number in user_numbers_str]
            except:
                print("You must only enter numbers.")
                continue

        # Passes user's numbers to perfect square function and prints the result
        perfect_squares = find_perfect_squares(user_numbers_float)
        print("The following numbers are perfect squares:", perfect_squares)

        # Asks the user if they would like to restart
        user_restart = input("Would you like to restart? (y/n): ").lower()
        if user_restart == "":
            continue
        elif user_restart[0] == "n":
            break


if __name__ == "__main__":
    main()
