import pyodbc
import dbpackage


def insert_data(inp_data):
    with dbpackage.connectdb() as con:
        sql_cmd = """
            INSERT INTO person(fullname, weight, height) 
            VALUES({})
        """.format(inp_data)
        try:
            con.execute(sql_cmd)
            print('insert data success')
        except pyodbc.ProgrammingError:
            print('insert data fail!')


# รับข้อมูลจาก Input
inp_name = input("Input your name: ")
inp_weight = float(input("Input your weight: "))
inp_height = float(input("Input your height: "))

my_data = "'{}',{},{}".format(inp_name, inp_weight, inp_height)
insert_data(my_data)
