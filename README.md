## Updated for Defcon Readteam Village 8/5/2020:  [Training Readme Here](https://github.com/jzadeh/aktaion2/blob/master/defcon2020/TrainingAbstract.md)

# Aktaion V2: Open Source Tool For Microbehavior Based Exploit Detection

Aktaion V2 is a python3 project for detecting exploits (and more generally attack behaviors).  
The project is meant to be a learning/teaching tool on how to blend multiple security signals and behaviors into an expressive framework for intrusion detection.  
The key abstraction we wanted to prototype is the idea of a Microbehavior.  
This concept helps to provide an expressive mechanism to add high level IOCs such as timing behavior of a certain Malware family in parallel to simple statistics, 
rules or anything relevant to building a programmatic description of a sequential evolving set of adversary behaviors.
Current project URL: <http://www.github.com/jzadeh/aktaion2>
The original Java/Scala code is located here: <http://www.github.com/jzadeh/aktaion>

## Project Setup (use python 3): 
To run the project make sure you have the latest python3/pip3 and virtual environment setup.  Then run the command 

`pip install virtualenv && virtualenv -p python3 venv && source venv/bin/activate && pip install -r requirements.txt`

## Running the main program
To execute the main program use the shell script in the root directory

`./aktaion2.sh`

The logic has two paths exposed right now. Select option 1 for demo mode and select option 2 for analyzing a file.

# Running the ML Logic in debug mode
This will use verbose printing of feature vector extraction and parsing logic for data in hardcoded directories linked 
to the project. This is useful for debugging specific issues related to the parsing of input files for building the 
ML workflow:

`./build_machine_learning_dataset.sh`
