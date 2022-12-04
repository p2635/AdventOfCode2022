"""Module to solve day 2 of Advent of Code."""

# Variables
PLAYER_SCORE = 0
OPPONENT_SCORE = 0

def get_stats():
    get_opp_stats()
    get_player_stats()

def get_opp_stats():
    # Not used
    print(f"The opponent score is {OPPONENT_SCORE}.")

def get_player_stats():
    print(f"The player score is {PLAYER_SCORE}.")

def get_gesture(letter):
    """Function that determines the gesture"""
    try:
        if letter in ("A", "X"):
            return "Rock"
        elif letter in ("B", "Y"):
            return "Paper"
        elif letter in ("C", "Z"):
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

def part1():

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
            current_player_gesture = get_gesture(current_match[1])

            print(f"* The opponent elf: {current_opp_gesture}.")
            print(f"* The player elf (you): {current_player_gesture}.")

            # We don't actually care about the opponent's score for this puzzle
            # OPPONENT_SCORE += get_gesture_score(current_opp_gesture)

            # Add gesture score
            PLAYER_SCORE += get_gesture_score(current_player_gesture)

            # Check total after getting gesture score
            get_player_stats()

            # Determine the outcome
            outcome = get_outcome_player(current_opp_gesture, current_player_gesture)
            print(f"The outcome of the match is {outcome}.")

            # Add outcome score
            PLAYER_SCORE += get_outcome_score(outcome)

            get_player_stats()

            # Next match
            i += 1
