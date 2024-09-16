from plyer import notification
import time


if __name__ == "__main__":
    while True:
        notification.notify(title="Take Rest",
                            message="Hey zain take rest",
                            timeout=5)

        time.sleep(10)
# pythonw filename to execute multiple time
