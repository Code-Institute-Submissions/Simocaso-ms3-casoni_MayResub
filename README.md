# ms3-casoni

![Casoni Task manager logo](readme-files/ctm-logo.png)

# Casoni Task manager

![CTM responsive displays](readme-files/CTM-responsive.png)

With this README file, I'll guide you through my MS3 project for the DUBLIN CODE INSTITUTE.
If looking at my commits' time, you are wondering if multiple people were working on this project, then the answer is no; I just didn't sleep at all.
However, this is not a complaint. I simply would like to show you my passion for studying coding (even in these terrible times, where it is very hard to find your motivation).

Casoni task manager is an application that allows users to create and share a task with their friends, like a basic social application.

It has been deployed to heroku and can be viewed [here](https://casoni-app.herokuapp.com/).

## Index
Casoni Task manager MS3 Project:
  - [UX](#ux)
    - [Project Goal](#project-goal)
    - [User Stories](#user-stories)
    - [Wireframes](#wireframes)
    - [Data Structure](#data-structure)
    - [Design](#design)
      - [Typography](#typography)
      - [Color Scheme](#color-scheme)
  - [Features](#features)
    - [Actual Features](#actual-features)
    - [User account](#user-account)
    - [User Session](#user-session)
    - [Security](#Security)
    - [Contact page](#contact-page)
    - [User Session](#user-session)
    - [404 page](#404-page)
  - [Future features](#future-features)
  - [Technologies Used](#technologies-used)
  - [Tools Used](#tools-used)
  - [Testing](#testing)
  - [Deployment](#deployment)
    - [MongoDB](#mongodb)
    - [Heroku](#heroku)
  - [Credits](#credits)
    - [Media](#media)
    - [Acknowledgements](#acknowledgements)

    ---

## UX

### Project Goal

The user's experience was at the center during the development of this project.
One of the goals of the project was to create an application that is intuitive and easy to use.

### User Stories

-   As a user, I want to be able to create a task that everyone can see
-   As a user, I want to be able to mark a task once it's completed
-   As a user, I want to be able to erase all the completed tasks easily
-   As a user, I want to be able to erase all the tasks when a project is finished
-   As a user, I want to see a contact page in case of any help needed
-   As a user, I want to be able to sign out removing the login session

### Wireframes

As always, here some old-style wireframes (in order: homepage, dashboard, contact)

#### homepage
![CTM responsive displays](readme-files/CTM-hp.png)
#### dashboard
![CTM responsive displays](readme-files/CTM-dash.png)
#### contact
![CTM responsive displays](readme-files/CTM-cnt.png)

### Data structure

Along with the user stories, the database collections has been delineated.
Specifically, in three main collections, using MongoDB as a non-relational database:

- #### details collection

I used this collection to test my database in the first instance (specifically,
I displayed some generic info on the home page right after having connected my
[MongoDB](https://account.mongodb.com/account/login) cluster, and database).

- #### users collection

This collection has been created to store all the unique users
(comprehensive of name, email, and encrypted password) that are registered
in the application.

_id: "id converted in a str of 32 characters (letters + numbers)" <br>
name: "user name  user last name" <br>
email:"generic@gmail[.]com" <br>
password: "encrypted password..." <br>

- #### tasks collection

The tasks collection, or our dynamic collection, let us register every user's
task through the tasks dashboard. Within the information sent
 to the database collection, a user can also manipulate the task's status,
 marking them as completed.

_id :"id converted in a str of 32 characters (letters + numbers)" <br>
new_task: "football match at 8!" <br>
complete_status: true (or false) <br>

### Design

The application was built using bootstrap and its responsive grid system.
The [Start Bootstrap scrolling-nav
template](https://startbootstrap.com/template/scrolling-nav) was used for
the main structure of the site, and its default styling was overridden by a [style.css](static/css/style.css) file.

Fonts and colors were carefully chosen to give the application a joyful and welcoming look.

#### Color scheme

Main colors used are:

- #ffe93a6b
- #DD133F
- #692020

![CTM responsive displays](readme-files/color-palette.png)

#### Typography

Fonts "Lobster" and "Kaushan", combined with the classic bootstrap font, were used
throughout the project to help the overall design looking user-friendly. 

## Features

### Actual features

#### User account

1. Every new user can create an account to access the dashboard,
using the "Sign up" form on the homepage. Once created a new account,
the user is automatically redirected to the dashboard.
2. If a user tries to create an account using an existing email, an automatic
message will display "This email address is already in use"
3. If a user tries to login account using an existing email,
an automatic message will display: "Your Login credentials are invalid".
4. If a user tries to go directly to the dashboard (even via URL),
he/she will be redirected to the homepage.

#### Dashboard

1. Use the dashboard on the dashboard page to add a new task,
and it will be visible to all your friends! Just type the task you like to add and press the "Add" button.
2. if one of the users wants to erase a task,
the only thing he/she has to do is click on it. 
3. On the contrary, if one of the users wants to remove a completed task
from the tasks list, he/she can use the "Remove completed" button.
4. A user can always remove all the tasks (completed or not) by clicking the
"Remove all" button directly.
5. To sign out completely, just use the "Sign out" button (below the dashboard). It will
redirect you to the homepage, cancelling your current session. 

#### Security

Every password used to signup is encrypted before being sent to the database.

#### Contact page

For more support, the user can click on the contact page to see the support phone number.

#### 404 page

Cannot find the right page? the 404 page will show you a link to help you go back to the homepage

### Future features
- defensive programming for deleting tasks
- dark mode
- multiple private groups where you can add only the user you like
- personal dashboard 
- contact form that will send us an email
- receiving an email after being registered, and password recovery system

## Technologies Used

-   HTML
-   CSS / Bootstrap
-   JavaScript / JQuery
-   AJAX
-   Python
-   Flask
-   Fontawesome
-   Fonts Google

## Tools Used

-   [GitHub](https://github.com/) for version control
-   [Heroku](https://heroku.com/) to deploy the application
-   [Chrome developer tools](https://developers.google.com/web/tools/chrome-devtools) to deploy the application
-   [Grammarly](https://app.grammarly.com/) to check possible grammar errors
-   [Responsive viewer extension](https://chrome.google.com/webstore/detail/responsive-viewer/inmopeiepgfljkpkidclfgbgbmfcennb) to check responsiveness

## Testing

Testing was done manually throughout the development process.<br>
Below, my manual test procedures to assess functionality, usability,
responsiveness and data management within the Full Stack web application.<br>

here the points that had to be tested and that I have tested:

- Signup
    1. Signup form will have to respect: a unique email, a minimum of 6 characters, and all the fields need to be filled up.
    2. The signup form will have to send all the data correctly to the users' collection in the database.
    3. If valid, it will have to redirect the user to the dashboard page, with a session.
    4. If the email address is already in use, it will have to display an error.

- Login
    1. Login form will have to respect a minimum of 6 characters, and all the fields need to be filled up.
    2. The login form will have to check all the data sent from the signup form, and verify if the user already exists in the database.
    3. If valid, it will have to redirect the user to the dashboard page, with a session.
    4. If the email and/or password credentials are not valid, it will have to display an error.


- Routes
    1. All routes need to work properly and redirect the user to the proper one.
    2. Each route needs to activate the respective function when used.

- Menu
    1. The toggle menu needs to open properly and be responsive.
    2. All the links in the menu need to work, and need to redirect the user to the correct link.
    3. The dashboard link has to redirect the user to the dashboard only if the user session is active.
    4. The toggle menu needs to expand all of its links in a full page and minimise itself in small/medium pages.

- Dashboard page 
    1. Tasks dashboard
        1. It will have to let the user do all the CRUD functions.
        2. It needs to be connected to the dashboard form.
        3. Initially, it will have to register a status 200, whenever a task is sent to the database.
        4. If the add button is clicked, the dashboard will display the task right below the "remove" buttons.
        5. If a task is clicked, it will have to redirect you again to the dashboard page, and the task will be marked with a line.
        6. If the "remove completed" button is clicked, it will remove all the tasks having the database key "complete_status" equal to "true".
        7. If the "remove all" button is clicked, it will have to delete all the tasks present in the dashboard.

    2. User card
        - The user card will have to show a welcome message with the name, and email, of the user who has already signed up/logged in.

- The 404 page
    - If you Cannot find the right page, in the url, the 404 page will show up and it will present you a link to go back to the homepage

- Responsiveness
    1. The application will need to be tested on multiple browsers
    2. The application will need to be tested on multiple devices
    3. The application will need to be tested on multiple display-sizes
    4. The application will need to be tested on multiple 
    5. The navigation, layout and various functionalities will be tested across various screen sizes with chrome developer tools and with the Responsive Viewer Chrome extension.


All code was validated in the following ways:

**HTML** - All pages were successfully run through the [W3C HTML Validator](https://validator.w3.org/)
to ensure compliance with the standards set by the W3C, excluding the python code used within them.

**CSS** - The style.css file was successfully run through the the W3C's [Jigsaw Validator](https://jigsaw.w3.org/css-validator/).

**Python** - All Python code was checked with the [PEP8 online validator](http://pep8online.com/) and is PEP8 compliant.

## Deployment

Before deploying the application, ensure the following are installed:

-   [Python 3](https://www.python.org/)
-   [PIP](https://pypi.org/project/pip/)
-   [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli)

The application relies on the following service, and accounts will have to be created for it:

### MongoDB:

- connecting [MongoDB:](https://www.mongodb.com/) <br>Thanks to [TravelTimN](https://github.com/TravelTimN):
      [mongoSetup.md](https://github.com/Code-Institute-Solutions/MongoDB/blob/master/01-CreateAMongoDBDatabase/01-create_a_mongodb_database/mongoSetup.md)

### Heroku:

-  connecting to [Heroku:](https://heroku.com/)
    <br><br>To deploy the application to Heroku, use the following steps:

    1. Login to your Heroku account and create a new app.

    2. Ensure the Procfile and requirements.txt files exist are present in your repository.

        The Procfile should contain the following line:

        ```
        web: python app.py
        ```

        To ensure requirements.txt exists and is up to date, use the following line in your terminal:

        ```
        pip3 freeze --local > requirements.txt
        ```

    3. Connect heroku to your github repository using the "Deployment method", in the "Deploy" page of your heroku app:
        - https://dashboard.heroku.com/apps/%3Capp-name%3E/deploy/github 
        - Push the application automatically to heroku with Automatic deploys, always in the "Deploy" section

    4. In your app in heroku, go to settings, reveal the config vars and enter the following variables:

        | Variable       | Value               |
        | -------------- | ------------------- |
        | IP             | 0.0.0.0             |
        | PORT           | 5000                |
        | MONGODB_NAME   | YOUR_DB_NAME        |
        | MONGO_URI      | YOUR_MONGO_URI      |
        | SECRET_KEY     | YOUR_SECRET_KEY     |

    5. Go to the deploy tab of your application, and click "Deploy Branch" under the manual deploy section.

    6. The application is now deployed to heroku, and it can be accessed by clicking the "Open App" button on the top right.


### Acknowledgements

-   [Felipe Alarcon](https://github.com/fandressouza), my mentor
-   [Start Bootstrap scrolling-nav template](https://startbootstrap.com/template/scrolling-nav), and the whole bootstrap team
-   [Pretty Printed](https://www.youtube.com/channel/UC-QDfvrRIDB6F0bIO4I4HkQ) for his python tutorials on youtube, especially regarding CRUD operation
-   [Luke peters](https://www.youtube.com/channel/UC6Oowe4rpbQXo6AmRHmDMYg) for his python tutorials on youtube, especially regarding registration and login forms
-   [Jumboduck](https://github.com/jumboduck) for his readme file template
-   [Myself](https://github.com/Simocaso), and my genetic and passion for coding;
as I was able to code all day and sleep 10h in 5 days to finish this project :')

[GO UP](#index)