import pyodbc
import dbpackage


def delete_data():
    with dbpackage.connectdb() as con:
        sql_cmd = """
            DELETE FROM person WHERE id='3'
        """
        try:
            con.execute(sql_cmd)
            print('delete data success')
        except pyodbc.ProgrammingError:
            print('delete data fail!')


delete_data()
