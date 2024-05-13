print ('------------------------------------------')
salario_bruto = float (input('Informe o salário bruto do funcionário: '))
print ('------------------------------------------')

inss = '14%' if salario_bruto >= 3856.9 else '12%' if salario_bruto > 2571.30 and salario_bruto <3856.9 else '9%' if salario_bruto >= 1320.01 and salario_bruto <= 2571.29 else '7,5%'
if inss == '14%':
  salario_descontado_inss = salario_bruto * 0.86
elif inss == '12%':
  salario_descontado_inss = salario_bruto * 0.88
elif inss == '9%':
  salario_descontado_inss = salario_bruto * 0.91
elif inss == '7,5%':
  salario_descontado_inss = salario_bruto * 0.935

irpf = '7,5%' if salario_bruto > 2112.0 and salario_bruto <= 2826.65 else '15,0%' if salario_bruto >= 2826.66 and salario_bruto <= 3751.05 else '22,5%' if salario_bruto >= 3751.06 and salario_bruto <= 4664.68 else '27,5%' if salario_bruto >= 4664.68 else 'Isento'
if irpf == '27,5%':
  salario_descontado_irpf = salario_bruto * 0.725
elif irpf == '22,5%':
  salario_descontado_irpf = salario_bruto * 0.775
elif irpf == '15%':
  salario_descontado_irpf = salario_bruto * 0.85
elif irpf == '7,5%':
  salario_descontado_irpf = salario_bruto * 0.935
elif irpf == 'Isento':
  salario_descontado_irpf = salario_bruto

taxa_inss = salario_bruto - salario_descontado_inss
taxa_irpf = salario_bruto - salario_descontado_irpf
salario_liquido = salario_bruto - taxa_inss - taxa_irpf

print ('De acordo com o ano de 2024, o funcionário pagará:')
print (f'-> 14% de INSS, que equivale a -R${taxa_inss} reais')
print (f'-> 22,5% de IRPF, que equivale a -R${taxa_irpf} reais')
print ('-----------------------------------------------')
print (f'Salário líquido será de: R$ {salario_liquido}')
