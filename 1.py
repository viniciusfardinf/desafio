def pertence_fibonacci(numero):
    fib_1, fib_2 = 0, 1
    if numero == 0:
        return True
    while fib_2 <= numero:
        if fib_2 == numero:
            return True
        fib_1, fib_2 = fib_2, fib_1 + fib_2
    return False

numero = int(input("Informe um número: "))

if pertence_fibonacci(numero):
    print(f"O número {numero} pertence à sequência de Fibonacci.")
else:
    print(f"O número {numero} não pertence à sequência de Fibonacci.")
