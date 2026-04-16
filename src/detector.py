def detect_failed_logins(log_lines):
    failed_attempts = {}

    for line in log_lines:
        if "Failed login" in line:
            parts = line.split("from ")
            if len(parts) > 1:
                ip_part = parts[1].split(" ")[0]
                ip = ip_part.strip()

                if ip in failed_attempts:
                    failed_attempts[ip] += 1
                else:
                    failed_attempts[ip] = 1

    return failed_attempts


def print_suspicious_activity(failed_attempts, threshold=3):
    print("Suspicious Activity Report")
    print("-" * 30)

    if not failed_attempts:
        print("No failed login attempts found.")
        return

    for ip, count in failed_attempts.items():
        print(f"{ip} -> {count} failed attempts")

    print("\nPotential Threats")
    print("-" * 30)

    found = False
    for ip, count in failed_attempts.items():
        if count >= threshold:
            print(f"⚠ ALERT: {ip} may be attempting brute-force login ({count} failures)")
            found = True

    if not found:
        print("No suspicious activity detected.")

def detect_suspicious_times(login_times):
    suspicious = []

    for ip, time in login_times:
        hour = int(time.split(":")[0])

        if hour >= 0 and hour <= 5:
            suspicious.append((ip, time))

    return suspicious

def detect_multiple_users(ip_users):
    suspicious = {}

    for ip, users in ip_users.items():
        if len(users) > 1:
            suspicious[ip] = users

    return suspicious