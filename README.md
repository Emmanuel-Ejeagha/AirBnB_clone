# AirBnB_clone

![image](https://github.com/Emmanuel-Ejeagha/AirBnB_clone/assets/116760178/621aaacb-4fca-479d-ab7d-ea04dea84e57)

<p>This project contains many packages and modules.</p>
It is expected to run on the console using the cmd prompt.
<p>Example:</p>

```
python

>>> greet_user Prince 
Hello Prince
```
This project contains series of steps....

Airbnb Clone Project
Airbnb Clone is a complete web application that integrates database storage, a back-end API, and front-end interfacing, aiming to mimic the functionalities of Airbnb. As of now, the project has only implemented the back-end console.

Classes
Airbnb utilizes the following classes:

BaseModel
FileStorage
User
State
City
Amenity
Place
Review
Public Instance Attributes
id
created_at
updated_at
All classes inherit these attributes from the BaseModel class.

Public Instance Methods
save
to_dict
These methods are inherited by all classes and provide common functionality.

Public Class Attributes
email
password
first_name
last_name
These attributes are specific to the User class.

name
state_id
These attributes are specific to the State class.

name
city_id
These attributes are specific to the City class.

user_id
name
description
number_rooms
number_bathrooms
max_guest
price_by_night
latitude
longitude
amenity_ids
These attributes are specific to the Place class.

place_id
user_id
text
These attributes are specific to the Review class.

Private Class Attributes
file_path
objects
These attributes are specific to the FileStorage class, which handles storage operations for all other classes.

Storage
The classes mentioned above are managed by the abstracted storage engine defined in the FileStorage class. Every time the backend is initialized, Airbnb instantiates an instance of FileStorage called storage. This object is responsible for loading and re-loading data from class instances stored in the file.json file. Any changes made to class instances, including creation, updates, or deletions, are registered in the file.json file using the storage object.

Console
The console is a command line interpreter designed to manage the backend of Airbnb. It provides tools to manipulate and handle all classes used by the application, utilizing the storage object mentioned above.

Using the Console
The Airbnb console can be run interactively or non-interactively. To run it in non-interactive mode, pipe commands into the console.py file at the command line.

bash
Copy code
$ echo "help" | ./console.py
(hbnb)
Alternatively, you can run the console in interactive mode by executing the console.py file by itself.

bash
Copy code
$ ./console.py
(hbnb)
While running in interactive mode, the console displays a prompt for input. To exit the console, use the quit command or input an EOF signal (ctrl-D).

Console Commands
The Airbnb console supports the following commands:

create: Creates a new instance of a given class. The class's ID is printed, and the instance is saved to the file.json file.

show: Prints the string representation of a class instance based on a given ID.

destroy: Deletes a class instance based on a given ID. The file.json file is updated accordingly.

all: Prints the string representations of all instances of a given class. If no class name is provided, it prints all instances of every class.

count: Retrieves the number of instances of a given class.

update: Updates a class instance based on a given ID with a key/value attribute pair or a dictionary of attribute pairs. The type of attributes that can be updated depends on the format of the update command.

That's a summary of the Airbnb Clone project, its classes, storage mechanism, and how to interact with the console.