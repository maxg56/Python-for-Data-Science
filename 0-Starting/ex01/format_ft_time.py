import time
import datetime

# Get the current timestamp with subsecond precision
timestamp = time.time()

# Print seconds since epoch with both fixed and scientific notation
print("Seconds since January 1, 1970: {:.4f} or {:.2e} in scientific notation".format(timestamp, timestamp))

# Convert to human-readable date
readable_date = datetime.datetime.fromtimestamp(timestamp).strftime("%b %d %Y")
print(readable_date)
