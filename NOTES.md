#### If you accidentally open the application in more than one Terminal, you can kill all instances of the running application by typing: 
pkill -9 python3

commands

pip3 freeze --local > requirements.txt
python3 app.py


CONNECTING MONGODB
in console paste:

mongodb+srv://simocasoni:Mongodb1996!@myfirstcluster.q3xzf.mongodb.net/myFirstDB?retryWrites=true&w=majority
mongo "mongodb+srv://myfirstcluster.q3xzf.mongodb.net/myFirstDatabase" --username simocasoni

Access a MongoDB database and collection


Treat the database and its collection like a dictionary key to access them:
db = client["some_db"]

Here’s how to use an instance of that database to get the collection:
col = db["some_col"]


You can also use objects attributes to get the database and its collection like this:

db = client.some_db
col = db.some_col



BEFORE heroku
adding requirements.txt file
adding procfile (deleting last line to prevent heroku errors)
adding keys to heroku before deployment
downloading flask pymongo

CONNECTING HEROKU
npm install -g heroku    to connect heroku in the Terminal
heroku login -i          to login to heroku
heroku apps              it shows actual apps
heroku apps:rename casoni-app --app casoni-app-changed      it let you rename your app name


DOWNLOADING BOOTSTRAP THEME

wget https://github.com/startbootstrap/startbootstrap-scrolling-nav/archive/gh-pages.zip

cd - (goes previous directory)
cd (e.g.) static (change directory to static)
unzip filename

SIGN UP FORM
running test to verify data transmission (GDC > network >signup "request")


BUGS

couldn't access the preview
a typo error was made: "{#Template" to be inserted here }

jquery actions weren't working
python function include, in the html base file, was deleted by mistake


UPDATES FOR TOMORROW 

CHECK DATABASE LOGIC MINUTE 16:52