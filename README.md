# fithub_backend
 Backend for health app
# Installation ->
Navigate to folder and activate a python virtual enviroment ( if you hadn't created one yet, make one)
https://docs.python.org/3/library/venv.html
run 
pip install -r "requirements.txt" 
to install python requirements (pip version may differ)

After this, run:
python manage.py makemigrations
python manage.py migrate

# Usage:
To create a super user, simply:
python manage.py createsuperuser
To run the server, simply:
python manage.py runserver
