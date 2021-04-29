import mysql.connector
import datetime
from termcolor import colored

class Connector:
    def __init__(self):
        self.mydb = mysql.connector.connect(host="localhost",user="PingNet",password="ASDFqwer1234",database="pingnet")
        print(self.mydb)
        self.cursor = self.mydb.cursor()
        self.cursor.execute("USE pingnet")
        self.cursor.execute("create table if not exists agents("
                                "agentID varchar(6) not null primary key,"
                                "IPaddr INT(255) UNSIGNED NOT NULL,"
                                "os varchar(255) null,"
                                "service varchar(255) null,"
                                "status varchar(10) not null default \'ALIVE\',"
                                "pingtimestamp timestamp null,"
                                "team SMALLINT(255) NOT NULL"
                                ")")

    def add_agent(self, agentID, IPaddr,os ,service, team):
        cmd = "INSERT INTO agents(agentID,IPaddr,os,service,team) values (%s, %s, INET_ATON(%s),%s,%s)"
        values = ("a4f5a6","127.0.0.1", "Windows", "DNS", "01")
        self.cursor.execute(cmd, values)
        self.mydb.comit()

    def delete_agent(self, id):
        self.cursor.execute(f"DELETE FROM agents WHERE agentID={id}")
        self.mydb.comit()

    def dbPull(self):  # PUBLIC
        self.checkStatus()

        self.cursor.execute("select * from agents order by isnull(service), service asc")
        return self.cursor.fetchall()

    def pullSpecific(self, grouping, value):  # INTERNAL, use this when sending group commands?
        self.checkStatus()

        self.cursor.execute(f"select agentID from agents where {grouping}=\'{value}\'")
        return self.cursor.fetchall()

    def heart_ips(self):
        self.cursor.execute("SELECT inet_ntoa(IPaddr) FROM pingnet.agents;")
        return self.cursor.fetchall()
    
    def heart_ips_test(self):
        self.cursor.execute("SELECT inet_ntoa(IPaddr) FROM pingnet.agents WHERE team = 15")
        return self.cursor.fetchall()

    def removeAllAgents(self):  # PUBLIC, removes all agents
        self.cursor.execute("delete from agents")

        self.mydb.commit()
        print(colored(" All agents removed!\n", "yellow"))


    def updateTimestamp(self, tstamp, agent):  # INTERNAL, updates on resync request
        sqlcmd = "insert into agents (pingtimestamp) values (%s) where agentID=\'%s\'"
        values = (tstamp, agent)

        self.cursor.execute(sqlcmd, values)
        self.mydb.commit()


    def describe(self):
        self.cursor.execute("desc agents")
        for value in self.cursor.fetchall():
            print(value)
        print("")


    # STATUS CHECKS
    def missingStatus(self, ip):  # INTERNAL, after 3 pings missed (timestamp+3min)
        self.cursor.execute("update agents "
                            "set status = \'MIA\'"
                            f"where agentID =\'{ip}\'")

        self.mydb.commit()
        # print(colored(f" Agent {ip} is MIA!\n", "yellow")) 


    def deadStatus(self, ip):  # PUBLIC, after agent killed
        sqlcmd = "update agents set status=%s where agentid=%s"
        val = ("SRV-KILLED", str(ip))
        self.cursor.execute(sqlcmd, val)

        self.mydb.commit()


        #print(colored(f" Agent {ip} is dead!\n", "red")) 


    def aliveStatus(self, ip, timestamp):  # INTERNAL, after receiving beacon
        self.cursor.execute(f"select agentID from agents where agentID = \'{ip}\'")
        resp = self.cursor.fetchall()
        if len(resp) == 0:
            self.addAgent(ip, timestamp, "ALIVE")
        else:
            self.cursor.execute("update agents "
                                f"set status = \'ALIVE\',pingtimestamp=\'{timestamp}\' "
                                f"where agentID = \'{ip}\'")

            self.mydb.commit()

        #print(colored(f" \nPing from agent {ip}!\n", "green")) 


    def checkStatus(self):  # internal, called on each summon of the table
        tscurrent = datetime.datetime.now()
        strcurrent = "{:%Y-%m-%d %H:%M:%S}".format(tscurrent)

        t2 = datetime.datetime.strptime(strcurrent, "%Y-%m-%d %H:%M:%S")

        self.cursor.execute("select pingtimestamp,agentID,status from agents")
        data = self.cursor.fetchall()
        if len(data) == 0:
            return  # skip if no agents in table

        for entry in data:
            check = "{:%Y-%m-%d %H:%M:%S}".format(entry[0])  # %Y-%m-%d %H:%M:%S
            t1 = datetime.datetime.strptime(check, "%Y-%m-%d %H:%M:%S")  

            difference = t2 - t1

            if difference.seconds / 60 > 3.0 and entry[2] != "SRV-KILLED":
                self.missingStatus(entry[1])


    def cleanDB(self):  # EXTERNAL, called on 'shutdown'
        self.removeAllAgents()
        self.cursor.execute("drop table agents")
        self.mydb.commit()
        print(colored("\n Dropping agents table...", "yellow"))
        self.cursor.execute("drop database mesaC2")
        self.mydb.commit()
        print(colored("\n Deleting database mesaC2...\n", "yellow"))