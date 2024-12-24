# input
# Tổng số xu
c = int(input("Nhập số xu: "))

# 508 xu => 5 đô 8 xu
# 117 xu => 1 đô 17 xu
# 80 xu => 0 đô 80 xu

# 508 => 500 // 100 + 8
# 117 => 100 + 17
# Process:
d = c // 100
c1 = c % 100

print(f"{d}$ {c1} xu")

# Output
# Bao nhiêu đô và bao nhiêu xu