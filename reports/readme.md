# devicehealth
A simple reporter based on django, sqlite, celery, reabbitmq to report device health

# Requirements:
Python 3.6.2


# Installation Instructions (Mac)
- install python 3 if not installed - ```brew install python3```
- install virtualenv if not installed yet - ```sudo pip install virtualenv```
- create virtual environment using python3 - ```virtualenv -p python3 <venvname>```
- activate ```source <venvname>/bin/activate```
- ```git clone git@github.com:ahsan-codejit/devicehealth.git```
- ```cd devicehealth```
- ```pip install -r devicehealth/requirement.txt```
- ```python manage.py makemigrations reports```
- ```python manage.py migrate```

## Import csv reports
### settings to run importcsv periodically (Mac)
- Install rabbitmq server and run (if needed)
  - run ```brew install rabbitmq ```
  - add 'export PATH=$PATH:/usr/local/sbin' to your .bash_profile
  - to run server ```rabbitmq-server```
  - to stop ```rabbitmqctl stop```, to look status ```rabbitmqctl status```
- Install Celery - 'pip install celery'
- Run beat/scheduler (celery -A ports beat --loglevel=info) in a window
- Run worker (celery -A reports worker -l info) in another window

Notes: We can setup demeonization for celery to run in background later

------------------ OR --------------------

### importing reports into sqlite manually
- run importcsv script
  - ```python manage.py shell```
  - ```from reports.tasks import *```
  - importcsv()
  - ctrl+D to exit

#Run Project
- ```python manage.py runserver```
- browse http://127.0.0.1:8000

# Short notes on tasks
## Part1 (import reports)
- importcsv in reports/tasks to import reports into database
  - it lists all .csv files and iterate the list to import into database
  - it create records from file into database if row/report is not already inserted into db
- to run this script periodic manner, we setup scheduler and worker using celery and rabbitmq
- this script also can be run by manually in above mentioned way
- We also can run this script aschync way from uploader method when file is uploaded if we add feature to upload reports file in this project

## Part2 (views) (bootstrp sb-admin2 theme is used)
### View1
- Percentage View
  - If occurrences of selected date and same day of last week of the selected date are same, it will show progress as 0.0%
  - If occurence of same day of last week of the selected date is 0 or null, it will also show 0.0%
  - Formula to make percentage, here, is ((current-previous)/previous)*100

### View2

## Periodic runner settings
- configuration to make scheduler in reports/settings.py
- it is scheduled to send request to run imporcsv each 5 min. we can do it once in a day, or once in hour etc.. based on needs

**************************************** Enjoy the reports :) **************************************
