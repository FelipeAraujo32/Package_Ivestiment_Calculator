import windows
# Criando a funcao para calcular

def calculate_profit(event):    
    
    try:
        initial_investment = float(windows.e_value_investiment.get())
        days_invested = int(windows.e_value_days.get())
        return_percentage = float(windows.e_value_percentage.get())
        
        daily_return = return_percentage / 100 / days_invested
        
        daily_profit = (initial_investment * daily_return)
        weekly_profit = (daily_profit * 7)
        monthly_profit = (daily_profit * 30)
        total_profit = initial_investment * (1 + return_percentage / 100)
        
        print(f'Lucro diario: {daily_profit:.2f}')
        print(f'Lucro semanal: {weekly_profit:.2f}')
        print(f'Lucro mensal: {monthly_profit:.2f}')
        print(f'Lucro total: {total_profit:.2f}')

    except ValueError as e:
        pass