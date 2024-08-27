"""
Script Name: Weighing ball puzzle solver
Author: Kenneth Plum Toft   
Date: 2024-08-27
Description: This python script given a number of the odd ball and wether the odd ball is light or heavy, 
can then find the odd ball and tell if it is heavier or lighter assuming it doesnt know the input. The script will 
log the steps taken, thus help the user understand the algorithm used to solve this problem.
A problem solution can be found at: https://www.mathsisfun.com/pool_balls_solution.html
"""
import random

def weigh(group1, group2):
    if group1 == group2:
        return "balance"
    elif group1 > group2:
        return "left"
    else:
        return "right"

def ball_puzzle(odd_ball, odd_type):
    if not 1 <= odd_ball <= 12:
        print("Invalid input for odd_ball. Please enter a number between 1 and 12.")
        return
    
    normal_weight = 1
    if odd_type == "heavy":
        odd_weight = 2
    elif odd_type == "light":
        odd_weight = 0
    else:
        print("Invalid input for odd_type. Please enter 'heavy' or 'light'.")
        return
    
    # Step 1: Weighing [1, 2, 3, 4] vs [5, 6, 7, 8]
    print("\nStep 1: Weighing [1, 2, 3, 4] vs [5, 6, 7, 8]")
    result1 = weigh([odd_weight if x == odd_ball else normal_weight for x in [1, 2, 3, 4]],
                    [odd_weight if x == odd_ball else normal_weight for x in [5, 6, 7, 8]])
    
    if result1 == "balance":
        # Case 1: The odd ball is among [9, 10, 11, 12]
        print("The scales balance, so the odd ball is in [9, 10, 11, 12].")
        print("\nStep 2: Weighing [6, 7, 8] vs [9, 10, 11]")
        result2 = weigh([normal_weight, normal_weight, normal_weight],
                        [odd_weight if x == odd_ball else normal_weight for x in [9, 10, 11]])
        
        if result2 == "balance":
            print("The scales balance again, so 12 is the odd ball.")
            print("\nStep 3: Weighing 12 against any other ball.")
            print(f"The odd ball is 12 and it is {odd_type}.")
        elif result2 == "right":
            print("9, 10, 11 side is heavier, so one of them is heavy.")
            print("\nStep 3: Weighing 9 vs 10.")
            result3 = weigh([odd_weight if 9 == odd_ball else normal_weight],
                            [odd_weight if 10 == odd_ball else normal_weight])
            if result3 == "balance":
                print("9 and 10 balance, so 11 is the odd heavy ball.")
            elif result3 == "left":
                print("9 is heavier, so 9 is the odd heavy ball.")
            else:
                print("10 is heavier, so 10 is the odd heavy ball.")
        else:
            print("9, 10, 11 side is lighter, so one of them is light.")
            print("\nStep 3: Weighing 9 vs 10.")
            result3 = weigh([odd_weight if 9 == odd_ball else normal_weight],
                            [odd_weight if 10 == odd_ball else normal_weight])
            if result3 == "balance":
                print("9 and 10 balance, so 11 is the odd light ball.")
            elif result3 == "right":
                print("9 is lighter, so 9 is the odd light ball.")
            else:
                print("10 is lighter, so 10 is the odd light ball.")
    
    elif result1 == "right":
        # Case 2: [5, 6, 7, 8] side is heavier, or [1, 2, 3, 4] side is lighter.
        print("5, 6, 7, 8 side is heavier, or 1, 2, 3, 4 side is lighter.")
        print("\nStep 2: Weighing [1, 2, 5] vs [3, 6, 12]")
        result2 = weigh([odd_weight if x == odd_ball else normal_weight for x in [1, 2, 5]], 
                        [odd_weight if x == odd_ball else normal_weight for x in [3, 6, 12]])
        
        if result2 == "balance":
            print("The scales balance, so the odd ball is either 4 (light) or 7 or 8 (heavy).")
            print("\nStep 3: Weighing 7 vs 8.")
            result3 = weigh([odd_weight if 7 == odd_ball else normal_weight],
                            [odd_weight if 8 == odd_ball else normal_weight])
            if result3 == "balance":
                print("7 and 8 balance, so 4 is the odd light ball.")
            elif result3 == "left":
                print("7 is heavier, so 7 is the odd heavy ball.")
            else:
                print("8 is heavier, so 8 is the odd heavy ball.")
        elif result2 == "right":
            print("3, 6, 12 side is heavier, so 6 is heavy or 1 or 2 is light.")
            print("\nStep 3: Weighing 1 vs 2.")
            result3 = weigh([odd_weight if 1 == odd_ball else normal_weight],
                            [odd_weight if 2 == odd_ball else normal_weight])
            if result3 == "balance":
                print("1 and 2 balance, so 6 is the odd heavy ball.")
            elif result3 == "right":
                print("1 is lighter, so 1 is the odd light ball.")
            else:
                print("2 is lighter, so 2 is the odd light ball.")
        else:
            print("3, 6, 12 side is lighter, so 3 is light or 5 is heavy.")
            print("\nStep 3: Weighing 3 against any other ball.")
            result3 = weigh([odd_weight if 3 == odd_ball else normal_weight], [normal_weight])
            if result3 == "balance":
                print("3 balances, so 5 is the odd heavy ball.")
            else:
                print("3 is lighter, so 3 is the odd light ball.")

    else:
        # Case 3: [1, 2, 3, 4] side is heavier, or [5, 6, 7, 8] side is lighter.
        print("1, 2, 3, 4 side is heavier, or 5, 6, 7, 8 side is lighter.")
        print("\nStep 2: Weighing [5, 6, 1] vs [7, 2, 12]")
        result2 = weigh([odd_weight if x == odd_ball else normal_weight for x in [5, 6, 1]], 
                        [odd_weight if x == odd_ball else normal_weight for x in [7, 2, 12]])
        
        if result2 == "balance":
            print("The scales balance, so the odd ball is either 8 (light) or 3 or 4 (heavy).")
            print("\nStep 3: Weighing 3 vs 4.")
            result3 = weigh([odd_weight if 3 == odd_ball else normal_weight],
                            [odd_weight if 4 == odd_ball else normal_weight])
            if result3 == "balance":
                print("3 and 4 balance, so 8 is the odd light ball.")
            elif result3 == "left":
                print("3 is heavier, so 3 is the odd heavy ball.")
            else:
                print("4 is heavier, so 4 is the odd heavy ball.")
        elif result2 == "left":
            print("7, 2, 12 side is lighter, so 7 is light or 1 is heavy.")
            print("\nStep 3: Weighing 7 against any other ball.")
            result3 = weigh([odd_weight if 7 == odd_ball else normal_weight], [normal_weight])
            if result3 == "balance":
                print("7 balances, so 1 is the odd heavy ball.")
            else:
                print("7 is lighter, so 7 is the odd light ball.")
        else:
            print("7, 2, 12 side is heavier, so 2 is heavy or 5 or 6 is light.")
            print("\nStep 3: Weighing 5 vs 6.")
            result3 = weigh([odd_weight if 5 == odd_ball else normal_weight],
                            [odd_weight if 6 == odd_ball else normal_weight])
            if result3 == "balance":
                print("5 and 6 balance, so 2 is the odd heavy ball.")
            elif result3 == "right":
                print("5 is lighter, so 5 is the odd light ball.")
            else:
                print("6 is lighter, so 6 is the odd light ball.")


def get_odd_ball():
    odd_ball_input = input("Enter the number of the odd ball (1-12) or type 'random' or 'exit' to quit: ").lower()
    if odd_ball_input == "exit":
        return None
    elif odd_ball_input == "random":
        return random.randint(1, 12)
    else:
        try:
            return int(odd_ball_input)
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 12, 'random', or 'exit'.")
            return get_odd_ball()

def get_odd_type():
    odd_type_input = input("Is the odd ball heavy, light, or type 'random' or 'exit' to quit: ").lower()
    if odd_type_input == "exit":
        return None
    elif odd_type_input == "random":
        return random.choice(['heavy', 'light'])
    elif odd_type_input in ['heavy', 'light']:
        return odd_type_input
    else:
        print("Invalid input. Please enter 'heavy', 'light', 'random', or 'exit'.")
        return get_odd_type()

# Main program
if __name__ == "__main__":
    while True:
        odd_ball = get_odd_ball()
        if odd_ball is None:
            print("Exiting the program. Goodbye!")
            break

        odd_type = get_odd_type()
        if odd_type is None:
            print("Exiting the program. Goodbye!")
            break

        print()
        ball_puzzle(odd_ball, odd_type)
        print()
