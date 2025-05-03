# Simple Port Scanner

A simple, multi-threaded port scanner written in Python. This tool allows you to scan a given host (IP address or domain name) for open ports within a specified range. It uses Python's built-in socket library and threading for faster scanning.

## Features
- Scans a range of ports on a specified host.
- Checks if ports are open and reports the status.
- Multi-threaded for faster performance.

## Requirements
- Python 3.x (No external libraries required)

## Usage

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/simple-port-scanner.git
    cd simple-port-scanner
    ```

2. Run the script:

    ```bash
    python port_scanner.py
    ```

3. Enter the host (IP or domain), and specify the port range you want to scan.

    Example input:
    ```
    Enter host IP or domain: example.com
    Enter start port: 20
    Enter end port: 100
    ```

4. The script will display which ports are open within the specified range.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
