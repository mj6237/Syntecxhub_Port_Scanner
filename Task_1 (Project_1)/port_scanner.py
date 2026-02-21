# Import Required Libraries...
import socket     #For Creating Network Connection B/W Server and Client
import threading  #For Scanning Multiple Ports at Once
from datetime import datetime  #For Keeping the Record of Time And Date

# Taking Input Of Target IP or Hostname & Port Range
target = input("Enter target IP or Hostname (e.g, 192.168.34.5 / www.google.com) : ")
port_range = input("Enter port range (e.g, 10-80 OR Single Port 23) : ")

# Setting Log File Name In Which Our Output Will Be Stored....
log_file = "scanning_results.txt"  #Filename is upto you

# Creating Fuction To Check a port is open or closed...
def scan_port (ip, port):
    try:                      #IPv4 use           # TCP Protool
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((ip, port)) # It will return 0 if connection is established

        if result == 0:
            output = f"Port {port} is OPEN"
            print(output)
            with open(log_file, "a") as f:
                f.write(output + "\n")
        sock.close()
    except Exception as e:
        pass

# Creating Function to Manage range, threads and log_file...
def start_scanner ():
    print("-" * 50)
    print(f"Scanning Target: {target}")
    start_time = datetime.now()
    print(f"Time Started: {start_time}")
    print("-" * 50)

    #Clear log_file and  adding header to it
    with open(log_file, "w") as f:
        f.write(f"Scan Report for {target}\nStarted at :{datetime.now()}\n\n")

    #Checking port Range..
    if "-" in port_range:
        start_port, end_port = map(int, port_range.split("-"))
    else:
        start_port = end_port = int(port_range)

    #Creating threads
    threads = []
    for port in range(start_port, end_port +1):
        t = threading.Thread(target=scan_port, args=(target,port)) #Creating thead for eachPort
        threads.append(t)
        t.start()
    for t in threads: #It will wait for complete scanning of ports...
        t.join()
    end_time = datetime.now()
    duration = end_time - start_time

    print("-" * 50)
    print(f"Scan Complete. Results saved in {log_file}")
    print(f"Total Time Takenn :{duration}")
    print("-" *50)
if __name__ == "__main__":
    start_scanner()