import os
import logging
from datetime import datetime

# Explicitly set the project root directory
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
log_dir = 'logs'

# Print the project root directory
print(f"Project root directory: {project_root}")

logs_path = os.path.join(project_root, log_dir, LOG_FILE)

# Print the logs path
print(f"Logs path: {logs_path}")

# Ensure the log directory exists
try:
    os.makedirs(os.path.join(project_root, log_dir), exist_ok=True)
    print(f"Log directory created: {os.path.join(project_root, log_dir)}")
except Exception as e:
    print(f"Failed to create log directory: {e}")

# Configure logging
try:
    logging.basicConfig(
        filename=logs_path,
        format='[%(asctime)s] - %(name)s - %(levelname)s - %(message)s',
        level=logging.DEBUG,
    )
    print(f"Logging configured to write to: {logs_path}")
except Exception as e:
    print(f"Failed to configure logging: {e}")

# Example log message
try:
    logging.info("Logger initialized successfully.")
    print("Log message written successfully.")
except Exception as e:
    print(f"Failed to write log message: {e}")