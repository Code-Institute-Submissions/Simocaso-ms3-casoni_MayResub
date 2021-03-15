# ms3-casoni

![Casoni Task manager logo](readme-files/ctm-logo.png)

# Casoni Task manager

![CTM responsive displays](readme-files/CTM-responsive.png)

With this README file, I'll guide you through my MS3 project for the DUBLIN CODE INSTITUTE.
If looking at my commits' time, you are wondering if multiple people were working on this project, then the answer is no; I just didn't sleep at all.
However, this is not a complaint. I simply would like to show you my passion for studying coding (even in these terrible times, where is very hard to find your motivation).

Casoni task manager is an application that allows users to create and share a task with their friends, like a basic social application.

It has been deployed to heroku and can be viewed [here](https://casoni-app.herokuapp.com/).

- Casoni Task manager MS3 Project
  - [UX](#ux)
    - [Project Goal](#project-goal)
    - [User Stories](#user-stories)
    - [Wireframes](#wireframes)
    - [Views and Data Structure](#views-and-data-structure)
    - [Design](#design)
      - [Typography](#typography)
      - [Color Scheme](#color-scheme)
  - [Features](#features)
    - [Existing Features](#existing-features)
      - [Account Registration](#account-registration)
      - [User Session](#user-session)
      - [About Page](#about-page)
      - [Create New Entries](#create-new-entries)
      - [List and Search Entries](#list-and-search-entries)
      - [View, Edit, and Delete Entries](#view-edit-and-delete-entries)
      - [Profile and Account Management](#profile-and-account-management)
      - [Send Feedback](#send-feedback)
      - [Security](#security)
    - [Features Left to Implement](#features-left-to-implement)
  - [Technologies Used](#technologies-used)
  - [Tools Used](#tools-used)
  - [Testing](#testing)
  - [Deployment](#deployment)
    - [Local Deployment](#local-deployment)
    - [Deployment to Heroku](#deployment-to-heroku)
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
-   As a user, I want to be able to sign out removing login session

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
Specifically, in three main collections, using MongoDB as a non relational database:

- #### details collection

I used this collection to test my database in the first instance (specifically,
I displayed some generic info on the home page right after having connected my
[MongoDB](https://account.mongodb.com/account/login) cluster, and database).

- #### users collection

This collection has been created to store all the unique users
(comprehensive of name, email, and encrypted password) that are registered
in the application.

_id: "id converted in a str of 32 characters (letters + numbers)" <br>
name: "user user" <br>
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
Main colors used are:

- #ffe93a6b
- #DD133F
- #692020

![CTM responsive displays](readme-files/color-palette.png)

#### Typography

Fonts "Lobster" and "Kaushan", combined with the classic bootstrap font, were used
throughout the project to help the overall design looking user-friendly. 