import mysql.connector as connector

class DBrelation:
    def __init__(self):
        self.con = connector.connect(host = "localhost", user = "root", passwd = "1234", database="python_test",
        auth_plugin="mysql_native_password")
        query = 'create table if not exists User (userId int primary key, userName varchar(200),phone varchar(12), email varchar(20))'
        cur = self.con.cursor()
        cur.execute(query)
        print("Table Created")

    def insert_user(self, userid, username, phone, email):
        query = "insert into User(userID, userName, phone, email) values({},'{}',{},'{}')".format(userid, username, phone, email)
        #print(query)
        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("User data saved to database")

    def Fetch_all(self):
        query = "select * from user"
        cur = self.con.cursor()
        cur.execute(query)
        for row in cur:
            print("\n")
            print("UserId: ", row[0])
            print("UserName: ", row[1])
            print("Phone: ", row[2])
            print("email: ", row[3])
            print("\n")

    def update_user(self, userId, newname, newphone, newmail):
        query = "update  User set userName='{}', phone='{}', email='{}' where userId={}".format(newname, newphone, newmail, userId)
        print(query)
        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("Record Updated")



    def delete_user(self, userId):
        query = "Delete from User where userId = {}".format(userId)
        print(query)
        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit() #to delete record permanently in database
        print("User Deleted!")

