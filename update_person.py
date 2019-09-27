import pyodbc
import dbpackage


def update_data():
    with dbpackage.connectdb() as con:
        sql_cmd = """
            UPDATE person SET fullname='Johny', weight='70' WHERE id='2'
        """
        try:
            con.execute(sql_cmd)
            print('update data success')
        except pyodbc.ProgrammingError:
            print('update data fail!')


update_data()
