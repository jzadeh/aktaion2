# Aktaion: Behavior Based Exploit Detection Prototype

<p align="center">
  <img src="https://github.com/jzadeh/aktaion2/blob/master/graphics/aktaion_fractal_juliaset2.png" width="400" height="400">
</p>


## Updated for Defcon 28 Redteam Village 8/8/2020: 
[Training Readme Here](https://github.com/jzadeh/aktaion2/blob/master/defcon2020/TrainingAbstract.md)

Redteam Village Defcon 28 Links: [Homepage](https://redteamvillage.io/), 
[Discord](https://discord.gg/redteamvillage), 
[Training Link](https://www.eventbrite.com/e/aktaion-v2-open-source-tool-for-microbehavior-based-exploit-detection-tickets-115593759045)

<p align="center">
    <img src="https://github.com/jzadeh/aktaion2/blob/master/defcon2020/RTV-logo-high-res.png" width="250" height="250"> 
</p>

## Aktaion V2: Open Source Tool For Microbehavior Based Exploit Detection

Aktaion is a machine learning open source & active defense (orchestration) prototype. 
The tool focuses on the detection of Ransomware based on machine learning techniques, independent of static-based signatures. 
The tool has been mentioned and featured in may respected community publications and research, and in years past presented at a variety of Blackhat Arsenal events. 
AKTAION v2 is the second iteration or port of the project from the original Java into Python3.

The port to python  is meant to be a learning/teaching tool on how to blend multiple security signals and behaviors into an expressive framework for intrusion detection. The key abstraction we wanted to prototype is the idea of a Microbehavior.  
This concept helps to provide an expressive mechanism to add high level IOCs such as timing behavior of a certain Malware family in parallel to simple statistics, rules or anything relevant to building a programmatic description of a sequential evolving set of adversary behaviors.

1. *Current Project Repo*: <http://www.github.com/jzadeh/aktaion2>
2. The original Java/Scala code is located in an older repo here: <http://www.github.com/jzadeh/aktaion>

### Project Setup (use python 3): 
To run the project make sure you have the latest python3/pip3 and virtual environment setup.  Then run the command 

`pip install virtualenv && virtualenv -p python3 venv && source venv/bin/activate && pip install -r requirements.txt`

### Running the main program
To execute the main program use the shell script in the root directory

`./aktaion2.sh`

The logic has two paths exposed right now. Select option 1 for demo mode and select option 2 for analyzing a file.

### Running the ML Logic in debug mode
This will use verbose printing of feature vector extraction and parsing logic for data in hardcoded directories linked 
to the project. This is useful for debugging specific issues related to the parsing of input files for building the 
ML workflow:

`./aktaion2_ml_debug.sh`
