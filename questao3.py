def pilha_moedas(v, n, S):
  dp = [float('inf')] * (S + 1)
  rastreio = [-1] * (S + 1)

  dp[0] = 0

  for i in range(1, S+1):
    dp[i] = float('inf')
    rastreio[i] = -1

  for i in range(1, S+1):
    for j in range(0, n):
      if v[j] <= i:
        if dp[i - v[j]] + 1 < dp[i]:
          dp[i] = dp[i - v[j]] + 1
          rastreio[i] = v[j]

  return (dp, rastreio)

def resultado_troco(moedas, S):
  n = len(moedas)
  dp, rastreio = pilha_moedas(moedas, n, S)

  if dp[S] == float('inf'):
    print('Saída: -1')
    print("Não é possível atingir o valor indicado.\n")
    return

  print(f'Saída: {dp[S]}')

  usadas = []
  atual = S
  while atual > 0:
    moeda = rastreio[atual]
    usadas.append(str(moeda))
    atual -= moeda

  if S==0:
    print('Explicação: Não precisamos de moedas\n')
  else:
    expressao = ' + '.join(usadas)
    print(f'Explicação: {S} = {expressao}\n')