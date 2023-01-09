# $ pip install plyer
# $ pip install python-time

from plyer import notification
import time

if __name__ == '__main__':
    while True:
        notification.notify(
            title = "*** Take Rest ***",
            message = "Just send the messages with the true feelings and then you soul mate will be so happy to check",
            app_icon = None,
            timeout = 5)
        time.sleep(20)
    
# Pythonw Desktop_Notifier.py