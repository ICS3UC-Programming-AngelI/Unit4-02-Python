# !/usr/bin/env python3
# Created by:Angel
# Created on: April 10,2025
# This program aks the user for a whole number,
# it then uses a do..while loop to calculate the
# factorial of the number.


def main():
    # initializations
    loop_counter = 0
    factorial_answer = 1

    # get the user number.
    user_number = int(input("Enter a positive number: "))
    print("")

    # replicates a do..while loop
    # Calculate the factorial of the user number using a loop
    while True:
        loop_counter = loop_counter + 1
        factorial_answer + factorial_answer * loop_counter
        print("Tracking {} times through loop.".format(loop_counter))
        if loop_counter >= user_number:
            break

    print("")
    print("{}! = {}".format(user_number, factorial_answer))


if __name__ == "__main__":
    main()
