NEURON
checking conflicts
backend os - linux/mac OS
Requirements and procedures
1) Set environmental variable for PROJECT_HOME=../neuron
2) Install pip in your system - sudo easy_install pip
3) Install virtualenv in your system (pip install virtualenv)
4) Create virtual python environment (virtualenv <temp_name>)
5) activate virtualenv - source <name>/bin/activate
6) install mongodb - http://docs.mongodb.org/manual/installation/
// make sure pip is installed
7) pip install pyramid
8) pip install pyramid_mongodb
9) pip install pyramid_beaker
10) pip install pymongo
11) pip install velruse
12) cd ../neuron -> pip install -e .
13) start mongodb server (sudo mongod)
14) Now run the project -> pserve developement.ini --reload
