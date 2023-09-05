# Exercício solucionado: calculando as datas e parcelas de um empréstimo
# Maria pegou um empréstimo de 1.000.000
# para realizar o pagamento em 5 anos.
# A data em que ela pegou o empréstimo foi
# 20/12/2020 e o vencimento de cada parcela
# é no dia 20 de cada mês.
# - Crie a data do empréstimo
# - Crie a data do final do empréstimo
# - Mostre todas as datas de vencimento e o valor de cada parcela
from datetime import datetime
from dateutil.relativedelta import relativedelta

parcelas_mensais = 'R$ 16,666.67'
data_emprestimo = datetime(2020, 12, 20)
data_final = data_emprestimo + relativedelta(months=60)
# print(data_final)


count = 0
print(60)
for i in range(60):             #MINHA SOLUÇÃO
    count += 1

    data_emprestimo += relativedelta(months=1)
    data_emprestimo_formatada = data_emprestimo.strftime('%d/%m/%Y')
    print(f'{data_emprestimo_formatada}, {parcelas_mensais}')
print()
print(f'Você pegou R$1,000,000.00 para pagar em 5 anos ({count} meses) em parcelas de {parcelas_mensais}')

#########################################################################################################################################################################################


valor_total = 1_000_000
data_emprestimo = datetime(2020, 12, 20)
delta_anos = relativedelta(years=5)
data_final = data_emprestimo + delta_anos

data_parcelas = []
data_parcela = data_emprestimo
while data_parcela < data_final:
    data_parcelas.append(data_parcela)
    data_parcela += relativedelta(months=+1)

numero_parcelas = len(data_parcelas)
valor_parcela = valor_total / numero_parcelas

for data in data_parcelas:
    print(data.strftime('%d/%m/%Y'), f'R$ {valor_parcela:,.2f}')

print()
print(
    f'Você pegou R$ {valor_total:,.2f} para pagar '
    f'em {delta_anos.years} anos '
    f'({numero_parcelas} meses) em parcelas de '
    f'R$ {valor_parcela:,.2f}.'
)


