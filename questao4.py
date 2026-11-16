def alocador_trem(n, m, trens):
    por_plataforma = {}
    for t in trens:
        por_plataforma.setdefault(t[3], []).append(t)

    total = 0
    print('N° do trem - Chegada - Partida - N° da plataforma')
    for p in sorted(por_plataforma):
        lista = sorted(por_plataforma[p], key=lambda x: x[2])
        livre = '00:00'
        for num, chegada, partida, _ in lista:
            if chegada >= livre:     
                livre = partida
                total += 1
                print(f'{num} - {chegada} - {partida} - {p}')
    return total
