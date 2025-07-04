from datetime import datetime
import time

import schedule

from main import main


def run():
    print(f"Run started at {datetime.now().strftime('%d-%m-%Y %H:%M:%S')}")
    try:
        main()
        print("Run finished successfully.\n")
    except Exception as e:
        print(f"Error: {e}\n")


schedule.every(1).hours.do(run)

run()

print("Scheduler started. Running every hour.")

while True:
    schedule.run_pending()
    time.sleep(60)
