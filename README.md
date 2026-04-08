# Smart Log Analyser

A beginner-friendly Python cybersecurity project that analyzes log files and detects suspicious failed login attempts.

## Features
- Reads log files
- Detects failed login attempts
- Counts suspicious IP activity
- Flags possible brute-force attacks

## Project Structure
```bash
smart-log-analyser/
│
├── data/
│   └── sample.log
│
├── src/
│   ├── parser.py
│   └── detector.py
│
├── main.py
├── README.md
├── requirements.txt
└── .gitignore
```

## How to Run

```bash
python main.py
```

## Example Output

```txt
Suspicious Activity Report
------------------------------
192.168.1.10 -> 3 failed attempts
192.168.1.20 -> 4 failed attempts

Potential Threats
------------------------------
⚠ ALERT: 192.168.1.10 may be attempting brute-force login (3 failures)
⚠ ALERT: 192.168.1.20 may be attempting brute-force login (4 failures)
```

## Future Improvements
- Add timestamp analysis
- Add attack severity scoring
- Add dashboard with Streamlit
- Export reports to JSON