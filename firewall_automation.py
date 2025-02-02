import os
import subprocess

def execute_command(command):
    """Executes a shell command."""
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    if result.returncode == 0:
        print(f"Command executed successfully: {command}")
    else:
        print(f"Error executing command: {command}\n{result.stderr}")

def block_ip(ip):
    """Blocks an IP address (all traffic)."""
    command = f"iptables -A INPUT -s {ip} -j DROP"
    execute_command(command)

def block_icmp(ip):
    """Blocks ICMP (ping) traffic from an IP address."""
    command = f"iptables -A INPUT -s {ip} -p icmp -j DROP"
    execute_command(command)

def allow_port(port):
    """Allows traffic on a specific port."""
    command = f"iptables -A INPUT -p tcp --dport {port} -j ACCEPT"
    execute_command(command)

def log_and_block(ip):
    """Logs and blocks traffic from an IP."""
    log_command = f"iptables -I INPUT -s {ip} -j LOG --log-prefix 'Blocked Traffic: '"
    block_command = f"iptables -A INPUT -s {ip} -j DROP"
    execute_command(log_command)
    execute_command(block_command)

def view_rules():
    """Views all iptables rules."""
    command = "iptables -L -v -n --line-numbers"
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    print(result.stdout)

if __name__ == "__main__":
    print("Firewall Automation Script")
    while True:
        print("\nOptions:")
        print("1. Block an IP (All Traffic)")
        print("2. Block ICMP (Ping) Traffic from an IP")
        print("3. Allow a Port")
        print("4. Log and Block an IP")
        print("5. View Current Rules")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            ip = input("Enter the IP to block: ")
            block_ip(ip)
        elif choice == "2":
            ip = input("Enter the IP to block ICMP (ping): ")
            block_icmp(ip)
        elif choice == "3":
            port = input("Enter the port to allow: ")
            allow_port(port)
        elif choice == "4":
            ip = input("Enter the IP to log and block: ")
            log_and_block(ip)
        elif choice == "5":
            view_rules()
        elif choice == "6":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")
