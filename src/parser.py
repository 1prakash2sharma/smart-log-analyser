def read_log_file(file_path):
    with open(file_path, "r") as file:
        lines = file.readlines()
    return lines

def extract_login_times(log_lines):
    login_times = []

    for line in log_lines:
        if "login" in line.lower():
            parts = line.split()
            time = parts[1]  # assuming format: date time ...
            ip = parts[5]    # adjust if needed

            login_times.append((ip, time))

    return login_times

def extract_ip_user_mapping(log_lines):
    ip_users = {}

    for line in log_lines:
        if "login" in line.lower():
            parts = line.split()

            ip = parts[5]          # IP address
            user_part = parts[6]   # user=xyz
            user = user_part.split("=")[1]

            if ip not in ip_users:
                ip_users[ip] = set()

            ip_users[ip].add(user)

    return ip_users