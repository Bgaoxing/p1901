import pymysql
import pymysql.cursors

def my(sql):
    connection = pymysql.connect(host = '127.0.0.1',
                                 user = 'root',
                                 password = '12345678',
                                 db = 'p1901',
                                 charset = 'utf8mb4',
                                 cursorclass = pymysql.cursors.DictCursor)


    with connection.cursor() as cursor:
        #sql = 'select * from `student`'
        cursor.execute(sql)
        result = cursor.fetchall()  #fetchall :抓取所有  fetchone:抓取一条
    return result

if __name__ == '__main__':
    sql = 'select * from `student`'
    res = my(sql)
    print(res)