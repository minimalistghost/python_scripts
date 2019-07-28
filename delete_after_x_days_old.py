# Class that contains various display colors and styles
class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

import subprocess, os, time

# Variables
deletedatabasepath = r"/media/mg/Backup1/Work/deprecated/Databases/mysql_backups/"
now = time.time()

# Cleans up files older than 90 days
print color.GREEN + '\nClean up old database dumps\n' + color.END
for filename in os.listdir(deletedatabasepath):
    # if os.stat(os.path.join(path, filename)).st_mtime < now - 7 * 86400:
    if os.path.getmtime(os.path.join(deletedatabasepath, filename)) < now - 90 * 86400:
        if os.path.isfile(os.path.join(deletedatabasepath, filename)):
            print(filename)
            os.remove(os.path.join(deletedatabasepath, filename))
