import random
import string
with open("SQLimport.sql", "w") as f:
    for teamnum in range(1,16):
        thing = []
        thang = []
        for i in range(1,14):
            thing.append(''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(6)))
        box1=f'INSERT INTO agents(agentID,IPaddr,os,service,team) values ("{thing[0]}", INET_ATON("10.{teamnum}.2.2"),"Ubuntu","Web","{teamnum}");\n'
        box2=f'INSERT INTO agents(agentID,IPaddr,os,service,team) values ("{thing[1]}", INET_ATON("10.{teamnum}.2.3"),"CentOS","Database","{teamnum}");\n'
        box3=f'INSERT INTO agents(agentID,IPaddr,os,service,team) values ("{thing[2]}", INET_ATON("10.{teamnum}.2.4"),"Windows Server 2016","FTP","{teamnum}");\n'
        box4=f'INSERT INTO agents(agentID,IPaddr,os,service,team) values ("{thing[3]}", INET_ATON("10.{teamnum}.2.10"),"Ubuntu","IoT","{teamnum}");\n'
        box5=f'INSERT INTO agents(agentID,IPaddr,os,service,team) values ("{thing[4]}", INET_ATON("10.{teamnum}.2.12"),"NA","CalDev","{teamnum}");\n'
        box6=f'INSERT INTO agents(agentID,IPaddr,os,service,team) values ("{thing[5]}", INET_ATON("10.{teamnum}.2.14"),"Ubuntu","HTTP/SSH","{teamnum}");\n'
        box7=f'INSERT INTO agents(agentID,IPaddr,os,service,team) values ("{thing[6]}", INET_ATON("10.{teamnum}.1.10"),"NA","ICMP/SSH","{teamnum}");\n'
        box8=f'INSERT INTO agents(agentID,IPaddr,os,service,team) values ("{thing[7]}", INET_ATON("10.{teamnum}.1.40"),"Ubuntu","SSH","{teamnum}");\n'
        box9=f'INSERT INTO agents(agentID,IPaddr,os,service,team) values ("{thing[8]}", INET_ATON("10.{teamnum}.1.60"),"Windows Server 2019","LDAP/DNS","{teamnum}");\n'
        box10=f'INSERT INTO agents(agentID,IPaddr,os,service,team) values ("{thing[9]}", INET_ATON("10.{teamnum}.1.70"),"Windows 10","WinRM","{teamnum}");\n'
        box11=f'INSERT INTO agents(agentID,IPaddr,os,service,team) values ("{thing[10]}", INET_ATON("10.{teamnum}.1.80"),"Windows 10","WinRM","{teamnum}");\n'
        box12=f'INSERT INTO agents(agentID,IPaddr,os,service,team) values ("{thing[11]}", INET_ATON("10.{teamnum}.1.90"),"Windows 10","WinRM","{teamnum}");\n'
        box13=f'INSERT INTO agents(agentID,IPaddr,os,service,team) values ("{thing[12]}", INET_ATON("10.{teamnum}.1.100"),"Windows 10","WinRM","{teamnum}");\n'
        thang.append(box1)
        thang.append(box2) 
        thang.append(box3) 
        thang.append(box4) 
        thang.append(box5) 
        thang.append(box6)
        thang.append(box7) 
        thang.append(box8) 
        thang.append(box9) 
        thang.append(box10)
        thang.append(box11)
        thang.append(box12)
        thang.append(box13)

        f.writelines(thang)

    #print(thang)     