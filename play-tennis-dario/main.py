def run(points: str) -> str:
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

            if tiebreak_a_points >= 7 and tiebreak_a_points - tiebreak_b_points >= 2:
                sets_a += 1
                result += '7-6 '
                tiebreak = False
                a_games = b_games = 0
                tiebreak_a_points = 0
                tiebreak_b_points = 0
            elif tiebreak_b_points >= 7 and tiebreak_b_points - tiebreak_a_points >= 2:
                sets_b += 1
                result += '6-7 '
                tiebreak = False
                a_games = b_games = 0
                tiebreak_a_points = 0
                tiebreak_b_points = 0
        else:
            if point == 'A':
                a_points += 1
            elif point == 'B':
                b_points += 1

            if a_points >= 4 and a_points - b_points >= 2:
                a_games += 1
                a_points = 0
                b_points = 0
            elif b_points >= 4 and b_points - a_points >= 2:
                b_games += 1
                a_points = 0
                b_points = 0

            if a_games >= 6 and a_games - b_games >= 2:
                sets_a += 1
                result += f'{a_games}-{b_games} '
                a_games = b_games = 0
            elif b_games >= 6 and b_games - a_games >= 2:
                sets_b += 1
                result += f'{a_games}-{b_games} '
                a_games = b_games = 0

            if a_games == 6 and b_games == 6:
                tiebreak = True
                tiebreak_a_points = 0
                tiebreak_b_points = 0
                continue
            
            if sets_a == 2 or sets_b == 2:
                break
    return result

# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
