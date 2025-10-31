# Trabalho 1 – Recursividade  
## Exercício 1: Cálculo Fatorial Recursivo  

###  Aluno  
**Thalys e Leonardo Souza**

### Disciplina  
**Fundamentos Matemáticos**


---

## Introdução  

A recursividade é uma técnica de programação em que uma função chama a si mesma para resolver versões menores de um mesmo problema.  
Essa técnica é muito útil quando o problema pode ser definido de forma repetitiva.  

Um exemplo clássico é o cálculo do fatorial de um número inteiro não negativo, que é definido matematicamente como:

\[
n! = n \times (n - 1)!
\]
com a condição de que:
\[
0! = 1
\]

Ou seja, o fatorial de um número é o produto de todos os inteiros positivos menores ou iguais a ele.

---

## Código-Fonte  

O código abaixo implementa o cálculo fatorial de forma recursiva, utilizando uma função que se chama até atingir o caso base.

## Caso Base
O caso base é o ponto que interrompe a recursão e evita chamadas infinitas.
No fatorial, ele ocorre quando n é igual a 0 ou 1, pois ambos retornam 1, sem esse caso base, a função chamaria fatorial(n-1) para sempre, resultando em erro.
if n == 0 or n == 1:
    return 1

## Passo recursivo
O passo recursivo é a parte que faz a função se chamar novamente com um valor reduzido:

return n * fatorial(n - 1)

Aqui, o problema de calcular fatorial(n) é reduzido a um subproblema menor: fatorial(n-1).

## Rastreamaneto manual
Vamos acompanhar passo a passo o que acontece quando chamamos fatorial(4):

1. A função começa com fatorial(4)
→ Ela precisa saber o valor de fatorial(3) para continuar.

2. Agora entra fatorial(3)
→ Ela precisa saber o valor de fatorial(2).

3. Depois vem fatorial(2)
→ Ela chama fatorial(1).

4. Chegamos ao caso base com fatorial(1)
→ Como n == 1, a função retorna 1 e para de se chamar.

Agora as funções começam a retornar seus resultados, de baixo para cima:

fatorial(2) recebe o retorno de fatorial(1) e calcula 2 × 1 = 2

fatorial(3) recebe o retorno de fatorial(2) e calcula 3 × 2 = 6

fatorial(4) recebe o retorno de fatorial(3) e calcula 4 × 6 = 24

# Código

def fatorial(n):
    # Caso base: quando n é 0 ou 1, o fatorial é 1
    if n == 0 or n == 1:
        return 1
    else:
        # Passo recursivo: n multiplicado pelo fatorial de (n - 1)
        return n * fatorial(n - 1)

