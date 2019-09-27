import pyodbc
import dbpackage

def create_table():
    with dbpackage.connectdb() as con:
        sql_cmd = """
            create table person(
                id int PRIMARY KEY AUTO_INCREMENT,
                fullname varchar(255),
                weight float,
                height float
            )
        """
        try:
            con.execute(sql_cmd)
            print('Create table success')
        except pyodbc.ProgrammingError:
            print('Already have table')


create_table()
