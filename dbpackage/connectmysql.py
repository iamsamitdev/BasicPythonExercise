import pyodbc


def connectdb():
    con_string = 'driver=MySQL ODBC 5.3 Unicode Driver;' \
                          'server=localhost;' \
                          'database=mypythondbs;' \
                          'uid=root;' \
                          'pwd=1234'
    return pyodbc.connect(con_string)


# print(connectdb())
