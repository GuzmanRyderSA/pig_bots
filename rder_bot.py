def choice(round_score, my_score, opponent_score):
    if my_score < 10:
        return round_score <= 10
    elif my_score < 30 and my_score >= 10:
        return round_score <= 20
    elif my_score < 47 and my_score >= 30:
        return round_score <= 20
    elif my_score < 67 and my_score >= 50:
        return round_score <= 20
    elif my_score < 90 and my_score >= 60:
        return round_score <= 20
    elif my_score >= 90:
        return round_score
    else:
        return False
