import pymysql as my
from pymysql.cursors import DictCursor


def get_list():
  con = my.connect(host='localhost', port=3306, user='root' , password='1234', database='shop', cursorclass=DictCursor)
  cursor = con.cursor()

  sql = "SELECT id, title, writer, date FROM bbs ORDER BY id DESC"
  cursor.execute(sql)

  rows = cursor.fetchall()
  
  print(rows)
  con.close()
  return rows

def post(data):
  con = my.connect(host='localhost', port=3306, user='root' , password='1234', database='shop', cursorclass=DictCursor)
  cursor = con.cursor()

  sql = "INSERT INTO bbs (title, content, writer, date) VALUES (%s, %s, %s, now())"
  cursor.execute(sql, data)  
  con.commit()
  con.close()
  return "success"