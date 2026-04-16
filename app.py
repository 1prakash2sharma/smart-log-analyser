import streamlit as st
import pandas as pd

from src.parser import read_log_file, extract_login_times, extract_ip_user_mapping
from src.detector import detect_failed_logins, detect_suspicious_times, detect_multiple_users

st.set_page_config(page_title="Smart Log Analyser", layout="centered")

st.title("🔐 Smart Log Analyser Dashboard")
st.subheader("Cybersecurity Log Analysis Tool")

st.markdown("---")
st.markdown("### 🔍 Analyze system logs and detect suspicious activity in real-time")

uploaded_file = st.file_uploader("Upload a log file", type=["log", "txt"])

if uploaded_file:
    log_lines = uploaded_file.read().decode("utf-8").splitlines()
else:
    log_lines = read_log_file("data/sample.log")
    st.info("Using sample log file")

# Run detections
failed_attempts = detect_failed_logins(log_lines)
login_times = extract_login_times(log_lines)
suspicious_times = detect_suspicious_times(login_times)
ip_users = extract_ip_user_mapping(log_lines)
multi_user_ips = detect_multiple_users(ip_users)

st.header("📊 Summary")

col1, col2, col3 = st.columns(3)

col1.metric("Failed IPs", len(failed_attempts))
col2.metric("Suspicious Logins", len(suspicious_times))
col3.metric("Multi-user IPs", len(multi_user_ips))

# -------------------------------
# Failed Login Table
# -------------------------------
st.header("Failed Login Attempts")

if failed_attempts:
    df_failed = pd.DataFrame(list(failed_attempts.items()), columns=["IP Address", "Failed Attempts"])
    st.dataframe(df_failed)
else:
    st.success("No failed login attempts found.")

# -------------------------------
# Threat Alerts
# -------------------------------
st.header("🚨 Potential Threats")

threat_found = False
for ip, count in failed_attempts.items():
    if count >= 3:
        st.error(f"{ip} may be attempting brute-force login ({count} failures)")
        threat_found = True

if not threat_found:
    st.success("No suspicious activity detected.")

# -------------------------------
# Suspicious Login Times
# -------------------------------
st.header("⏰ Suspicious Login Times")

if suspicious_times:
    df_time = pd.DataFrame(suspicious_times, columns=["IP Address", "Time"])
    st.dataframe(df_time)
else:
    st.success("No suspicious login times detected.")

# -------------------------------
# Multiple Users per IP
# -------------------------------
st.header("👤 Multiple Users per IP")

if multi_user_ips:
    data = [(ip, ", ".join(users)) for ip, users in multi_user_ips.items()]
    df_users = pd.DataFrame(data, columns=["IP Address", "Usernames"])
    st.dataframe(df_users)
else:
    st.success("No multiple-user activity detected.")