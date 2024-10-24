import schedule
import time
from utils.send_message import send_message

def schedule_message(phone_no, message, time_hour, time_minute):
    # Schedule a message at a specific time
    schedule.every().day.at(f"{time_hour}:{time_minute}").do(send_message, phone_no, message)

    # Keep running the scheduler
    while True:
        schedule.run_pending()
        time.sleep(1)
