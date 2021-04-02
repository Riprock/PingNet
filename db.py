import mysql.connector
import datetime

from colorama import init
init()

class Connector:
    def __init__(self):
        username = "Ping"
        password = "Thing"
    try:
        self.mydb = mysql.connector.connect(
            host = "localhost",
            username = username,
            password = password
        )
        print(mysql)
        self.cursor = self.mysql.cursor()
        self.cursor.execute("DROP DATABASE IF EXISTS pingnet")
        self.cursor.execute("CREATE DATABASE pingnet")
        self.cursor.execute("USE pingnet")
        self.cursor.execute("create table if not exists agents("
                                "agentID varchar(16) not null primary key,"
                                "IPaddr INT(255) UNSIGNED NOT NULL"
                                "os varchar(255) null,"
                                "service varchar(255) null,"
                                "status varchar(10) not null default \'ALIVE\',"
                                "pingtimestamp timestamp null,"
                                "team SMALLINT(255) NOT NULL"
                                ")
    except:
        print("Cannot connect to database\nPlease check your user,pass, hostanme and verify the service is running")

    
    def add_agent(self, ip, id, status):
        cmd = "INSERT INTO agents(agentID, status, IPaddr) values (%s, %s, INET_ATON(%s))"
        values = (id, "New", "127.0.0.1")#Needs to be updated for the import statement and Need to do ID generation
        self.cursor.execute(cmd, values)
        self.mydb.comit()

    def delete_agent(self, id):
        self.cursor.execute(f"DELETE FROM agents WHERE agentID={id}")
        self.mydb.comit()

    def getDB(self):
        self.cursor

    def getAgent(self):
        pass

    def updateTimestamp(self):
        pass

    def statusUpdate(self):
        pass
    
    def DBstatus(self):
