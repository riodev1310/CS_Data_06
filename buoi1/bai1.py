# input 
# Doanh thu: float
# Giá vốn hàng bán: float
revenue = float(input("Doanh thu: "))
cogs = float(input("Giá vốn hàng bán: "))

# Process
profit = revenue - cogs
profit_margin = (profit / revenue) * 100

print(f"Lợi nhuận gộp: {profit}")
print(f"Tỷ suất: {profit_margin}")
# output
# Lợi nhuận gộp
# Tỷ suất lợi nhuận gộp (%)