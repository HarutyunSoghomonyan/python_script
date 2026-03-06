**The script operates in three simple steps:**
1) It scans each log entry. If a login "status" is failed, it adds 1 to that IP address's specific failure count.
2) If a login is success, it resets that IP's failure count back to 0. This ensures that a legitimate user who simply mistyped their password doesn't get banned.
3) After checking all logs, the script looks for any IP with a failure count of 3 or more. If found, it prints a message simulating a firewall block.
