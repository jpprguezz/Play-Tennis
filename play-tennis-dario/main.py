def run(points: str) -> str:
    puntajes_a = 0
    puntajes_b = 0
    juegos_a = 0
    juegos_b = 0
    sets_a = 0
    sets_b = 0
    tiebreak_a = 0
    tiebreak_b = 0
    result = ""

    # recorriendo todos los puntos
    for punto in points:
        if punto == 'A':
            puntajes_a += 1
        elif punto == 'B':
            puntajes_b += 1
        
        # el juego se gana con 4 puntos o
        if puntajes_a >= 4 and puntajes_a - puntajes_b >= 2:
            juegos_a += 1
            puntajes_a = 0
            puntajes_b = 0
        elif puntajes_b >= 4 and puntajes_b - puntajes_a >= 2:
            juegos_b += 1
            puntajes_a = 0
            puntajes_b = 0
        
        # si un jugador a ganado mas de 6 juegos y tiene de diferencia 2 con el otro jugador gana set
        if juegos_a >= 6 and juegos_a - juegos_b >= 2:
            sets_a += 1
            if result:
                result += ''
            result += f"{juegos_a}-{juegos_b} "
            juegos_a = 0
            juegos_b = 0
        elif juegos_b >= 6 and juegos_b - juegos_a >= 2:
            sets_b += 1
            if result:
                result += ''
            result += f"{juegos_a}-{juegos_b} "
            juegos_a = 0
            juegos_b = 0
        #fumada
        if juegos_a == 5 and juegos_b ==5:
            if juegos_a > juegos_b:
                tiebreak_a +=1
                juegos_a+=1
                if tiebreak_a == 2:
                    sets_a +=1
                    result += f"{juegos_a}-{juegos_b} "
                    break
                else:
                    sets_b +=1
                    result += f"{juegos_a}-{juegos_b} "
                    break
            else:
                tiebreak_b +=1
                juegos_b +=1
        
        # gana con 2 sets
        if sets_a == 2 or sets_b == 2:
            break
      
    return result


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
