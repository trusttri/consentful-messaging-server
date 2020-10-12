# consentful-messaging-server
Server code for consentful messaging.

## Getting started
1) Have python 3 installed
`brew install python3`

2) Install virtualenv
`sudo pip3 install virtualenv`

3) Clone the repository
`git clone https://github.com/trusttri/consentful-messaging-server.git`

4) `cd consentful-messaging-server`

5) Create a virtual environment (inside the directory of consentful-messaging-server/). I called it consent-message-env.
`virtualenv consent-message-env -p python3`

6) Activate the environment. 
`source consent-message-env/bin/activate`

7) `cd consentful_messaging/`

8) Install the required python packages. `pip install -r requirements.txt`

9) `python manage.py runserver`

You should see "welcome to consentful messaging!" when you go to localhost:8000 (for now). 
