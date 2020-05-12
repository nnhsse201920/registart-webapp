# RegiStart Survey Web App

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

The app uses a Docker container to simplify the process of setting it up.

### Activities Page
![image](https://github.com/nnhsse201920/registart-webapp/blob/master/Page%20Screenshots/activities.png) <br/>
The number of activities that the organizer chooses to enter is all up to them as the app uses something called a SelectMultipleField: an input field where the user can search up the activities that they want and select multiple of them at once. The builtin SelectMultipleField in Flask is overhauled by an external library called [Select2](select2.org).

### Relationships Page
![image](https://github.com/nnhsse201920/registart-webapp/blob/master/Page%20Screenshots/relationships.png) <br/>
The relationships page uses a cycling system powered by JQuery. Each name of the  senior class is displayed on the screen one at a time and there is a binary choice system where the user can click 'Yes' or 'No' if they know them. The next name immediately appears after clicking. This cycling system greatly expedites the process of filtering out the senior class to find students that the organizer knows. There are arrow (< and >) buttons to the side of the displayed name which allows organizers to go back and change their decision if they made a mistake.

### Relationship Rankings Page
![image](https://github.com/nnhsse201920/registart-webapp/blob/master/Page%20Screenshots/rankings.png) <br/>
The rankings page uses the same cycling system as the previous one. The page prompts the user to indicate how well they know each of the students that they said 'Yes' to. There are 4 options to choose from: Very Well, Well, Somewhat, and Not Much. Each of this has an integral value (1-4) associated with it and will be assigned to the student that they select it for. Upon selecting a choice, the next name will immediately be displayed. There are also arrow (< and >) buttons to the side of the displayed name which allows organizers to go back and change their decision if they made a mistake.

### After the survey
This data collected from the survey will then be inputted to the high perfomance matching algorithm which will then generate a list of personalized targets for organizers. These targets can be viewed on the mobile app.

# Platform Requirements
- Windows 7+ or MacOS X <br/>
- [VSCode](https://code.visualstudio.com/) 
- Latest version of [Docker Desktop](https://www.docker.com/products/docker-desktop) (Windows Pro editions)
- Latest version of [Docker Toolbox](https://docs.docker.com/toolbox/toolbox_install_windows)  (Windows consumer editions)
- Latest version of [Python](https://www.python.org/downloads)


# Configuration 
To setup this project, ensure that [Python](https://www.python.org/) and its respective [VSCode extension](https://code.visualstudio.com/docs/python/python-tutorial) are installed. <br/>

Working directory: ``\Users\[USER]\Documents\GitHub\registart-webapp`` <br/>

### Starting Docker
Make sure that you follow ALL the instructions for successfully installing Docker Desktop/Toolbox and verifying its installation.

Docker Desktop can be easily launched from the desktop or the programs menu. <br/>
For Docker Toolbox, start Kitematic. <br/>

### Building the necessary Docker images for the FIRST time
Open up a new terminal for each image, and run a command in each one dedicated to it. (e.g. Run database command in one terminal, application in another)

<strong>Database: </strong>  ``docker-compose up --build db`` <br/>
<strong>Application: </strong>  ``docker-compose up --build webapp`` <br/>
<strong>Phpmyadmin: </strong>  ``docker-compose up --build app`` <br/>

# Running the Application

### Setting up Docker containers AFTER building them
<strong>Database: </strong>  ``docker-compose up db`` <br/>
<strong>Application: </strong>  ``docker-compose up webapp`` <br/>
<strong>Phpmyadmin: </strong>  ``docker-compose up app`` <br/>

Open up a new terminal for each image, and run a command in each one dedicated to it. (e.g. Run database command in one terminal, application in another)

### Launching the app

The application runs on port 80. <br/>
Go to [127.0.0.1](http://127.0.0.1/) or [localhost](localhost) to view the main page.

### Main Page
![](https://github.com/nnhsse201920/registart-webapp/blob/master/Page%20Screenshots/landing.png)

## Team Members
* Tom Carsello
* Luke Zhang
* James Huang
* Ethan He
