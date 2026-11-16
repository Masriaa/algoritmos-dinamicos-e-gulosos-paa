def alocador_trem(n, m, trens):
  trens_ordenados = sorted(trens, key=lambda x: x[1])

  plataformas_livres_hora = ['00:00'] * n
  trens_alocados = 0

  print('N° do trem - Horário de chegada - Horário de partida - N° da plataforma')

  for trem in trens_ordenados:
    num, chegada, partida = trem
    plataforma_recomendada = -1
    melhor_horario = '23:59'

    for plataforma in range(n):
      if plataformas_livres_hora[plataforma] <= chegada:
        if plataformas_livres_hora[plataforma] < melhor_horario:
          melhor_horario = plataformas_livres_hora[plataforma]
          plataforma_recomendada = plataforma

    if plataforma_recomendada != -1:
      plataformas_livres_hora[plataforma_recomendada] = partida
      trens_alocados += 1
      print(f'{num} - {chegada} - {partida} - {plataforma_recomendada + 1}')
    else:
      continue

  return trens_alocados