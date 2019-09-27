# สร้างฟังก์ชัน hello
def hello(name):
    print('Hello %s ' % name)


# สร้างฟังก์ชันที่มีการ return ค่า
def area(width, height=2):
    c = width * height
    return c


# เรียกใช้ฟังก์ชัน hello
hello("Samit")

# เรียกใช้ฟังก์ชัน area
print(area(5, 8))
print(area(15, 3))

