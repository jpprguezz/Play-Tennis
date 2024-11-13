def run(points: str) -> str:
    GAME_WIN_POINTS = 4
    GAME_WIN_MARGIN = 2
    GAMES_WIN_SET = 6
    MARGIN_WIN_SET = 2
    SETS_TO_WIN_MATCH = 2
    TIEBREAK_WIN_POINTS = 7
    TIEBREAK_WIN_MARGIN = 2
    GAMES_FOR_TIEBREAK = 6

    a_points = 0
    b_points = 0
    a_games = 0
    b_games = 0
    sets_a = 0
    sets_b = 0
    result = ''
    tiebreak = False
    tiebreak_a_points = 0
    tiebreak_b_points = 0

    for point in points:
        if tiebreak:
            if point == 'A':
                tiebreak_a_points += 1
            elif point == 'B':
                tiebreak_b_points += 1

            if tiebreak_a_points >= TIEBREAK_WIN_POINTS and tiebreak_a_points - tiebreak_b_points >= TIEBREAK_WIN_MARGIN:
                sets_a += 1
                result += '7-6 '
            elif tiebreak_b_points >= TIEBREAK_WIN_POINTS and tiebreak_b_points - tiebreak_a_points >= TIEBREAK_WIN_MARGIN:
                sets_b += 1
                result += '6-7 '

            if ((tiebreak_a_points >= TIEBREAK_WIN_POINTS and tiebreak_a_points - tiebreak_b_points >= TIEBREAK_WIN_MARGIN) or 
            (tiebreak_b_points >= TIEBREAK_WIN_POINTS and tiebreak_b_points - tiebreak_a_points >= TIEBREAK_WIN_MARGIN)):
                tiebreak = False
                a_games = b_games = 0
                tiebreak_a_points = 0
                tiebreak_b_points = 0
        else:
            if point == 'A':
                a_points += 1
            elif point == 'B':
                b_points += 1

            if a_points >= GAME_WIN_POINTS and a_points - b_points >= GAME_WIN_MARGIN:
                a_games += 1
                a_points = 0
                b_points = 0
            elif b_points >= GAME_WIN_POINTS and b_points - a_points >= GAME_WIN_MARGIN:
                b_games += 1
                a_points = 0
                b_points = 0

            if a_games >= GAMES_WIN_SET and a_games - b_games >= MARGIN_WIN_SET:
                sets_a += 1
                result += f'{a_games}-{b_games} '
                a_games = 0
                b_games = 0
            elif b_games >= GAMES_WIN_SET and b_games - a_games >= MARGIN_WIN_SET:
                sets_b += 1
                result += f'{a_games}-{b_games} '
                a_games = 0
                b_games = 0

            if a_games == GAMES_FOR_TIEBREAK and b_games == GAMES_FOR_TIEBREAK:
                tiebreak = True
                tiebreak_a_points = 0
                tiebreak_b_points = 0

            if sets_a == SETS_TO_WIN_MATCH or sets_b == SETS_TO_WIN_MATCH:
                break

    return result


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
