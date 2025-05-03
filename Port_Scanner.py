import socket
import threading

# Function to check if a port is open on a given host
def scan_port(host, port):
    try:
        # Create a socket object
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        
        # Try to connect to the given host and port
        result = sock.connect_ex((host, port))
        
        # If the result is 0, the port is open
        if result == 0:
            print(f"Port {port} is open.")
        sock.close()
    except socket.error as err:
        print(f"Error scanning port {port}: {err}")

# Function to perform a port scan within a specified range
def scan_ports(host, start_port, end_port):
    print(f"Scanning ports {start_port}-{end_port} on {host}...\n")
    
    # Create a list to store threads
    threads = []
    
    # Start scanning the ports in the range
    for port in range(start_port, end_port + 1):
        thread = threading.Thread(target=scan_port, args=(host, port))
        thread.start()
        threads.append(thread)
    
    # Wait for all threads to finish
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    # Get host and port range from the user
    host = input("Enter host IP or domain: ")
    start_port = int(input("Enter start port: "))
    end_port = int(input("Enter end port: "))
    
    # Call the function to scan ports
    scan_ports(host, start_port, end_port)
