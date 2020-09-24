
import pymysql.cursors
import constant.database as DB

class Database:
    def __init__(self):
        self.conn = None
        self.cursor = None
        self.__connect()
    
    def __connect(self):
        self.conn = pymysql.connect(
            host= DB.HOST,
            port= DB.PORT,
            user= DB.USER,
            password = DB.PASSWORD,
            db= DB.NAME,
            cursorclass= pymysql.cursors.DictCursor
        )
        self.cursor = self.conn.cursor()
        return

    def query(self, sentence):
        try:
            self.cursor.execute(sentence)
            self.conn.commit()
        except Exception as e:
            try:
                self.__connect()
                self.cursor.execute(sentence)
                self.conn.commit()
            except Exception as e:
                print(DB.ERRORS["FAIL_CONNECTION"])

    def fetchOne(self, sentence):
        self.query(sentence)
        return self.cursor.fetchone()

    def fetchMany(self, sentence, size):
        self.query(sentence)
        return self.cursor.fetchmany(size)

    def fetchAll(self, sentence):
        self.query(sentence)
        return self.cursor.fetchall()

    def procedure(self, name, args):
        qry = "call {}(".format(name)+",".join(["'{}'".format(arg) for arg in args])+")"
        result = None
        try:
            result = self.fetchAll(qry)
        except Exception as e:
            try:
                self.__connect()
                result = self.fetchAll(qry)
            except Exception as e:
                print(DB.ERRORS["FAIL_CONNECTION"])
        return result

    def release(self):
        self.conn.close()
