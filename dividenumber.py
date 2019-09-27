while True:
    try:
        a = input("Enter number 1: ")
        b = input("Enter number 2: ")
        result = int(a) / int(b)
        print(result)
        break
    except ValueError:
        print('กรุณาป้อนข้อมูลเป็นตัวเลขเท่านั้น')
    except ZeroDivisionError:
        print('ไม่สามารถหารด้วย 0 ได้')
