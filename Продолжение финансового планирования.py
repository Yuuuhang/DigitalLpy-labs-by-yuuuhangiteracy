import math

salary = 5000
spend = 6000
months = 10
increase = 0.03

money_capital = 0.0
current_spend = spend

for _ in range(months):
    shortage = max(0, current_spend - salary)
    money_capital += shortage
    current_spend *= (1 + increase)
    
integer_part = int(money_capital)

print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов: {integer_part}")
