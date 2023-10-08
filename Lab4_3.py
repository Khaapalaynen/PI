from datetime import datetime
import time

for i in range(1,6):
    start_time = datetime.now()
    print(f"Время №{i} - {start_time}")
    time.sleep(1)