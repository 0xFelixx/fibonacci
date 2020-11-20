num = int(input("hvor meget vil du tælle til? \n"))

fibo1 = 0
fibo = 1

for i in range(num):
    tempFibo = fibo1     + fibo
    print(f"{i + 1  } - {fibo}")
    fibo1 = fibo
    fibo = tempFibo
