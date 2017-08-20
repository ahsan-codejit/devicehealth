# devicehealth
A simple reporter based on django, sqlite, celery, reabbitmq to report device health

# Requirements:
Python 3.6.2

# Installation Instructions
- create virtual environment using python3 (virtualenv -p python3 <venvname>)
- source <venvname>/bin/activate
- git clone git@github.com:ahsan-codejit/devicehealth.git
- cd devicehealth
- pip install -r devicehealth/requirement.txt
- python manage.py migration
- python manage.py runserver
- browse http://127.0.0.1:8000

# settings to run importcsv periodically
- Install rabbitmq server and run
- Install Celery
- Run beat (celery -A ports beat --loglevel=info)
- Run worker (celery -A reports worker -l info)

------------------ OR --------------------

# manually importing reports into sqlite
- run importcsv script

# Enjoy the reports :)
