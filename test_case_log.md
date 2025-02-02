# Test Cases for Firewall Project

## Scenario 
- **Firewall System IP is `192.168.140.129`**
- **Target System IP is `192.168.140.128`**

## Test Case 1: Block Specific IP (All Traffic)
- **Description:** Block all traffic from a specific IP.
- **Steps:**
  1. Use `firewall_automation.py` to block IP `192.168.140.128`.
  2. Attempt to ping `192.168.140.129` from `192.168.140.128`.
  3. Verify that the IP is blocked using `iptables -L -v -n`.

## Test Case 2: Block ICMP Traffic
- **Description:** Block ICMP (ping) traffic from a specific IP.
- **Steps:**
  1. Use `firewall_automation.py` to block ICMP traffic from IP `192.168.140.128`.
  2. Ping the Firewall system from `192.168.140.128`.
  3. Verify the ping requests fail.

## Test Case 3: Allow Specific Port
- **Description:** Allow traffic on port 8080.
- **Steps:**
  1. Use `firewall_automation.py` to allow port 8080.
  2. Test connectivity to the system on port 8080.
  3. Verify the traffic is allowed.

## Test Case 4: Log and Block Traffic
- **Description:** Log and block traffic from a specific IP.
- **Steps:**
  1. Use `firewall_automation.py` to log and block IP `44.228.249.3`.
  2. Attempt to access services from `44.228.249.3`.
  3. Check `/var/log/syslog` or `kern.log` for "Blocked Traffic".
  4. Verify traffic is blocked.
