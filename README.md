# AirBNB Clone project for ALX

![hbnb logo](logo.png)

## Introduction

Welcome to our Airbnb Clone project! This is a platform designed to replicate the core functionality of the popular 
vacation rental and lodging service, Airbnb. Our aim is to provide users with a seamless and user-friendly experience 
for searching, booking, and listing accommodations, just like the original Airbnb.

## Overview

The Airbnb Clone project is a web application that allows users to browse through a wide range of accommodations, 
including apartments, houses, villas, and more. Users can search for properties based on various criteria such as 
location, check-in and check-out dates, number of guests, and price range. They can view detailed property listings, 
complete with photos, descriptions, amenities, and reviews from previous guests.

In addition to searching for accommodations, users can also create accounts, list their own properties for rent, manage 
their bookings, and communicate with other users through our integrated messaging system. Hosts can provide information 
about their properties, set pricing and availability, and interact with potential guests. Guests can submit booking 
requests, view booking history, and leave reviews after their stays.

This project aims to showcase our skills in web development, user experience design, and database management. Whether 
you're a traveler looking for a place to stay or a host interested in renting out your property, our Airbnb Clone 
provides a comprehensive solution.

## The console
This project consists of a console that is used for backend tasks such as creating users, updating information
, deleting users and other miscellaneous tasks.

Shown below is the overview of the interaction

```commandline
Welcome to the hbnb console


(hbnb) help

            Available Commands(For detailed explanation including
            examples, run help <command>):
            
            EOF or quit :   Exits the shell
            help        :   Displays this list
            create      :   Creates a new instance
            show        :   Prints a string representation of an
                            instance based on class name
            destroy     :   Deletes an instance based on the class
                            name and ID
            all         :   Prints all string representation of all instances
            update      :   Updates an instance based on the class name and id
                            by adding or updating attribute (save the change into
                            the JSON file).


```
For an extensive look at the commands with usage examples, run the help command before the command as
shown below.

```commandline
(hbnb) help create

        This method creates a new instance of
        Base Model, saves it to a json file and
        prints the id
        Args:
            cls_name: The class name

        Examples:
            create BaseModel

        Returns:

        
(hbnb) help show

        This method prints the string representation of an instance
        based on the class name and  id
        Args:
            arg

        Examples:
            show <class Name> <id>
            show BaseModel 1234-1234-1234

        Returns:

        
(hbnb) help quit

        Exits the interactive shell
        Args:
            arg:

        Returns:

        
(hbnb) 

```

## Setup

To setup the program, clone this repository then navigate to the root directory. In there you will find 
the script console.py. This program is a plug-and-play kind of program so no installation is required.
Run the script as shown below then use it as guided.

```commandline
$ ./console.py
```



## Usage

To familiarise yourself with the program, run help so that you get an idea of the command you can run and 
the expected arguments and results.

### Create

To start things off, let us create an instance. The command is 

**create class_name** 

This will then create a class and print the ID while saving it to a json file for later reference.
<ul>
<li>If the class name is missing it will display a message indicating as such</li>
<li>As above, if the class name does not exist, there will be a message highlighting so</li>
</ul>

```commandline
(hbnb) create BaseModel
d34afd51-694e-45b7-a65c-18752e2a34fc
(hbnb) 
(hbnb) create HandModel
** class doesn't exist **
(hbnb) 
(hbnb) 
(hbnb) create
** class name missing **
(hbnb) 

```
