times_futebol = ('GREMIO',
            'REAL MADRID',
            'BARCELONA',
            'CHELSEA',
            'ATLETICO DE MADRID',
            'MILAN',
            'LIVERPOOL',
            'JUVENTUS',
            'NAPOLI',
            'REAL BETIS')
for times in times_futebol:
    print(f'{times} tem', end=' ')
    for letra in times:
        if letra in 'AEIOU':
            print(letra.lower(), end=' ')
    print()
