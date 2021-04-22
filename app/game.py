import random

SWITCH_OPTION_KEEP = "keep"
SWITCH_OPTION_CHANGE = "change"


def run_round(choose_option, doors_count=3):
    """
    Run a single round of the Monty Hall game, with or without switching
    after the gameshow host keep a goat behind one of the unchosen doors.
    (choose_option is change or False). The car is behind door number 1 and the
    gameshow host knows that.

    """
    # Get a random door
    chosen_door = random.randint(1, doors_count)
    if choose_option == SWITCH_OPTION_CHANGE:
        # Reveal a goat
        revealed_door = 3 if chosen_door == 2 else 2
        # Forming a door list excluding chosen door and revealed door
        available_doors = [door for door in range(1, doors_count + 1)
                           if door not in (chosen_door, revealed_door)]
        chosen_door = random.choice(available_doors)
    # You win if you picked door number 1
    return chosen_door == 1


def run_multiple_rounds(attempts, choose_option, doors_count=3):
    wins_count = loose_count = 0
    for i in range(attempts):
        if run_round(choose_option, doors_count):
            wins_count += 1
        else:
            loose_count += 1
    return {
        "wins": wins_count,
        "loose": loose_count
    }
