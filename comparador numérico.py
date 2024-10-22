primeiro = input('Digite um valor: ')
segundo = input('Digite outro valor: ')

if primeiro > segundo:
    print(
        f'{primeiro = } é maior '
        f'que {segundo = }'
    )
elif primeiro == segundo:
    print(
        f'{primeiro = } é igual '
        f'ao que {segundo = }'
        
    )
else:
    print(
        f'{segundo = } é maior '
        f'do que {primeiro = }'
    )