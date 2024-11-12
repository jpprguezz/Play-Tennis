def run(points: str) -> str:
    a_points = 0
    b_points = 0
    a_games_win = 0
    b_games_wins = 0
    sets_a = 0
    sets_b = 0
    result = ''
    tiebreak = False  # Controla si estamos en un tiebreak
    tiebreak_a_points = 0  # Puntos en el tiebreak para A
    tiebreak_b_points = 0  # Puntos en el tiebreak para B

    # recorriendo todos los puntos
    for punto in points:
        if not tiebreak:  # Si no estamos en tiebreak
            if punto == 'A':
                a_points += 1
            elif punto == 'B':
                b_points += 1

            # Condiciones para ganar un juego
            if a_points >= 4 and a_points - b_points >= 2:
                a_games_win += 1
                a_points = 0
                b_points = 0
            elif b_points >= 4 and b_points - a_points >= 2:
                b_games_wins += 1
                a_points = 0
                b_points = 0

            # Condición para iniciar tiebreak si ambos llegan a 6 juegos
            if a_games_win == 6 and b_games_wins == 6:
                tiebreak = True  # Activamos el tiebreak
                tiebreak_a_points = 0
                tiebreak_b_points = 0

        else:  # Si estamos en tiebreak
            if punto == 'A':
                tiebreak_a_points += 1
            elif punto == 'B':
                tiebreak_b_points += 1

            # El tiebreak se gana con 7 puntos y una diferencia de al menos 2 puntos
            if tiebreak_a_points >= 7 and tiebreak_a_points - tiebreak_b_points >= 2:
                sets_a += 1
                result += f'7-6 '
                tiebreak = False
                a_games_win = 0
                b_games_wins = 0

            elif tiebreak_b_points >= 7 and tiebreak_b_points - tiebreak_a_points >= 2:
                sets_b += 1
                result += f'6-7 '
                tiebreak = False
                a_games_win = 0
                b_games_wins = 0

        # Condiciones para ganar un set fuera de tiebreak
        if not tiebreak:
            if a_games_win >= 6 and a_games_win - b_games_wins >= 2:
                sets_a += 1
                result += f'{a_games_win}-{b_games_wins} '
                a_games_win = 0
                b_games_wins = 0

            elif b_games_wins >= 6 and b_games_wins - a_games_win >= 2:
                sets_b += 1
                result += f'{a_games_win}-{b_games_wins} '
                a_games_win = 0
                b_games_wins = 0

        # Condición para terminar el partido si un jugador gana 2 sets
        if sets_a == 2 or sets_b == 2:
            break

    return result

# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)


