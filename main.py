
#!/usr/bin/python3
 
import pymysql
 
# 打开数据库连接
conn = pymysql.connect(
    host= "localhost",
    user= "root",
    password= "root",
    database= "Test",
    charset= "utf8")
 
# 得到一个可以执行SQL语句的光标对象
cursor = conn.cursor()  # 执行完毕返回的结果集默认以元组显示
 
# 使用 execute()  方法执行 SQL 查询 
cursor.execute("SELECT VERSION()")
 
# 使用 fetchone() 方法获取单条数据.
data = cursor.fetchone()
 
print ("Database version : %s " % data)
 
# 关闭数据库连接
conn.close()

