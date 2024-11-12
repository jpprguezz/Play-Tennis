def run(points: str) -> str:
    a_points = 0
    b_points = 0
    a_games_win = 0
    b_games_win = 0
    sets_a = 0
    sets_b = 0
    result = ''
    tiebreak = False  # Variable para gestionar el tiebreak

    # Recorriendo todos los puntos
    for punto in points:
        if punto == 'A':
            a_points += 1
        elif punto == 'B':
            b_points += 1

        # El juego se gana con 4 puntos o diferencia de dos puntos
        if a_points >= 4 and a_points - b_points >= 2:
            a_games_win += 1
            a_points = 0
            b_points = 0
        elif b_points >= 4 and b_points - a_points >= 2:
            b_games_win += 1
            a_points = 0
            b_points = 0

        #se activa el tiebreak cuando el juego va 6-6
        if a_games_win == 6 and b_games_win == 6:
            tiebreak = True

        # Si estamos en un tiebreak
        if tiebreak:
            if a_points >= 7 and a_points - b_points >= 2:
                sets_a += 1
                result += f'7-6 '
                a_games_win = 0
                b_games_win = 0
                a_points = 0
                b_points = 0
                tiebreak = False
            elif b_points >= 7 and b_points - a_points >= 2:
                sets_b += 1
                result += f'6-7 '
                a_games_win = 0
                b_games_win = 0
                a_points = 0
                b_points = 0
                tiebreak = False  
        else:
            if a_games_win >= 6 and a_games_win - b_games_win >= 2:
                sets_a += 1
                result += f'{a_games_win}-{b_games_win} '
                a_games_win = 0
                b_games_win = 0
            elif b_games_win >= 6 and b_games_win - a_games_win >= 2:
                sets_b += 1
                result += f'{a_games_win}-{b_games_win} '
                a_games_win = 0
                b_games_win = 0

        if sets_a == 2 or sets_b == 2:
            break

    return result

# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
