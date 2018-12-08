
#activate_this = '/var/www/html/blog/venv/bin/activate_this.py'
#with open(activate_this) as file_:
#	exec(file_.read(), dict(__file__=activate_this))

import sys
sys.path.insert(0, '/var/www/html/cloud_print')
from cloud_print import app as application
