#sample-data
login_logs = [
    {"ip": "192.168.1.15", "user": "admin", "status": "failed"},
    {"ip": "10.0.0.45", "user": "root", "status": "success"},
    {"ip": "192.168.1.15", "user": "root", "status": "failed"},
    {"ip": "192.168.1.15", "user": "admin", "status": "success"},
    {"ip": "172.16.0.5", "user": "ubuntu", "status": "success"},
    {"ip": "192.168.1.15", "user": "admin", "status": "failed"},
    {"ip": "10.0.0.45", "user": "admin", "status": "failed"},
    {"ip": "203.0.113.8", "user": "root", "status": "failed"},
    {"ip": "203.0.113.8", "user": "root", "status": "failed"},
    {"ip": "203.0.113.8", "user": "admin", "status": "failed"},
    {"ip": "10.0.0.45", "user": "root", "status": "success"}
]
def logAnalyzer(logs):
    ip_tracker = {}
    for log in logs:
        current_ip = log["ip"]
        if log["status"] == "failed":
            if current_ip in ip_tracker:
                ip_tracker[current_ip] += 1
            else:
                ip_tracker[current_ip] = 1
        else:
                ip_tracker[current_ip] = 0
    return ip_tracker
def security(tracker_data):
    for ip, count in tracker_data.items():
        if count >= 3:
            print(f"Adding {ip} to the firewall")

results = logAnalyzer(login_logs)
security(results)
