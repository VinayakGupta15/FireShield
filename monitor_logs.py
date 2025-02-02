import time

def monitor_logs(log_file):
    """Monitors the log file for new entries."""
    with open(log_file, "r") as file:
        file.seek(0, 2)  # Move to the end of the file
        while True:
            line = file.readline()
            if line:
                print(line.strip())
            time.sleep(0.1)

if __name__ == "__main__":
    # log_file = "/var/log/kern.log"  # Adjust path if needed
    log_file = "kern.log" # Use this in project directory
    print(f"Monitoring log file: {log_file}")
    try:
        monitor_logs(log_file)
    except KeyboardInterrupt:
        print("Stopped monitoring.")