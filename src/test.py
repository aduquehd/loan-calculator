valor = int(input("Valor a retirar: "))

billetes = {
    '100': 100000,
    '50': 50000,
    '20': 20000,
    '10': 10000,
    '5': 5000,
    '2': 2000,
    '1': 1000,
}

contador_billetes = {key: 0 for key in billetes}

for key in billetes:
    while valor >= billetes[key]:
        valor -= billetes[key]
        contador_billetes[key] += 1

for key in contador_billetes:
    print(f"Billetes de {key}: {contador_billetes[key]}")
