# Registart Survey Web App

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
1. Clone the repository from GitHub

2. Ensure that [Python](https://www.python.org/) and its respective [VSCode extension](https://code.visualstudio.com/docs/python/python-tutorial) is installed. <br/>

3. Navigating to the Project
Project path: ``\Users\[USER]\Documents\GitHub\registart-webapp\Project``
<strong>Through a terminal:</strong><br/>
Open a terminal and ``cd`` to the 'Project' folder<br/>
Then, input ``code .`` to launch VSCode and the Project.<br/>

<strong>Through VSCode:</strong><br/>
Open VSCode and click 'Open Folder' ``\Users\[USER]\Documents\GitHub\registart-webapp\Project``
Navigate to the project path:

4. Setting up the Python Virtual Environment
Flask Applications needs a virtual environment to run.  <br/>
Input the following commands into the terminal for configuration: <br/>
<br/>
<strong>Windows:</strong><br/>
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
In the terminal, input the following command.
<strong>Both Operating Systems: </strong><br/>
```
(venv) $ flask run
```
The terminal displays a link to localhost (A local server) <br/>
``` 
* Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```
CTRL+Click to launch the link and run the application and the index page will display. <br/>

## Team Members
* Tom Carsello
* Luke Zhang
* James Huang
* Ethan He
