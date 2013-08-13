NEURON
backend os - linux
Requirements and procedures
1) Set environmental variable for PROJECT_HOME=../neuron
2) Python virutalenv <name>
3) activate virtualenv - source <name>/bin/activate
4) install mongodb - http://docs.mongodb.org/manual/installation/
5) pip install pyramid
6) pip install pyramid_mongodb
7) pip install pyramid_beaker
8) pip install pymongo
9) pip install velruse
10) cd ../neuron -> pip install -e .
11) Now run the project -> pserve developement.ini --reload
