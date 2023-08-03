# สร้างฟังก์ชันหาผลรวมของเบอร์โทร
def sum_phone_digit(phone_number):

    return sum(int(c) for c in phone_number)


# สร้างฟังก์ชันทำนายผลของเบอร์โทร
def interpret(number):

    # เขียนเงื่อนไขตรวจสอบกับข้อมูลหมายเลขใน list
    if number in (9, 14, 15, 19, 23, 24, 32, 36, 40, 41, 42, 44, 45, 46, 50, 51, 54, 55, 56, 59, 63, 64, 65):
        return "ดีมาก"
    elif number in (69, 79):
        return "โอกาสประสบผลสำเร็จสูง อุปสรรคน้อย เจริญรุ่งเรือง ร่ำรวย รวดเร็ว และมีความสุข"
    elif number in (10, 13, 16, 18, 20, 22, 25, 26, 28, 31, 35, 38, 39, 47, 49, 52, 53, 57, 58, 60, 61):
        return "ดีปานกลาง"
    elif number in (62, 66, 68, 74, 75):
        return "เหนื่อย มีอุปสรรค แต่ยังมีโอกาสประสบผลสำเร็จ หากมีความพยายาม"
    elif number in (11, 12, 17, 21, 27, 29, 30, 33, 34, 37, 43, 48, 67, 70, 71, 72, 73, 76, 77, 78, 80):
        return "เหนื่อยมาก อุปสรรคมาก เจอปัญหารุมเร้า การงาน การเงิน ความรัก เกิดอุบัติเหตุชีวิตไม่จบไม่สิ้น"
    else:
        return "ไม่พบข้อมูล"


# เรียกใช้ฟังก์ขันหาผลรวมและทำนายผลเบอร์
# รับค่าเบอร์โทรศัพท์จากผู้ใช้
phone = input("enter your phone number: ")  # string
print(interpret(sum_phone_digit(phone)))
