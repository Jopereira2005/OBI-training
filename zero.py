quantidade = int(input())
lista = []

for i in range(quantidade):
    num = int(input())
    if(num == 0):
        lista.pop()

    lista.append(num)

print(sum(lista))