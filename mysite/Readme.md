facebookapp is an example of social authentication with Django.
The social application here is facebook.
facebookapp displays your name and profile picture of the logged in user.

Installation and use:
–> clone the repository
–> setup a virtual environment for the project and activate it:
python -m venv venv
source venv/bin/activate
–> Navigate to the project’s root directory
–> install the requirements: pip install -r requirements.txt
–> provide your facebook app id and secret key in the settings.py
–> Run the migrations : python manage.py migrate
python manage.py makemigrations facebookapp
python manage.py migrate
–> Run the server: python manage.py runserver


