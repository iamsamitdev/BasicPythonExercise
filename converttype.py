try:
    # convert string to int
    s = input('Enter integer number: ') #string
    num = int(s) # convert to int

    print(num + 10)

    # convert string to float
    s2 = input('Enter floating number: ')
    f = float(s2)

    print("Hello python convert")
    print(f + 5.50)
except ValueError:
    print('ป้อนข้อมูลไม่ถูกต้อง ลองใหม่')

