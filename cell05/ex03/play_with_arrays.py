array = [2, 8, 9, 48, 8, 22, -12, 2]
new_array = set()  # ใช้ set เพื่อลบค่าซ้ำ

for plus in array:
    if plus > 5:
        new_array.add(plus + 2)  # เพิ่มค่าที่ไม่ซ้ำเข้า set
print(array)
print(new_array)
