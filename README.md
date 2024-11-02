# Overview

In this repository I wanted to grow my skills with using postgres in python. Where the program stands right now it is just using one table but the schema is setup to have relations across several tables.

This program integrates with a locally hosted postres database using the psycopg2 python library. This could easily be refactored to use a hosted database. To use the program you would just run the main_program file on the command line and from there you could use the database functionality, assuming you had it hosted properly either locally or online.

I had used postgres before but I had not done much with it while integrating python. This gave me a good chance to really delve into it and see how it works. I was able to see how I can run an entire seed file to create the schema for a database as well as delete and modify items in the table.

[Software Demo Video](https://youtu.be/53x-3dQrSS4)

# Relational Database

For this project I am using a postgres database. I chose this because I have worked with postgres a little bit before so I wouldn't need to spend a lot of time just figuring out how it works in general. This would effectively be the beginnings of a property manager software that links properties to their owners with the correct metadata for each one.

{Describe the structure (tables) of the relational database that you created.}
I have 5 tables in the database but so far I am only using one of them. There ia a users table that holds basic user info like first name, last name, email address, and a hashed password for sercurity.

There is then a properties table that is linked to the users through the users unique ID. This holds the highest level data about the property such as the id of the owner, a unique id for itself, the address, and the property type.

The properties table then links every property to another table depending on its property type. There is a multi_unti, single_family, and duplex table that holds the low level data such as property rent, how many units and on the smaller properties whether it is rented or not.

# Development Environment

I used the sql CLI to confirm that my project was working as expected. I could query the tables and see everything going in or out of the DB. I also used VSCode as my IDE to help make development easier.

{Describe the programming language that you used and any libraries.}
I used python in this project and a few of the available libraries to work in this. The libraries I used are psycoppg2, bcrypt, and getpass. I used psycopg2 for all of the database interactions. I used bcrypt to hash and store the password so that it is secure and not just storing a raw password. Lastly I used getpass so that when a user is entering their password it won't be visible in the terminal history.

# Useful Websites

- [Postgresql Docs](https://www.postgresql.org/docs/)

# Future Work

- I have currently only implemented the functionality for adding, modifying, and deleting users so I can implement the other tables' functionality.
- The program currently runs on the command line, I would like to either implement a GUI using TKinter or hosting a flask server that can be hit by a web app.