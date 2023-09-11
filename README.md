# EVENT MANAGEMENT SYSTEM
Attending events in the country is always a hectic process especially for anyone who is trying to book for the event. This process of event ticket booking is cumbersome and has led to numerous customer dissatisfaction. Many customers are faced with issues of denied entry due to inefficient systems. 

With all these at hand, I decied to created a simple python based backend system intergrated with a command line interface. 

# Table of contents
- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [TechnologiesUsed](#technologies-used)
- [License](#license)

# Installation
```
# clone the repo
$ git clone <repo>
```

```
# navigate to directory
$ cd <directory>
```

```
# create virtual environment and install dependancies
$ pip install pipenv
$ pipenv shell
```

# Usage
To use this  project:
```
# Run this command in cli
$ python commands.py
```

```
# Run the help to see available options
$ python commands.py --help
```

This backend system is composed of different functinoality
1. The system uses Object Relational Mapping to map python classes to SQL. 
2. Uses SQLAlchemy to apply python logic in database tables
3. Uses Data Structure Algorithm for query results
4. Uses CLI to provide prompts and user input


# Features
The features of the event management system include the following:
1. Venue 
    a. Name of the venue - The name of the venue where the b. event is to be held
    c. Capacity of the venue - Maximum capacity the venue can hold. 
2. Event
    a. Name of the event - Name of the event itself
    b. Date of the event - Date and time of when the event is to be held
    c. Venue - The location of where the event is to be held.
3. Booking
    a. Username - The name of the person making a booking for the event
    b. Event attending - The name of the event attending

# Technologies Used
```
python - For the backend logic of the system
sql alchemy - Handles database management and python mapping
command line interface - Used for user input and interactions with the system

```
# LICENSE

LICENSE [MIT](LICENSE)