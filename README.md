# Registart Survey Web App

## Table of contents
* [Overview](#overview)
* [What it Does](#what-it-does)
* [How it Works](#how-it-works)
* [Platform Requirements](#platform-requirements)
* [Configuration](#configuration)
* [Running the Application](#running-the-application)

# Overview
This web application is a brief and simple survey for student organizers of the RegiStart program. Taking this survey will generate a list of personalized targets for the organizer which can be viewed on the RegiStart mobile app.

# What it Does
Student organizers will first enter however many activities that they are committed to at their school or organization. They will then filter out the students they know out of their entire senior class through a quick and seamless process. This will narrow the names down to where the organizer can indicate their relationship strength for the people they are familiar with.

# How it Works

### Technologies Used
The application uses Flask, a web development framework, which provides libraries, modules, and tools to build a functional web application. It handles much of the backend elements of the app.

The application also uses the official [Bootstrap](https://getbootstrap.com/docs/3.3/) library as well as its built-in variant within Flask for its frontend elements. 

JQuery is used to power the functionality of the Activities and Relationships page which allows for the survey process to be much faster.

### Activities Page
The number of activities that the organizer chooses to enter is all up to them as the app uses something called a SelectMultipleField: an input field where the user can search up the activities that they want and select multiple of them at once. The builtin SelectMultipleField in Flask is overhauled by an external library called [Select2](select2.org) with BootStrap.

### Relationships Page
The relationships page uses a cycling system powered by JQuery. Each name of the  senior class is displayed on the screen one at a time and there is a binary choice system where the user can click 'Yes' or 'No' if they know them. The next name immediately appears after clicking. This cycling system greatly expedites the process of filtering out the senior class to find students that the organizer knows. There are arrow (< and >) buttons to the side of the displayed name which allows organizers to go back and change their decision if they made a mistake.

### Relationship Rankings Page
The rankings page uses the same cycling system as the previous one. The page prompts the user to indicate how well they know each of the students that they said 'Yes' to. There are 4 options to choose from: Very Well, Well, Somewhat, and Not Much. Each of this has an integral value (1-4) associated with it and will be assigned to the student that they select it for. Upon selecting a choice, the next name will immediately be displayed. There are also arrow (< and >) buttons to the side of the displayed name which allows organizers to go back and change their decision if they made a mistake.

### After the survey
This data collected from the survey will then be inputted to the high perfomance matching algorithm which will then generate a list of personalized targets for organizers. These targets can be viewed on the mobile app.

# Platform Requirements
- Windows 7+ or MacOS X <br/>
- [VSCode](https://code.visualstudio.com/) 
- Latest version of [Docker Desktop](https://www.docker.com/products/docker-desktop) (Windows Pro editions)
- Latest version of [Docker Toolbox](https://docs.docker.com/toolbox/toolbox_install_windows)  (Windows consumer editions)


# Configuration 
To setup this project, ensure that [Python](https://www.python.org/) and its respective [VSCode extension](https://code.visualstudio.com/docs/python/python-tutorial) are installed. <br/>

Project path: ``\Users\[USER]\Documents\GitHub\registart-webapp\Project`` <br/>
<br/>
<strong>Through a terminal:</strong><br/>
Open a terminal and ``cd`` to the 'Project' folder<br/>
Then, input ``code .`` to launch VSCode and the Project.<br/>

<strong>Through VSCode:</strong><br/>
Open VSCode and click 'Open Folder' <br/>
Navigate to the project path:  ``\Users\[USER]\Documents\GitHub\registart-webapp\Project``

Flask Applications needs a virtual environment to run.  <br/>
If you are in VSCode, click on 'Terminal' on the top of the window and open a new terminal. <br/>
Input the following commands into the terminal to set up a virtual environment: <br/>
<br/><strong>Windows:</strong><br/>
```
$ python -m venv venv       # create a virtual environment for Python 
$ venv\scripts\activate     # activate the virtual environment  
(venv) $ pip install -r requirements.txt    # install all the packages needed for the app to run
```

<strong>MacOS X:</strong><br/>
```
$ python3 -m venv venv 
$ source venv/bin/activate 
(venv) $ pip3 install -r requirements.txt 
```

# Running the Application
In the terminal, input the following commands.<br/>

<strong>Step 1:</strong> Start databases in Docker container from [Database GitHub Repository](https://github.com/nnhsse201920/database-migration)
* NOTE: Only build the image on the first run. Rebuilding the image on future runs will clear the contents of the database. 

<strong>First Run ONLY - Initialize Database</strong><br/>
```
(venv) $ flask db init
(venv) $ flask db migrate
(venv) $ flask db upgrade
```
<br/><strong>Starting the server: </strong><br/>
```
(venv) $ flask run
```
The terminal then displays a link to localhost (A local server) <br/>
``` 
* Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```
Do CTRL+LMB to launch the link and run the application and the RegiStart landing page will display. <br/>
The Flask server runs on

## Team Members
* Tom Carsello
* Luke Zhang
* James Huang
* Ethan He
