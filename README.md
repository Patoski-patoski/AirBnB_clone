# AirBnB_clone

0x00. AirBnB - The console
Description of the project This is the first step towards building your first full web application: the AirBnB clone. The aim of the project is to deploy a replica of the Airbnb Website using my server. The final version of this project will have:

- A command interpreter to manipulate data without a visual interface, like a shell (for development and debugging)
- A website (front-end) with static and dynamic functionalities
- A comprehensive database to manage the backend functionalities
- An API that provides a communication interface between the front and backend of the system.

Resources Videos showing examples of how various parts of the project work, listed below:

- https://www.youtube.com/playlist?list=PLlLHfkTcnvmPOp6jv_89tRpJUMFrP-Wbi HBNB videos
- https://www.youtube.com/watch?v=QTwmCB_AWqI Holberton Airbnb overview
- https://www.youtube.com/watch?v=jeJwRB33YNg The Airbnb Console
- https://www.youtube.com/watch?v=ZwCD8cNZk9U Airbnb ORM
- https://www.youtube.com/watch?v=LrQhULlFJdU Airbnb API
- https://www.youtube.com/watch?v=m-cfupVumos Final product
- Other resource
- https://docs.python.org/3.8/library/cmd.html cmd module
     -packages concept page
     -https://docs.python.org/3.4/tutorial/modules.html#packages Python packages
     -https://docs.python.org/3.8/library/uuid.html uuid module
     -https://docs.python.org/3.8/library/datetime.html datetime
     -https://docs.python.org/3.8/library/unittest.html#module-unittest unittest module
     -https://yasoob.me/2013/08/04/args-and-kwargs-in-python-explained/ args/kwargs
     -https://www.pythonsheets.com/notes/python-tests.html Python test cheatsheet
     -https://www.airbnb.com/ AirBnB website

Aims & Objectives of this project This will help to be able to manage the objects of our project:

- Creation of a new object (ex: a new "User" or a new "Place")
- Retrieval of an object from a file storage, a database etc…
- Perform operations on objects (count, compute stats, etc…)
- Update attributes of an object
- Destroy an object

The created objects The list of the objects (instances) that can be created are as follows:

- BaseModel
- User
- City
- Amenity
- State
- Review
- Place

Files and Directories

- models directory contains all classes used for the entire project. A class, called “model” in a OOP project is the representation of an object/instance.
- tests directory contains all unit tests.
- console.py file is the entry point of our command interpreter.
- models/base_model.py file is the base class of all our models. It contains common elements:
     - attributes: id, created_at and updated_at
     - methods: save() and to_json()
- models/engine directory contains all storage classes (using the same prototype). For the moment I will have only one: file_storage.py.
The project's implementation will happen in the following phases:

Phase OneDescription of the command interpreter The first phase is to manipulate a powerful storage system to give an abstraction between objects and how they are stored and persisted. To achieve this, I will:

- put in place a parent class (called BaseModel) to take care of the initialization, - serialization and deserialization of my future instances
- create a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file
- create all classes used for AirBnB (User, State, City, Place…) that inherit from BaseModel
- create the first abstracted storage engine of the project: File storage.
- create all unittests to validate all our classes and storage engine
- Create a data model
- Manage (create, update, destroy, etc) objects via a console/command interpreter
- Store and persist objects to files (JSON files)
- Commands Implemented Description of the command interpreter

Commands and Description

- quit=This command quits or exits the console
- EOF=This command quits or exits the console interpreter when pressed Ctrl+D
- help or help =Displays all commands or Displays instructions for a specific command (Ex: help or help quit).
- create =Creates an object of type, saves it to a JSON file, and prints the objects ID (Ex: create BaseModel or BaseModel.create())
- show =Shows string representation of an object (Ex: show BaseModel 1234-1234-1234 or BaseModel.show("1234-1234-1234"))
- destroy =Deletes an objects based on the class name and id (Ex: destroy BaseModel 1234-1234-1234 or BaseModel.destroy("1234-1234-1234")).
- all or all =Prints all string representations of all objects or Prints all string representations of all objects of a specific class (Ex: all BaseModel or all or User.all()).
- update ""=Updates an object with a certain attribute (new or existing) (Usage: update ").
- .all()=Same as all
- .count()=Retrieves the number of objects of a certain class (Usage: .count(), Example: User.count()).
- .show()=Same as show
- .destroy(=Same as destroy
- .update(, , =Same as update
- .update(, )=Updates an objects based on a dictionary representation of attribute names and values
Compilation To start up the interpreter, clone this repository, and run the console file on linux as follows:

- Clone this repository: git clone "github.com/MamaboloKatlego/AirBnB_clone.git"
- Access AirBnb directory: cd AirBnB_clone
- Run hbnb(interactively): ./console and then press enter command
- Run hbnb(non-interactively): echo "" | ./console.py
$ ./console.py (hbnb) help

Documented commands (type help ):
EOF help quit (hbnb) (hbnb) (hbnb) quit $ But also in non-interactive mode: (like the Shell project in C)

$ echo "help" | ./console.py (hbnb)

Documented commands (type help ):
EOF help quit (hbnb) $ $ cat test_help help $ $ cat test_help | ./console.py (hbnb)

Documented commands (type help ):
EOF help quit (hbnb) $

guillaume@ubuntu:~/AirBnB$ ./console.py (hbnb) all MyModel ** class doesn't exist ** (hbnb) show BaseModel ** instance id missing ** (hbnb) show BaseModel My_First_Model ** no instance found ** (hbnb) create BaseModel 49faff9a-6318-451f-87b6-910505c55907 (hbnb) all BaseModel ["[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'id': '49faff9a-6318-451f-87b6-910505c55907', 'updated_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903300)}"] (hbnb) show BaseModel 49faff9a-6318-451f-87b6-910505c55907 [BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'id': '49faff9a-6318-451f-87b6-910505c55907', 'updated_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903300)} (hbnb) destroy ** class name missing ** (hbnb) update BaseModel 49faff9a-6318-451f-87b6-910505c55907 first_name "Betty" (hbnb) show BaseModel 49faff9a-6318-451f-87b6-910505c55907 [BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'first_name': 'Betty', 'id': '49faff9a-6318-451f-87b6-910505c55907', 'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'updated_at': datetime.datetime(2017, 10, 2, 3, 11, 3, 49401)} (hbnb) create BaseModel 2dd6ef5c-467c-4f82-9521-a772ea7d84e9 (hbnb) all BaseModel ["[BaseModel] (2dd6ef5c-467c-4f82-9521-a772ea7d84e9) {'id': '2dd6ef5c-467c-4f82-9521-a772ea7d84e9', 'created_at': datetime.datetime(2017, 10, 2, 3, 11, 23, 639717), 'updated_at': datetime.datetime(2017, 10, 2, 3, 11, 23, 639724)}", "[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'first_name': 'Betty', 'id': '49faff9a-6318-451f-87b6-910505c55907', 'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'updated_at': datetime.datetime(2017, 10, 2, 3, 11, 3, 49401)}"] (hbnb) destroy BaseModel 49faff9a-6318-451f-87b6-910505c55907 (hbnb) show BaseModel 49faff9a-6318-451f-87b6-910505c55907 ** no instance found ** (hbnb)

Authors

- Mamabolo katlego
- Okafor Patrick Chibuike
