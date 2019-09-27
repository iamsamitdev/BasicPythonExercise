from tkinter import *

# สร้างหน้าต่าง
window = Tk()

# เพิ่มปุ่มกด
btn = Button(window, text="This is Button widget", fg='blue')
btn.place(x=80, y=100)

# เพิ่มคุณสมบัติให้หน้าต่างโปรแกรม
window.title('First GUI')
window.geometry("300x200+100+200")
window.mainloop()