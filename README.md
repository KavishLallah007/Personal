# School Event Manager
#### Video Demo: https://youtu.be/Ei--HK1lbfk

#### Description:

This project is a simple event manager for schools. The idea comes from schools in my country which do not have a computerized system for events and are still using traditonal pen and paper to keep track of events of the school. In this project, all users are assumed to be teachers or member of the school administrative staff.

When loading the web app, the user will land on the login page. The login.html contain a form with 2 text field asking the user to input their username and password. The username must be in the following format: firstname.lastname, in lowercase. When the user clicks the login button, in app.py the information provided will be processed as follows, the password will be hashed by using the generate_password_hash() function then both the username and hashed password will be compared with the data in the users table in school.db database. If there is no matching data the user will have to re-enter the login information again. When the user login successfully, the session variable updates with the users' user id and is redirected to the home page.


If the user does not have an account, they can register in the register page. The register.html page consist of a form with four text fields. The user will have to provide their first name, last name, password and retype the password as confirmation and click on Register button. In app.py the information provided by the user is processed as follows, the username of the registered user is automatically generated by concactanating the firstname.lastname and the data about the new user is inserted in the database school.db in table users. If the user submit a form that contains either blank data or the password and confirm password does not match, an error will be generated and the user will not be registered. If all the information provided is correct, the user is registered, the session is updated with data concerning the current person's user id, the data is inserted in the users table and the user is redirected to the home page.


Once logged in the user will be on the home page, index.html. This page consist of a table which will be displayed with all the events which will occur in the current month. In app.py for index, login is required this is achieved by checking if there is a session and if there is no session, the user will be redirected to the login page. The following code is used to get today's date today = datetime.today(). With this information, the current month is calculated and the calculated data is fed into a sql query which seaches all the events in the events table for the current month.


The calender page consists of a table which displays all the events created for the school. In app.py for calender.html, login is required this is achieved by checking if there is a session and if there is no session, the user will be redirected to the login page. A sql select statement is executed to get all the data in the events table.


The event.html page contain a form which users can fill to create new events. The user will need to provide data for Name of the event, date, start time, end time, who can attend and event type. Event type is a drop down with 3 options namely, Exam, Party, Conference. In app.py for event.html, login is required this is achieved by checking if there is a session and if there is no session, the user will be redirected to the login page. def event() handles the code for checking if the user is submitting correct information from the form. If the user submits a form that contain blank data, the new event will not be created and  def event (): will return an error. Onces all the validation is passed, the data is inserted in the database in the events table. When the user successfully create an event, they will automatically be redirected to the calender.html page.


The query.html page contain a form which the user can fill to query details about any event. The user will have to input the event id which they can get on either the calender page or the home page, their username and email address and click submit. In app.py for query.html, login is required this is achieved by checking if there is a session and if there is no session, the user will be redirected to the login page. In def query (): sql queries are executed to get details about the event that the user requested. The event id us used to get the details from the events table and also a nested select statement is executed to get the name of the person who created said event from the users table. Once all the data validation is completed and all the sql queries are executed successfully, the user will be redirected to the result.html page.


The results.html page consists of a table that displays data about the event that the user has queried about in the query.html form. The Event creator, event name, date, start time, end time, who can attend and event type information is displayed in a table.


In app.py, there is a logout function which simply clears the session and redirects the user to "/". Since "/" is the home page and required login to access, the user will be automatically redirected to the login page as the session has been cleared. The database is named school.db and contains only 2 tables namely users table and events table. In the Events table, the user id is used as a foreign key to be able to retrieve the first name and last name of a person who created an event. For simplicity the cs50 SQL library was used to execute all sql queries in this project.