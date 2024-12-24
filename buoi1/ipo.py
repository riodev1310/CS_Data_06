# input
# hours: float (Tổng số giờ làm việc của nhân viên)
# luong_theo_gio: int (Lương theo giờ)
hours = float(input("Tổng số giờ làm việc: "))
luong_theo_gio = float(input("Nhập số lương theo giờ: "))


# process 
# Bước 1: Tính tổng số lương của nhân viên
total = hours * luong_theo_gio
# Bước 2: In ra màn hình
print(f"Tổng số lương nhân viên nhận được là: {total}")

# output
# In ra tổng số lương lên màn hình terminal 