def run(points: str) -> str:
    a_points = 0
    b_points = 0
    a_games_win = 0
    b_games_wins = 0
    sets_a = 0
    sets_b = 0
    result = ''

    # recorriendo todos los puntos
    for punto in points:
        if punto == 'A':
            a_points += 1
        elif punto == 'B':
            b_points += 1

        # el juego se gana con 4 puntos o diferencia de dos puntos
        if a_points >= 4 and a_points - b_points >= 2:
            a_games_win += 1
            a_points = 0
            b_points = 0
        elif b_points >= 4 and b_points - a_points >= 2:
            b_games_wins += 1
            a_points = 0
            b_points = 0

        if a_games_win == 5 and b_games_wins == 5:
            continue  # seguimos

        if a_games_win >= 6 and b_games_wins >= 6:
            if a_games_win == 7:
                sets_a += 1
                if result:
                    result += ' '
                result += f'{a_games_win}-{b_games_wins}'
                a_games_win = 0
                b_games_wins = 0

            elif b_games_wins == 7:
                sets_b += 1
                if result:
                    result += ' '
                result += f'{a_games_win}-{b_games_wins}'
                a_games_win = 0
                b_games_wins = 0

        # si un jugador a ganado mas de 6 juegos y tiene de diferencia 2 con el otro jugador gana set
        elif a_games_win >= 6 and a_games_win - b_games_wins >= 2:
            sets_a += 1
            if result:
                result += ' '
            result += f'{a_games_win}-{b_games_wins}'
            a_games_win = 0
            b_games_wins = 0

        elif b_games_wins >= 6 and b_games_wins - a_games_win >= 2:
            sets_b += 1
            if result:
                result += ' '
            result += f'{a_games_win}-{b_games_wins}'
            a_games_win = 0
            b_games_wins = 0
        if sets_a == 2 or sets_b == 2:
            break
    return result

# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
