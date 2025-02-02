# **Project: FireShield**
![alt test](/logo.webp)

### **Interactive and Adaptive Network Security with iptables**

---

## **Overview**
FireShield is a dynamic, interactive, and highly customizable network security solution that leverages the power of `iptables`. It offers a practical implementation to configure, monitor, and secure networks against common cyber threats such as unauthorized access, DoS attacks, and port scans.

---

## **Features**
- **Dynamic Firewall Management:**
  - Block or allow IPs and ports in real-time using `firewall_automation.py`.
  - Pre-configured secure default policies to protect against attacks.

- **Attack Simulation:**
  - Test firewall robustness with simulated DoS attacks and port scans.

- **Log Monitoring:**
  - Monitor dropped packets and suspicious activity in real-time.

- **Customizable Rules:**
  - Easily edit `iptables_rules.sh` for specific organizational needs.

---

## **File Structure**
```plaintext
FireShield/
├── iptables_rules.sh       # Core firewall rule setup script
├── firewall_automation.py  # Interactive Python script to manage iptables rules
├── monitor_logs.py         # Real-time log monitoring tool
├── simulate_dos.sh         # Simulates DoS attacks using hping3
├── simulate_port_scan.sh   # Simulates port scanning with nmap
├── test_case_log.md        # Documentation of test cases
├── requirements.txt        # Python dependencies for the project
```

---

## **Getting Started**

### Prerequisites
1. Python 3.8+
2. `iptables` (pre-installed on most Linux systems)
3. `hping3` and `nmap` for attack simulations:

   ```bash
   sudo apt-get install hping3 nmap
   ```

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/VinayakGupta15/FireShield.git
   cd FireShield
   ```

2. Set up a Python virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: .\venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Make scripts executable:
   ```bash
   chmod +x *
   ```

---

## **Usage**

### 1. Configure Firewall Rules
Run the `iptables_rules.sh` script to apply default firewall rules:
```bash
sudo ./iptables_rules.sh
```

### 2. Manage Firewall Rules
Use the `firewall_automation.py` script for interactive rule management:
```bash
python firewall_automation.py
```

- **Options:**
  1. Blocks an IP address (all traffic).
  2. Blocks ICMP (ping) traffic from an IP address.
  3. Allows traffic on a specific port.
  4. Logs and blocks traffic from an IP.
  5. Views all iptables rules.
  6. Exit

### 3. Monitor Logs
Monitor network activity in real-time:
```bash
sudo python monitor_logs.py
```

### 4. Simulate Attacks
- **Simulate DoS Attack:**
  ```bash
  ./simulate_dos.sh <target_ip>
  ```
- **Simulate Port Scan:**
  ```bash
  ./simulate_port_scan.sh <target_ip>
  ```

---

## **Testing**
Refer to `test_case_log.md` for comprehensive test scenarios and validation steps. Example:
- Block IP: Test if traffic from a specific IP is denied.
- Allow Port: Verify if allowed ports accept traffic.
- Log Analysis: Check `/kern.log` or `/fireshield/kern.log` for activity logs.

---

## **License**
This project is licensed under the MIT License. See the LICENSE file for details.

---

