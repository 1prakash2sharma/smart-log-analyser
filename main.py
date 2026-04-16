from src.parser import read_log_file, extract_login_times
from src.detector import detect_failed_logins, print_suspicious_activity, detect_suspicious_times
from src.parser import extract_ip_user_mapping
from src.detector import detect_multiple_users
import json

# Step 1: Read log file
log_lines = read_log_file("data/sample.log")

# Step 2: Existing logic
failed_attempts = detect_failed_logins(log_lines)
print_suspicious_activity(failed_attempts)

# Step 3: New feature (time detection)
login_times = extract_login_times(log_lines)
suspicious_times = detect_suspicious_times(login_times)

print("\nSuspicious Login Times")
print("------------------------------")

for ip, time in suspicious_times:
    print(f"{ip} logged in at suspicious time: {time}")

ip_users = extract_ip_user_mapping(log_lines)
multi_user_ips = detect_multiple_users(ip_users)

print("\nMultiple Users per IP")
print("------------------------------")

if multi_user_ips:
    for ip, users in multi_user_ips.items():
        print(f"{ip} used multiple usernames: {', '.join(users)}")
else:
    print("No multiple-user activity detected.")

report = {
    "failed_attempts": failed_attempts,
    "suspicious_times": [f"{ip} at {time}" for ip, time in suspicious_times],
    "multiple_users": {ip: list(users) for ip, users in multi_user_ips.items()}
}

with open("report.json", "w") as f:
    json.dump(report, f, indent=4)

print("\nReport saved as report.json")