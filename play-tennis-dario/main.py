def run(points: str) -> str:
    A_GAME_WIN = 1
    B_GAME_WIN = 1
    GAME_WIN_POINTS = 4
    GAME_WIN_MARGIN = 2
    GAMES_WIN_SET = 6
    MARGIN_WIN_SET = 2
    COMPARING_SETS_WINNER = 2
    A_SET_WIN = 1
    B_SET_WIN = 1
    IN_GAME_POINT = 1
    IN_TIEBREAK_POINT = 1
    TIEBREAK_WIN_POINTS = 7
    TIEBREAK_WIN_MARGIN = 2
    A_TIEBREAK_SET_WIN = 1
    B_TIEBREAK_SET_WIN = 1
    COMPARING_TIEBREAK = 6
    RESET_POINTS = 0
    RESET_GAMES = 0
    RESET_TIEBREAK_WIN_POINTS = 0

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
                tiebreak_a_points += IN_TIEBREAK_POINT
            elif point == 'B':
                tiebreak_b_points += IN_TIEBREAK_POINT

            if tiebreak_a_points >= TIEBREAK_WIN_POINTS and tiebreak_a_points - tiebreak_b_points >= TIEBREAK_WIN_MARGIN:
                sets_a += A_TIEBREAK_SET_WIN
                result += '7-6 '
            elif tiebreak_b_points >= TIEBREAK_WIN_POINTS and tiebreak_b_points - tiebreak_a_points >= TIEBREAK_WIN_MARGIN:
                sets_b += B_TIEBREAK_SET_WIN
                result += '6-7 '
            if tiebreak_a_points >= TIEBREAK_WIN_POINTS and tiebreak_a_points - tiebreak_b_points >= TIEBREAK_WIN_MARGIN or tiebreak_b_points >= TIEBREAK_WIN_POINTS and tiebreak_b_points - tiebreak_a_points >= TIEBREAK_WIN_MARGIN:
                tiebreak = False
                a_games = 0
                b_games = 0
                tiebreak_a_points = 0
                tiebreak_b_points = 0
        else:
            if point == 'A':
                a_points += IN_GAME_POINT
            elif point == 'B':
                b_points += IN_GAME_POINT

            if a_points >= GAME_WIN_POINTS and a_points - b_points >= GAME_WIN_MARGIN:
                a_games += A_GAME_WIN
                a_points = RESET_POINTS
                b_points = RESET_POINTS
            elif b_points >= GAME_WIN_POINTS and b_points - a_points >= GAME_WIN_MARGIN:
                b_games += B_GAME_WIN
                a_points = RESET_POINTS
                b_points = RESET_POINTS

            if a_games >= GAMES_WIN_SET and a_games - b_games >= MARGIN_WIN_SET:
                sets_a += A_SET_WIN
                result += f'{a_games}-{b_games} '
                a_games = RESET_GAMES
                b_games = RESET_GAMES
            elif b_games >= GAMES_WIN_SET and b_games - a_games >= MARGIN_WIN_SET:
                sets_b += B_SET_WIN
                result += f'{a_games}-{b_games} '
                a_games = RESET_GAMES
                b_games = RESET_GAMES

            if a_games == COMPARING_TIEBREAK and b_games == COMPARING_TIEBREAK:
                tiebreak = True
                tiebreak_a_points = RESET_TIEBREAK_WIN_POINTS
                tiebreak_b_points = RESET_TIEBREAK_WIN_POINTS
                continue
            
            if sets_a == COMPARING_SETS_WINNER or sets_b == COMPARING_SETS_WINNER:
                break
    return result

# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
