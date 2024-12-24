# Đầu ngày
# loại 1 có b1 mặt hàng
# loại 2 có b2 mặt hàng

# Mặt hàng loại 1: c1 đồng / mặt hàng
# Mặt hàng loại 2: c2 đồng / mặt hàng

# Sau một ngày
# Loại 1 còn lại e1 mặt hàng
# Loại 2 còn lại e2 mặt hàng

#input 
# Số lượng mặt hàng b1 ban đầu
# Số lượng mặt hàng b2 ban đầu
# Giá của b1
# Giá của b2
# Số lượng còn lại e1
# Số lượng còn lại của e2
b1 = int(input("Số lượng mặt hàng loại 1 ban đầu: "))
b2 = int(input("Số lượng mặt hàng loại 2 ban đầu: "))
c1 = float(input("Giá b1: "))
c2 = float(input("Giá b2: "))
e1 = int(input("Số lượng còn lại b1: "))
e2 = int(input("Số lượng còn lại b2: "))

#process:
actual_revenue = (b1 - e1) * c1 + (b2 - e2) * c2 
maximum_revenue = b1 * c1 + b2 * c2

print(f"Actual revenue: {actual_revenue}")
print(f"Maximum Revenue: {maximum_revenue}")

# output
# Actual revenue
# Maximum revenue