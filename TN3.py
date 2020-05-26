
import telnetlib
import time

def telnet_gns3(ip):
    wait = 2 

    connection = telnetlib.Telnet(ip, 23, 5)
        
    output = connection.read_until("Password:", 5)
    connection.write('cisco' + "\n")
    connection.write('enable' + "\n")

    output = connection.read_until("Password:", 5)
    connection.write('cisco' + "\n")
    time.sleep(wait)
        
    
    connection.write("terminal length 0" + "\n")
    time.sleep(wait)
        
    
    
    connection.write("configure terminal" + "\n")
    time.sleep(wait)
    connection.write("int s0/0" + "\n")
    time.sleep(wait)   
    connection.write("no ip address 6.5.5.5 255.0.0.0" + "\n")
    time.sleep(wait)
    connection.write("end" + "\n")

    time.sleep(wait)
    connection.write("show ip int brief" + "\n")
    time.sleep(wait)

    output = connection.read_very_eager()
    print output
        
    
    connection.close()
        

#Call gns3
telnet_gns3('192.168.1.101')