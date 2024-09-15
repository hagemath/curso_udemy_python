print("-------Sequência de Fibonacci-------")
#Rever
def sequencia_fibo(n):
    seq = [0, 1]
    soma = 0
    while len(seq) < n:
        seq.append(seq[-1] + seq[-2])
    for i in seq:
        print(f"{i}", end=" ")
        
sequencia_fibo(10)


