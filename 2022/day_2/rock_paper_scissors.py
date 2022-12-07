outcome_score = {"lost": 0, "win": 6, "draw": 3}
shape_score = {"rock": 1, "paper": 2, "scissors": 3}
loss_prediction = {"rock": "scissors", "paper": "rock", "scissors": "paper"}
win_prediction = {"rock": "paper", "paper": "scissors", "scissors": "rock"}
decode_outcome = {"X": "lost", "Y": "draw", "Z": "win"}
decode_shape = {
    "A": "rock",
    "B": "paper",
    "C": "scissors",
    "X": "rock",
    "Y": "paper",
    "Z": "scissors",
}


def solution(input):
    rounds = input.split("\n")[:-1]
    our_score = 0
    for round in rounds:
        opponentShape, ourShape = round.split(" ")
        opponentShape = decode_shape[opponentShape]
        ourShape = decode_shape[ourShape]

        if opponentShape == ourShape:
            our_score += shape_score[ourShape] + outcome_score["draw"]
            continue

        if (
            (opponentShape == "rock" and ourShape == "paper")
            or (opponentShape == "scissors" and ourShape == "rock")
            or (opponentShape == "paper" and ourShape == "scissors")
        ):
            our_score += shape_score[ourShape] + outcome_score["win"]
            continue

        if (
            (opponentShape == "rock" and ourShape == "scissors")
            or (opponentShape == "scissors" and ourShape == "paper")
            or (opponentShape == "paper" and ourShape == "rock")
        ):
            our_score += shape_score[ourShape] + outcome_score["lost"]
            continue

    return our_score


def solution_part2(input):
    rounds = input.split("\n")[:-1]
    our_score = 0
    for round in rounds:
        opponentShape, outcome = round.split(" ")
        opponentShape = decode_shape[opponentShape]
        outcome = decode_outcome[outcome]

        if outcome == "win":
            our_shape = win_prediction[opponentShape]
            our_score += shape_score[our_shape] + outcome_score["win"]
            continue

        if outcome == "lost":
            our_shape = loss_prediction[opponentShape]
            our_score += shape_score[our_shape] + outcome_score["lost"]
            continue

        if outcome == "draw":
            our_shape = opponentShape
            our_score += shape_score[our_shape] + outcome_score["draw"]
            continue

    return our_score
