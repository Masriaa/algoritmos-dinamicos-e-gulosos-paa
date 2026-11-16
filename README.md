# Projeto e Análise de Algoritmos (PAA) - Trabalho 2

Repositório dedicado à implementação e resolução das questões práticas da disciplina de Projeto e Análise de Algoritmos da Universidade Federal do Ceará (UFC) - Campus Crateús.

[Link para vídeo explicativo](https://drive.google.com/drive/folders/1-9QO92JpyEjJhYf1wB4tvXsyP9La_-mo?usp=sharing)

---

## 🛠️ Tecnologias Utilizadas
* **Linguagem:** Python 3
---

## Descrição das Questões Resolvidas (Matrícula Par)

### Questão 3: O Problema do Troco (Programação Dinâmica *Bottom-Up*)
* **Objetivo:** Encontrar o número mínimo de moedas necessárias para atingir um valor objetivo $S$ e reconstruir o conjunto de moedas utilizadas.
* **Abordagem:** Utilizou-se a técnica de **Programação Dinâmica de baixo para cima (*bottom-up*)**, construindo iterativamente uma tabela de menores custos (`dp`) e um vetor auxiliar (`rastreio`) para recuperar a solução ótima, evitando as falhas da abordagem gulosa clássica.

### Questão 4: Alocação de Trens em Plataformas (Algoritmo Guloso)
* **Objetivo:** Alocar o máximo possível de trens em $n$ plataformas disponíveis, considerando os horários de chegada e partida de cada trem.
* **Abordagem:** Utilizou-se uma estratégia **Gulosa (*Greedy*)**, ordenando os trens cronologicamente pelo horário de chegada e gerenciando dinamicamente o horário de liberação de cada plataforma para maximizar o aproveitamento da estação.

---

## 📚 Referências Bibliográficas

* **CORMEN, Thomas H. et al.** *Introduction to Algorithms*. 3ª ou 4ª ed. MIT Press. (Utilizado como referência teórica fundamental para a modelagem da Programação Dinâmica e algoritmos gulosos).
* Material didático e enunciados fornecidos pela coordenação da disciplina de Projeto e Análise de Algoritmos da Universidade Federal do Ceará (UFC - Crateús).
