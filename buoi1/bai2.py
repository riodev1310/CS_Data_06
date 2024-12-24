# input
# curent profit: float
# groưth rate: float
# năm: int 
current_profit = float(input("Current profit: "))
growth_rate = float(input("Growth rate: "))
years = int(input("Years: "))

# process
percentage_growth_rate = growth_rate / 100
future_profit = current_profit * (1+ percentage_growth_rate)**years 
comparison = ((future_profit - current_profit) / current_profit) * 100

print(f"Lợi nhuận tương lai: {round(future_profit, 2)}")
print(f"So sánh: {round(comparison, 2)}")

# ouput
# Lợi nhuận tương lai
# So sánh: tăng bao nhiêu % hoặc là giảm bao nhiêu %

# total = a + b
# example = total + c
# Inplace value