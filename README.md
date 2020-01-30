# Registart Survey Web App

## Table of contents
* [Overview](#overview)
* [Functionality](#functionality)
* [How it Works](#how-it-works)
* [Platform Requirements](#platform-requirements)
* [Configuration](#configuration)
* [Running the Application](#running-the-application)

# Overview
A simple and brief survey developed with the Flask Microframework for Registart, a nonprofit startup that allows high school seniors to encourage their peers to register to vote.

# Functionality
Students can take the survey by inputting their information regarding their relationships with their peers in their NNHS activities and the senior class and obtain a list of 20 students that they should encourage to register to vote. 

Currently, the skeleton and the foundation are the only features of the web app for now. Therefore, pages will render as they should but there is no functionality within the database yet.

# How it Works
By taking this survey, sudent organizers will be able the know exactly what Registart is, the Illinois Voter Registration Process, and a guide on how to encourage their peers to vote. Students will enter their activities and their relationships to their senior class peers and obtain a list of 20 student targets.

# Platform Requirements
- Windows 7 or above <br/>
- MacOS and Unix compatible <br/>

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
$ venv/scripts/activate     # activate the virtual environment  
$ pip install -r req.txt    # install all the packages needed for the app to run
```

<strong>MacOS:</strong><br/>
```
$ python3 -m venv venv 
$ source venv/bin/activate 
$ pip3 install -r req.txt 
```

# Running the Application
In the terminal, input the following command.<br/>
<br/><strong>Both Operating Systems: </strong><br/>
```
(venv) $ flask run
```
The terminal then displays a link to localhost (A local server) <br/>
``` 
* Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```
CTRL+Click to launch the link and run the application and the index page will display. <br/>

## Team Members
* Tom Carsello
* Luke Zhang
* James Huang
* Ethan He
