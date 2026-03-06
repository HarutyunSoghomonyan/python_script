#the list of incoming IPs
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
""""
This is the first function. Firstly we define a dictionary called "ip_tracker". 
This is where the script writes down how many times each IP has failed to connect.
Then we start the loop. We define a variable for the IP key from the top list.
Then using an if statement we check the lines where the status is equal to "failed"
If an ip with failed status exists in the "ip_tracker" we defined earlier it adds +1 to its count.
If it doesn't exist it writes it down with value 1.
Then if create an "else" for successful attempts so that a user doesn't get wrongly banned if they fail 2 times then login, but then fail again.
Then we return the ip_tracker. This is like handing the list with the IPs to the next function.
"""
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
"""""
The next function looks for the data inside our ip_tracker list.
We define ip and count iterators. Using .items() it tracks the key and it's value.
The number next to the IP equals 3 or more it should print a firewall notice.
"""""
def security(tracker_data):
    for ip, count in tracker_data.items():
        if count >= 3:
            print(f"Adding {ip} to the firewall")

results = logAnalyzer(login_logs)
security(results)
