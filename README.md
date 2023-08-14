# AirBnB Clone - The Console
#### Welcome to the AirBnB Clone Project. 
This project dives deep into deploying a simple copy of the AirBnB website. The first part of this project is to create a command interpreter to manipulate data without a visual interface, like in a Shell (perfect for development and debugging). 

# Description
- Create a data model that should manage (create, update, destroy, etc) objects via a console / command interpreter
store and persist objects to a file (JSON file)
- The first piece is to manipulate a powerful storage system. This storage engine will give us an abstraction between “My object” and “How they are stored and persisted”. This means: from your console code (the command interpreter itself) and from the front-end and RestAPI you will build later, you won’t have to pay attention (take care) of how your objects are stored.
- This abstraction will also allow you to change the type of storage easily without updating all of your codebase.
- The console will be a tool to validate this storage engine

Each task is linked and will help you to:

- Put in place a parent class (called BaseModel) to take care of the initialization, serialization and deserialization of your future instances
- Create a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file
- Create all classes used for AirBnB (User, State, City, Place, Amenity, Review) that inherit from BaseModel
- Create the first abstracted storage engine of the project: File storage.

# Usage
- The console can be run in both interactive and non-interactive mode.
- It prints a prompt **(hbnb)** and waits for the user for input.

## Interactive Mode
```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb)
(hbnb)
(hbnb) quit
$
```

## Non-interactive Mode
```
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$
```

