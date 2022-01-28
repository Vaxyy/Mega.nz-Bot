# Copyright (c) 2021 Itz-fork

import os


if os.environ.get("LOGS_CHANNEL"):
    log_channel = int(os.environ.get("LOGS_CHANNEL"))
else:
    log_channel = None

class Config(object):
    APP_ID = int(os.environ.get("APP_ID", 7712824))
    API_HASH = os.environ.get("API_HASH", "2d3673e18b462f8032c4eea2f50b9f52")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5076719969:AAF-dO7u1Qqvhd5s3whqG39GgTLFx1Zy4A8")
    AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "1808315958").split())
    DOWNLOAD_LOCATION = "./NexaBots"
    IS_PUBLIC_BOT = os.environ.get("IS_PUBLIC_BOT", "False")
    LOGS_CHANNEL = log_channel
    TG_MAX_SIZE = 2040108421
    # Mega User Account
    MEGA_EMAIL = os.environ.get("MEGA_EMAIL", "hottygay143@gmail.com")
    MEGA_PASSWORD = os.environ.get("MEGA_PASSWORD", "Passwd@123")

# Text Prints
B_START_TEXT = """
   __  ___                                     ___       __ 
  /  |/  /__ ___ ____ _      ___  ___   ____  / _ )___  / /_
 / /|_/ / -_) _ `/ _ `/ _   / _ \/_ /  /___/ / _  / _ \/ __/
/_/  /_/\__/\_, /\_,_/ (_) /_//_//__/       /____/\___/\__/ 
           /___/

Process: {}
"""

PROCESS_TEXT = """
Process: {}
"""

LOGGED_AS_USER = """
Successfully Logged Into Mega.nz User Account
"""

LOGIN_ERROR_TEXT = """
Can't Get Mega Email and Password Login as an Anonymouse User
"""

ERROR_TEXT = """
 _____                     
| ____|_ __ _ __ ___  _ __ 
|  _| | '__| '__/ _ \| '__|
| |___| |  | | | (_) | |   
|_____|_|  |_|  \___/|_|  

Log: {}

Save the Log file and Send it to @Nexa_bots for Help :)
"""

START_TEXT="""
    _   __                   ____        __      
   / | / /__  _  ______ _   / __ )____  / /______
  /  |/ / _ \| |/_/ __ `/  / __  / __ \/ __/ ___/
 / /|  /  __/>  </ /_/ /  / /_/ / /_/ / /_(__  ) 
/_/ |_/\___/_/|_|\__,_/  /_____/\____/\__/____/ 


Bot is Running Now! Join @NexaBotsUpdates
"""
