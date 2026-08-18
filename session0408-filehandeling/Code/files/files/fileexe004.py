from collections import defaultdict

file_path = r"F:\Mithun-PythonCode\Python\Materials\session0408-filehandeling\Code\files\files\logfile.txt"

def analyze_log(file_path):
    error_counts = defaultdict(int)

    try:
        with open(file_path, 'r') as f:
            for line in f:
                if "ERROR" in line:
                    parts = line.strip().split("ERROR:")
                    if len(parts) > 1:
                        error_type = parts[1].strip()
                        error_counts[error_type] += 1
    except FileNotFoundError:
        print("Log file not found.")
        return

    print("Error Summary:")
    for error, count in error_counts.items():
        print(f"{error}: {count} times")

# Call the function to run the analysis
analyze_log(file_path)

