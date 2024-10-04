questao_2.py
def pertence_fibonacci(numero):
    fib1, fib2 = 0, 1
    while fib1 <= numero:
        if fib1 == numero:
            return True
        fib1, fib2 = fib2, fib1 + fib2
    return False

# Definindo um número para verificar
numero = 21

if pertence_fibonacci(numero):
    print(f"O número {numero} pertence à sequência de Fibonacci.")
else:
    print(f"O número {numero} não pertence à sequência de Fibonacci.")
