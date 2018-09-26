import pymysql

class SQLOperate():
    def GetLoginname(self, name):
        conn = pymysql.connect(
            host= '10.246.190.99',
            port = 3306,
            user = 'outsourcing',
            password = '99Outsourcing!@#',
            database = "outsourcing",
            ) 
        cursor = conn.cursor()
        # 使用 execute()  方法执行 SQL 查询
        cursor.execute("SELECT loginname from `user` WHERE username = '"+name+"'")
 
        # 使用 fetchone() 方法获取单条数据.
        data = "".join(cursor.fetchone())
        # 关闭数据库连接
        conn.close()
        return data
        
if __name__ == "__main__":
    mission = SQLOperate()
    print(mission.GetLoginname( '闵银花' ))
