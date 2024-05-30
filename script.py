import rpa
import pandas

number_email = 10

rpa.init(turbo_mode=True, chrome_browser=True)

rpa.url("https://10minutemail.net/")
rpa.wait()
print("[DEBUG] Website connected")
