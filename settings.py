import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import settings


class login:
    token = ""

class bot:
    prefixes = ['sudo ', '!']
    admins = [] # add bot admins here
    version = "0.0.0"

    class status:
        statuses = ["",""] # Set multiple statuses here, will change every $change_interval seconds
        change_interval = 0 # Should not be under 30, if set to 0 the statuses wont change

class sql:
    host =     r""
    database = r""
    user =     r""
    password = r""
    uri =      r""

class extensions:
    initial_extensions = ["cogs.admin",'cogs.master', "cogs.status"]

class files:
    base_dir = os.path.dirname(os.path.realpath(__file__))