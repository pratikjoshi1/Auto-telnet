
import telnetlib
import time

def telnet_gns3(ip,router):
    wait = 4  


    # -----------Sign in--------------------------
    connection = telnetlib.Telnet(ip, 23, 5)        
    connection.read_until("Password:", 5)
    connection.write('cisco' + "\n")
    connection.write('enable' + "\n")
    connection.read_until("Password:", 5)
    connection.write('cisco' + "\n")
    # -----------Sign in--------------------------


    # -----------Command loop--------------------------
    cmd_file = raw_input('Enter command file name and extension: ') 
    selected_cmd_file = open(cmd_file, 'r')
    selected_cmd_file.seek(0)
    for each_line in selected_cmd_file.readlines():
        time.sleep(wait)
        connection.write(each_line)
        connection.write("\n")
    # -----------Command loop--------------------------

    connection.write('show run' + "\n")
    time.sleep(30)

    # -------Write output to a file-------------------
    if router == 1: 
        time.sleep(wait)
        output = connection.read_very_eager()
        R1 = open("R1", "w")
        R1.write(output)
        R1.close
    elif router == 2: 
        time.sleep(wait)
        output = connection.read_very_eager()
        R2 = open("R2", "w")
        R2.write(output)
        R2.close
    elif router == 3: 
        time.sleep(wait)
        output = connection.read_very_eager()
        R3 = open("R3", "w")
        R3.write(output)
        R3.close        
    elif router == 4:
        time.sleep(wait)
        output = connection.read_very_eager()
        R4 = open("R4", "w")
        R4.write(output)
        R4.close      
    # -------Write output to a file-------------------
    connection.close()
        
# Program starts
#Call gns3
#loop n number times where n = the number of routers
for router in range(1,5):
    if router == 1: 
        ip = '192.168.1.101' 
    elif router == 2: 
        ip = '192.168.1.102'
    elif router == 3: 
        ip = '192.168.1.103'
    elif router == 4: 
        ip = '192.168.1.104'
    telnet_gns3(ip,router) 
    


















