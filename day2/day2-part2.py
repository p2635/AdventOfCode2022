"""Module to solve day 2 of Advent of Code (part 2)."""
# - Removed opponent score, we don't need to track that
# - Implement a new method called get_desired_outcome
# - Implement a new method called get_correct_move

# Variables
PLAYER_SCORE = 0

def get_player_stats():
    print(f"The player score is {PLAYER_SCORE}.")

def get_desired_outcome(letter):
    """Function that determines the desired outcome."""
    try:
        if letter in ("X"):
            return "Lose"
        elif letter in ("Y"):
            return "Draw"
        elif letter in ("Z"):
            return "Win"
    except:
        print("Something went wrong.")

def get_correct_move(opp_move, desired_outcome):
    """Function that determines the correct move, given opponent's move and player's desired outcome."""

    # Copy opponent if desired outcome is draw
    if desired_outcome == "Draw":
        return opp_move

    # Do something else if desired outcome is something else
    if opp_move == "Rock":
        if desired_outcome == "Win":
            return "Paper"
        if desired_outcome == "Lose":
            return "Scissors"
    elif opp_move == "Paper":
        if desired_outcome == "Win":
            return "Scissors"
        if desired_outcome == "Lose":
            return "Rock"
    elif opp_move == "Scissors":
        if desired_outcome == "Win":
            return "Rock"
        if desired_outcome == "Lose":
            return "Paper"
    else:
        print("Something went wrong.")

def get_gesture(letter):
    """Function that determines the gesture"""
    try:
        if letter in ("A"):
            return "Rock"
        elif letter in ("B"):
            return "Paper"
        elif letter in ("C"):
            return "Scissors"
    except:
        print("Something went wrong.")

def get_gesture_score(gesture):
    """Function that determines what score you get based on the gesture"""
    try:
        if gesture == "Rock":
            return 1
        elif gesture == "Paper":
            return 2
        elif gesture == "Scissors":
            return 3
    except:
        print("Something went wrong.")

# Outcome of the round for the player - I know this is ugly code but I'm a n00b.
def get_outcome_player(opp, player):
    """Function that determines match outcome for the player (Win/Lose/Draw)"""
    if opp == player:
        return "Draw"
    elif (opp == "Paper" and player == "Scissors") or \
        (opp == "Scissors" and player == "Rock") or \
        (opp == "Rock" and player == "Paper"):
        return "Win"
    else:
        # Rock:Scissors, Paper:Rock, Scissors:Paper
        return "Lose"

# Outcome of the round (0 if you lost, 3 if the round was a draw, and 6 if you won).
def get_outcome_score(outcome):
    """Function that determines score based on match outcome."""
    if outcome == "Win":
        return 6
    elif outcome == "Lose":
        return 0
    elif outcome == "Draw":
        return 3

def part2():

    global PLAYER_SCORE

    with open("input/d2.txt", encoding="utf-8", mode="r") as rounds:

        i = 1

        # Elves line up, let's compete for the snack storage!
        for round in rounds:

            # Match details
            current_match = round.split()
            print(f"Match {i}", current_match)

            # Translate the gestures
            current_opp_gesture = get_gesture(current_match[0])
            current_desired_outcome = get_desired_outcome(current_match[1])
            current_best_move = get_correct_move(current_opp_gesture, current_desired_outcome)

            print(f"* The opponent elf: {current_opp_gesture}.")
            print(f"* The desired outcome is {current_desired_outcome}")
            print(f"* You play {current_best_move}")

            # Add gesture score
            PLAYER_SCORE += get_gesture_score(current_best_move)

            # Check total after getting gesture score
            get_player_stats()

            # Determine the outcome
            outcome = get_outcome_player(current_opp_gesture, current_best_move)
            print(f"The outcome of the match is {outcome}.")

            # Add outcome score
            PLAYER_SCORE += get_outcome_score(outcome)

            get_player_stats()

            # Next match
            i += 1

part2()