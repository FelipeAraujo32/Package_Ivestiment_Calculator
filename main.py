# Criando a funcao para calcular

def calcular_lucro(investimento_inicial, dias_investimento, porcetagem_retorno):
    
    retorno_diario = porcetagem_retorno / 100 / dias_investimento
    
    lucro_diario = (investimento_inicial * retorno_diario)
    lucro_semenal = (lucro_diario * 7)
    lucro_mensal = (lucro_diario * 30)
    lucro_total = investimento_inicial * (1 + porcetagem_retorno / 100)
    
    print(f'Lucro diario: {lucro_diario:.2f}')
    print(f'Lucro semanal: {lucro_semenal:.2f}')
    print(f'Lucro mensal: {lucro_mensal:.2f}')
    print(f'Lucro total: {lucro_total:.2f}')
    
calcular_lucro(5000,30,5)