import pyodbc
import dbpackage


def select_data():
    with dbpackage.connectdb() as con:
        sql_cmd = """
            SELECT *  FROM person
        """
        try:
           for row in con.execute(sql_cmd):
            # print(row)
            print(row[0], row[1], row[2], row[3])
        except pyodbc.ProgrammingError:
            print('select data fail!')


select_data()