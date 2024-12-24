# input
# L: float
# n: int
# r: float
L = float(input("Lợi nhuận sau thuế: "))
n = int(input("Số cổ phần: "))
r = float(input("Tỷ lệ: "))

#process
total = n * (r / 100) * (L / 100)

print(f"Tổng: {total}")

#output:
# Tổng số tiền cổ tức công ty phải chia cho các cổ đông.