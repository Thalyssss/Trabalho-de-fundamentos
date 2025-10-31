# 🧮 Trabalho 1 – Recursividade  
## Exercício 1: Cálculo Fatorial Recursivo  

### 👨‍💻 Aluno  
**Thalys e Leonardo Souza**

### 🏫 Disciplina  
**Fundamentos Matemáticos**


---

## 🧠 Introdução  

A **recursividade** é uma técnica de programação em que uma função chama a si mesma para resolver versões menores de um mesmo problema.  
Essa técnica é muito útil quando o problema pode ser definido de forma **repetitiva ou auto-referencial**.  

Um exemplo clássico é o **cálculo do fatorial de um número inteiro não negativo**, que é definido matematicamente como:

\[
n! = n \times (n - 1)!
\]
com a condição de que:
\[
0! = 1
\]

Ou seja, o fatorial de um número é o produto de todos os inteiros positivos menores ou iguais a ele.

---

## 💻 Código-Fonte  

O código abaixo implementa o cálculo fatorial de forma **recursiva**, utilizando uma função que se chama até atingir o **caso base**.

```python
def fatorial(n):
    # Caso base: quando n é 0 ou 1, o fatorial é 1
    if n == 0 or n == 1:
        return 1
    else:
        # Passo recursivo: n multiplicado pelo fatorial de (n - 1)
        return n * fatorial(n - 1)

# Exemplo de uso
if __name__ == "__main__":
    n = 4
    print(f"Fatorial de {n} = {fatorial(n)}")
