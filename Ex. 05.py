sa=int(input('Qual o valor da mercadoria?'))
pa=int(input('Qual a porcentagem do desconto?'))
total=pa*sa/100
total2=sa-total
print(f'O valor do desconto será {total}')
print(f'O valor total após o desconto será {total2}')
