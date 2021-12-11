import datetime
import time
from plyer import notification as nf

nf.notify(
            title = "It is {}".format(datetime.datetime.now()),
            message = "Your burger is ready",
            timeout=5,
            app_icon = "icon.ico"
            )
time.sleep(5)