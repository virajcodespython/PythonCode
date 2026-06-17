import random

def get_two_numbers():
    """Ask the user for two numbers and return them as a tuple."""
    num1 = int(input("Please tell me a number: "))
    num2 = int(input("Please tell me another number: "))
    return num1, num2


def guess_one_operator(num1, num2, op_list):
    """Round type 1: guess the single missing operator between two numbers."""
    op = random.randint(0, len(op_list) - 1)

    if op_list[op] == '+':
        rhs = num1 + num2
    elif op_list[op] == '-':
        rhs = num1 - num2
    else:
        rhs = num1 * num2

    answer = input(f"\n{num1} __ {num2} = {rhs}\nWhat's the missing operator? > ").strip()

    if answer == op_list[op]:
        print("Well done!\n")
        return True
    else:
        print(f"Wrong! The answer was '{op_list[op]}'\n")
        return False


def guess_two_operators(num1, num2, op_list):
    """Round type 2: guess two missing operators across three numbers."""
    num3 = random.randint(1, 100)
    print(f"New number chosen: {num3}")

    chosen_ops = [random.choice(op_list[:2]) for _ in range(2)]  # only + or - for simplicity
    rhs = num1
    for i, op in enumerate([chosen_ops[0], chosen_ops[1]]):
        value = num2 if i == 0 else num3
        rhs = rhs + value if op == '+' else rhs - value

    answer = input(f"\n{num1} __ {num2} __ {num3} = {rhs}\nMissing operators (e.g. +-) > ").strip()

    correct = "".join(chosen_ops)
    if answer == correct:
        print("Well done!\n")
        return True
    else:
        print(f"Wrong! The answer was '{correct}'\n")
        return False


def print_banner():
    """Print the game's ASCII banner."""
    lines = [
        "-----  |   |    /\\    |\\  |  |  /    |   | [---] |    |",
        "  |    |   |   /  \\   | \\ |  | /     |   | |   | |    |",
        "  |    |---|  /--  \\  |  \\|  |/       ---| |   | |    |",
        "  |    |   | /      \\ |   |  |\\          | |   | |    |",
        "  |    |   |/        \\|   |  | \\      ___| |___| |____|",
    ]
    for line in lines:
        print(line)


def play_game():
    """Main game loop: keep playing rounds until the player quits."""
    op_list = ['+', '-', '*']
    score = 0
    rounds_played = 0

    print("=== Number Guessing Game ===\n")

    while True:
        num1, num2 = get_two_numbers()
        round_type = random.choice(["one_op", "two_op"])

        if round_type == "one_op":
            correct = guess_one_operator(num1, num2, op_list)
        else:
            correct = guess_two_operators(num1, num2, op_list)

        rounds_played += 1
        if correct:
            score += 1

        print(f"Score: {score}/{rounds_played}")

        again = input("\nPlay another round? (y/n) > ").strip().lower()
        if again != 'y':
            break

    print(f"\nFinal score: {score}/{rounds_played}")
    print_banner()


if __name__ == "__main__":
    play_game()
