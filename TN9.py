# Create Command File
import telnetlib
import time

def telnet_gns3(ip):
    wait = 1   
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
    cmds = open(cmd_file, 'r')
    cmds.seek(0)
    for each_line in cmds.readlines():
        time.sleep(wait)
        connection.write(each_line)
        connection.write("\n")
    # -----------Command loop--------------------------


    # -------Write output to a file-------------------
    time.sleep(wait)
    output = connection.read_very_eager()
    R2 = open("R2", "w")
    R2.write(output)
    R2.close
    # -------Write output to a file-------------------
    print output
        
    
    connection.close()
        
def create_cmds():
    
    a=('terminal length 0','configure terminal')
    b=('no shut', 'int s0/0', 'ip address 5.5.5.5 255.0.0.0')
    c=('end','show ip int brief')
    cmds = a + b + c
    # -------Write output to a file-------------------
    file = open("file.txt", "w")
    for index in range(len(cmds)):
        file.write(cmds[index])
        file.write("\n")
    file.close
    # -------Write output to a file-------------------

#Start 
create_cmds()
telnet_gns3('192.168.1.101')











