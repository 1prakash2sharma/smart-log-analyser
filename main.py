from src.parser import read_log_file
from src.detector import detect_failed_logins, print_suspicious_activity


def main():
    file_path = "data/sample.log"

    log_lines = read_log_file(file_path)
    failed_attempts = detect_failed_logins(log_lines)
    print_suspicious_activity(failed_attempts)


if __name__ == "__main__":
    main()