# Aktaion V2: Open Source Tool For Microbehavior Based Exploit Detection

Aktaion V2 is a python3 project for detecting exploits (and more generally attack behaviors).  The project is meant to be a learning/teaching tool on how to blend multiple security signals and behaviors into an expressive framework for intrusion detection.  The key abstraction we wanted to protoype is the idea of a microbehavior.  This concept helps to provide an expressive mechanism to add high level IOCs such as timing behavior of a certain malware family in parrallel to simple statsitcs, rules or anything relevant to building a programmitic descpriotn of a sequential evolving set of advesary behaviors.

Current project URL: <http://www.github.com/jzadeh/aktaion2>

The original Java/Scala code is located here: <http://www.github.com/jzadeh/aktaion>

# Project Setup (use python 3): 

pip install virtualenv && virtualenv -p python3 venv && source venv/bin/activate && pip install -r requirements.txt

# Running the demo

./run_aktaion2.sh

# Running the ML Logic in debug mode

./build_machine_learning_dataset.sh
