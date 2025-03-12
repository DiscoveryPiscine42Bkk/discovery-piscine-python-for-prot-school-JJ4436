array = [2, 8, 9, 48, 8, 22, -12, 2]
new_array = set()  # ใช้ set เพื่อลบค่าซ้ำ

i = 0
while i < 8:
    if array[i] > 5:
        new_array.add(array[i] + 2)  # เพิ่มค่าที่ไม่ซ้ำเข้า set
    i += 1
print(array)
print(new_array)
